class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(start, goal, grid):
    open_list = []
    closed_list = []
    start_node = Node(start)
    open_list.append(start_node)

    while open_list:
        current = min(open_list, key=lambda n: n.f)

        if current.position == goal:
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        open_list.remove(current)
        closed_list.append(current)

        neighbors = [(current.position[0] + dx, current.position[1] + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]

        for next_pos in neighbors:
            if (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0]) and grid[next_pos[0]][next_pos[1]] == 0):
                neighbor = Node(next_pos, current)
                if neighbor in closed_list:
                    continue

                neighbor.g = current.g + 1
                neighbor.h = heuristic(neighbor.position, goal)
                neighbor.f = neighbor.g + neighbor.h

                if all(neighbor.g < n.g for n in open_list if n.position == neighbor.position):
                    open_list.append(neighbor)

    return None

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    start, goal = (0, 0), (4, 4)
    path = astar(start, goal, grid)
    print("Path from start to goal:", path)


# used help from chatgpt to debug and in the end
