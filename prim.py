import logging
from graphs import Edge


class Prim:
    # inputGraph = []
    # minimalSpacingTree = []

    def __init__(self, inputList):
        try:
            self.inputGraph = list(inputList)
            self.minimalSpacingTree = self.prim(self.inputGraph)
        except BaseException:
            logging.error("Error occurred while calculate minimal spacing tree:")

    def prim(self, graph):
        nodes = set([graph[0].nodes[0]])  # Take first found node for start
        minSpacingTree = []
        nodesCount = len(set([node for edge in graph for node in edge.nodes]))

        while nodesCount > len(nodes):
            adjacencyEdges = set()
            for node in nodes:
                adjacencyEdges = adjacencyEdges.union(
                    set([edge for edge in graph
                         if edge.contains(node)
                            and not edge.getNeighbour(node) in nodes])
                )
            adjacencyEdges = adjacencyEdges - set(minSpacingTree)
            minSpacingTree.append(min(adjacencyEdges))
            for edge in minSpacingTree:
                nodes = nodes.union(set(edge.nodes))

        return minSpacingTree
