class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            print("Duplicate entry", key, "ignored")
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def minNode(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    def depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def mirror(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.mirror(root.left)
            self.mirror(root.right)

    def copy(self, root):
        if root is None:
            return None
        new = Node(root.key)
        new.left = self.copy(root.left)
        new.right = self.copy(root.right)
        return new

    def showParents(self, root):
        if root:
            if root.left or root.right:
                print("Parent", root.key, end=": ")
                if root.left:
                    print("left =", root.left.key, end=" ")
                if root.right:
                    print("right =", root.right.key, end=" ")
                print()
            self.showParents(root.left)
            self.showParents(root.right)

    def showLeaves(self, root):
        if root:
            if root.left is None and root.right is None:
                print(root.key, end=" ")
            self.showLeaves(root.left)
            self.showLeaves(root.right)

    def levelOrder(self, root):
        if root is None:
            print("Tree is empty")
            return
        queue = [root]
        level = 0
        while len(queue) > 0:
            print("Level", level, ":", end=" ")
            count = len(queue)
            for i in range(count):
                cur = queue.pop(0)
                print(cur.key, end=" ")
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            print()
            level += 1


tree = BST()
root = None

while True:
    print("\n--- BST Menu ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display (Inorder, Preorder, Postorder)")
    print("5. Depth of tree")
    print("6. Mirror image")
    print("7. Create copy")
    print("8. Parents with children")
    print("9. Leaf nodes")
    print("10. Level wise display")
    print("11. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        val = int(input("Enter value: "))
        root = tree.insert(root, val)

    elif ch == 2:
        val = int(input("Enter value to delete: "))
        if tree.search(root, val):
            root = tree.delete(root, val)
            print("Deleted", val)
        else:
            print(val, "not found")

    elif ch == 3:
        val = int(input("Enter value to search: "))
        if tree.search(root, val):
            print(val, "found in tree")
        else:
            print(val, "not found")

    elif ch == 4:
        print("Inorder: ", end="")
        tree.inorder(root)
        print("\nPreorder: ", end="")
        tree.preorder(root)
        print("\nPostorder: ", end="")
        tree.postorder(root)
        print()

    elif ch == 5:
        print("Depth of tree:", tree.depth(root))

    elif ch == 6:
        m = tree.copy(root)
        tree.mirror(m)
        print("Mirror image (inorder): ", end="")
        tree.inorder(m)
        print()
        tree.levelOrder(m)

    elif ch == 7:
        c = tree.copy(root)
        print("Copied tree (inorder): ", end="")
        tree.inorder(c)
        print()

    elif ch == 8:
        tree.showParents(root)

    elif ch == 9:
        print("Leaf nodes: ", end="")
        tree.showLeaves(root)
        print()

    elif ch == 10:
        tree.levelOrder(root)

    elif ch == 11:
        break

    else:
        print("Invalid choice")
