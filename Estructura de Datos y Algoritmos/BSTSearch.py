class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return Node(data)

    if data <= node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node


def search(root, data):
    if root is None or root.data == data:
        return root

    if data < root.data:
        return search(root.left, data)

    return search(root.right, data)


def delete(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        if root.left is None:
            temp = root.right
            return temp

        elif root.right is None:
            temp = root.left
            return temp

        temp = minValueNode(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left

    return current


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level - 1)
        printCurrentLevel(root.right, level - 1)


def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)
        print()


if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 25)
    insert(root, 45)
    insert(root, 75)
    insert(root, 55)
    insert(root, 85)
    insert(root, 40)
    insert(root, 35)
    insert(root, 28)

    print("Inorder")
    inorder(root)

    print("\n\nPreorder")
    preorder(root)

    print("\n\nPostorder")
    postorder(root)

    print("\n\nHeight")
    print(height(root))

    print("\nCurrent Level")
    printCurrentLevel(root, 3)

    print("\n\nLevel Order")
    printLevelOrder(root)


