import logging


class Euler:

    def __init__(self, inputList):
        try:
            self.inputGraph = list(inputList)
            self.eulerPath = self.calcEulerPath(self.inputGraph)
        except BaseException:
            logging.error("Error occurred while calculate minimal spacing tree:")

    def isConnected(self, graph):
        coloredNodes = {}
        for edge in graph:
            node1 = edge.nodes[0]
            node2 = edge.nodes[1]
            for i in range(2):
                if node1 in coloredNodes.keys():
                    if node2 in coloredNodes.keys()\
                    and coloredNodes[node1] != coloredNodes[node2]:
                        return False
                    else:
                        coloredNodes[node2] = coloredNodes[node1]
                node1, node2 = node2, node1

            if node1 not in coloredNodes.keys() \
            and node2 not in coloredNodes.keys():
                curColor = 0
                for node in coloredNodes:
                    if coloredNodes[node] >= curColor:
                        curColor = coloredNodes[node] + 1
                coloredNodes[node1] = curColor
                coloredNodes[node2] = curColor

        return len(set(coloredNodes.values())) == 1

    def getOddNodesCount(self, graph):
        nodesDegree = {}
        for edge in graph:
            for node in edge.nodes:
                if node not in nodesDegree.keys():
                    nodesDegree[node] = 0
                nodesDegree[node] += 1

        oddNodes = []
        for node in nodesDegree.items():
            if node[1] % 2 == 1:
                oddNodes.append(node[0])

        return oddNodes

    def calcEulerPath(self, graph):
        if self.isConnected(graph):
            oddNodes = self.getOddNodesCount(graph)
            if len(oddNodes) != 0 and len(oddNodes) != 2:
                return None

            mainCycle = None
            restEdges = list(graph)

            while len(restEdges) > 0:
                startNode = None
                endNode = None
                if mainCycle is None and len(oddNodes) == 2:
                    startNode = oddNodes[0]
                    endNode = oddNodes[1]
                else:
                    startNode = endNode = restEdges[0].nodes[0]

                cycle = [startNode]
                curNode = startNode
                while curNode != endNode or len(cycle) < 2: # No loops with single node
                    for idx, edge in enumerate(restEdges):
                        if edge.contains(curNode):
                            curNode = edge.getNeighbour(curNode)
                            cycle.append(curNode)
                            restEdges.pop(idx)
                            break

                if mainCycle is None:
                    mainCycle = cycle
                else:
                    for idx, node in enumerate(mainCycle):
                        isForceExit = False
                        for i in range(len(cycle)):
                            if node == cycle[0]:
                                mainCycle.pop(idx)
                                for newNode in reversed(cycle):
                                    mainCycle.insert(idx, newNode)
                                isForceExit = True
                                break
                            if len(cycle) == 2:
                                cycle = reversed(cycle)
                            else:
                                cycle.pop(0)
                                cycle.append(cycle[0])
                        if isForceExit:
                            break

            return mainCycle
        else:
            return None
