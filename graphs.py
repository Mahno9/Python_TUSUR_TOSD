class Node:
    name = None

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Edge:
    def __init__(self, node1, node2, value=None):
        self.nodes = []
        self.nodes.append(node1)
        self.nodes.append(node2)
        if value is not None:
            self.value = value

    def contains(self, node):
        return node in self.nodes

    def isAdjacencyWith(self, other):
        if set(self.nodes).difference(set(other.nodes)) is not None and \
                        set(self.nodes).intersection(set(other.nodes)) is not None:
            return True
        return False

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if hasattr(self, "value"):
            return "({0} - {2} - {1})" \
                .format(self.nodes[0], self.nodes[1], self.value)
        return "({0} {1})".format(self.nodes[0], self.nodes[1])
