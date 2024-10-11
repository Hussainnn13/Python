class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

def bfs(start, visited=None):
    if visited is None:
        visited = set()
    queue = [start]

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            print(current.value)
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

if __name__ == "__main__":
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")

    a.addNeighbor(b)
    a.addNeighbor(c)
    b.addNeighbor(d)
    b.addNeighbor(e)
    c.addNeighbor(f)
    e.addNeighbor(f)

    print("BFS starting from node A:")
    bfs(a)
