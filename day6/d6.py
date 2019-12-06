class Node:
    def __init__(self, name):
        self.name = None
        self.children = []
        self.parent = None
        self.dist = -1

def calc_dist(node: Node, dist: int):
    node.dist = dist
    for c in node.children:
        calc_dist(c, dist+1)

def total_orbits(node: Node):
    orbits = node.dist
    for c in node.children:
        orbits += total_orbits(c)
    return orbits

def process(lines):
    arr = []
    for l in lines:
        arr.append(l.split(')'))

    # Mapping from name -> Node
    d = {}

    # Create Nodes
    for i in arr:
        d[i[0]] = Node(i[0])
    for i in arr:
        if i[1] not in d.keys():
            d[i[1]] = Node(i[1])
    
    # Add children
    for i in arr:
        d[i[0]].children.append(d[i[1]])
    # Add parents
    for i in arr:
        d[i[1]].parent = d[i[0]]

    # Find Root
    p = d[i[0]]
    while p.parent != None:
        p = p.parent

    calc_dist(p, 0)
    print(total_orbits(p))
    
    # Part 2
    you = d['YOU']
    san = d['SAN']

    yous = set()
    p = you
    while p.parent != None:
        p = p.parent
        yous.add(p)
    
    p = san
    while p.parent != None:
        p = p.parent
        if p in yous:
            diff = san.dist + you.dist - 2 * (p.dist+1)
            print(diff)
            break

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]
        process(lines)