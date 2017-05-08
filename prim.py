import logging


class Prim:

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

            # Pick adjacency edges for current tree
            for node in nodes:
                adjacencyEdges = adjacencyEdges.union(
                    set([edge for edge in graph
                         if edge.contains(node)
                            and not edge.getNeighbour(node) in nodes])
                )

            if len(adjacencyEdges) == 0:
                return None

            # Save only minimal edge
            adjacencyEdges = adjacencyEdges - set(minSpacingTree)
            minSpacingTree.append(min(adjacencyEdges))

            # Save new edge as included in tree
            for edge in minSpacingTree:
                nodes = nodes.union(set(edge.nodes))

        return minSpacingTree
