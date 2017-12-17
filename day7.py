import sys
import pprint

class tree_node:

    def __init__(self, name, weight, children):
        self.name = name
        self.weight = int(weight)
        self.children = [] if children == None else children

    def __repr__(self):
        return '{0} \n\tWeight:{1}\n\tChildren:{2}'.format(self.name, self.weight, self.children)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return hash(self) == hash(other)


class weighted_tree:
    
    def __init__(self, nodes):
        self.nodes = set(nodes)
        self.find_root()
        self.compute_subs()

    def find_root(self):
        total = set([node.name for node in self.nodes])
        children = set([child for node in self.nodes for child in node.children])
        root = total - children
        for node in root:
            self.root = node

    def compute_subs(self):
        self.totalWeights = {}
        toCheck = [self.get_node(self.root)]
        seen = set()
        while toCheck != []:
            node = toCheck.pop()
            seen.add(node)
            self.totalWeights[node] = node.weight
            for child in node.children:
                curr = self.get_node(child)
                if curr not in seen:
                    toCheck.append(curr)
                self.totalWeights[node] += curr.weight

    
    def check_balance(self):
        toCheck = [self.get_node(self.root)]
        seen = set()
        while toCheck != []:
            node = toCheck.pop()
            seen.add(node)
            if node.children != []:
                known = self.get_node(node.children[0])
                for child in node.children:
                    child = self.get_node(child)
                    if self.totalWeights[known] != self.totalWeights[child]:
                        return (self.totalWeights[known], self.totalWeights[child])
                    if child not in seen:
                         toCheck.append(child)
    
    def get_node(self, toGet):
        for node in self.nodes:
            if node == toGet:
                return node



def main():
    in_file = open(sys.argv[1], 'r')

    nodes = []    
    for line in in_file.readlines():
        nodes.append(line.strip())
    
    tree_nodes = initialize(nodes)
    tree = weighted_tree(tree_nodes)


    pprint.pprint(tree.check_balance())


def initialize(nodes):
    clean_nodes = []
    for node in nodes:
        adjacency = None
        if '->' in node:
            node = node.split('->')
            adjacency = [child.strip() for child in node[-1].split(', ')]
            node = node[0]
        
        node = node.split()
        weight = node[1].strip('(').strip(')')
        node = node[0]

        clean_nodes.append(tree_node(node, weight, adjacency))

    return clean_nodes


if __name__ == "__main__":
    main()
