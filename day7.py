import sys
import pprint

class tree_node:

    def __init__(self, name, weight, children):
        self.name = name
        self.weight = int(weight)
        self.children = [] if children == None else children

    def __repr__(self):
        return '{0} \n\tWeight:{1}\n\tChildren:{2}'.format(self.name, self.weight, self.children)


class weighted_tree:
    
    def __init__(self, nodes):
        self.nodes = nodes
        self.find_root()
        self.initialize_weights()

    def find_root(self):
        total = set([node.name for node in self.nodes])
        children = set([child for node in self.nodes for child in node.children])
        root = total - children
        for node in root:
            self.root = node

    def initialize_weights(self):
        self.weights = {}
        for node in self.nodes:
            self.weights[node.name] = node.weight


def main():
    in_file = open(sys.argv[1], 'r')

    nodes = []    
    for line in in_file.readlines():
        nodes.append(line.strip())
    
    tree_nodes = initialize(nodes)
    tree = weighted_tree(tree_nodes)


    print(tree.root)
    pprint.pprint(tree.weights)



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
