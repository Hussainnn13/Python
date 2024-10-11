class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)

if __name__ == "__main__":
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    root.right.left = Node("F")
    root.right.right = Node("G")

    print("Preorder:")
    preorder(root)

    print("\nInorder:")
    inorder(root)

    print("\nPostorder:")
    postorder(root)


#Took help from chatgpt