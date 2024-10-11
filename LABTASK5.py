class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def addn(self, neighbor):
        self.neighbors.append(neighbor)


def dfs(startingvalue):
    stack = [startingvalue]
    visited = set()

    while stack:
        pivot = stack.pop()
        
        if pivot not in visited:
            visited.add(pivot)
            print(pivot.value)              
            for neighbor in pivot.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)



if __name__ == "__main__":
    
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")

    
    a.addn(b)
    a.addn(c)
    b.addn(d)
    c.addn(e)

    
    print("DFS starting from node A:")
    dfs(a)
#LAB Task 5