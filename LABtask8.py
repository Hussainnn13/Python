def minimax(node, depth, y):
    if depth == 0 or x(node):
        return evaluate(node)

    if y:
        maxeval = float('-inf')
        for child in get_children(node):
            eval = minimax(child, depth - 1, False)
            maxeval = max(maxeval, eval)
        return maxeval
    else:
        mineval = float('inf')
        for child in get_children(node):
            eval = minimax(child, depth - 1, True)
            mineval = min(mineval, eval)
        return mineval

def x(node):
    return False

def evaluate(node):
    return 0

def get_children(node):
    return []

if __name__ == "__main__":
    pivot = None
    depth = 3
    bestscore = minimax(pivot, depth, True)
    print("Best score for maximizing player:", bestscore)
