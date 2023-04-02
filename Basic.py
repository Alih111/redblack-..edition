from tkinter import messagebox
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
        self.black=False     #black and red node

class RBTree:
    def __init__(self):
        self.root=None

    def _searchRec(self, word, node):
        if node == None:
            return None
        elif node.data < word:
            return self._searchRec(word, node.right)
        elif node.data > word:
            return (self)._searchRec(word, node.left)
        return node
    def search(self,data):
        return self._searchRec(data,a.root)

    def _size_recursive(self,root):
        if root is None:
            return 0
        return 1 + self._size_recursive(root.left) + self._size_recursive(root.right)
    def size_of_tree(self,root):
        return self._size_recursive(root)


    def _height_recursive(self,root):

        if root is None:
            return -1

        left_height = self._height_recursive(root.left)
        right_height = self._height_recursive(root.right)

        return 1 + max(left_height, right_height)

    def height_of_tree(self,root):
        return self._height_recursive(root)



    def insert_recursive(self,data,node):
        global left
        if self.root == None:
            a=Node(data)
            return a
        parent=node
        while node != None:
            parent=node
            if data > node.data:
                right=True
                left=False
                node=node.right
            elif data < node.data:
                left=True
                right=False
                node=node.left
        newNode=Node(data)
        newNode.parent=parent
        if left:
            parent.left=newNode
        else:
            parent.right=newNode
        self.fixupRedBlackTree(newNode)
        return self.root

    def fixupRedBlackTree(self, node):
        self.root.black = True
        while node.parent is not None and node.parent.black == False:  # case 1 uncle is red
            if node.parent.parent.left == node.parent:  # uncle on the right
                uncle = node.parent.parent.right
                if uncle is not None and uncle.black == False:  # uncle is red
                    node.parent.black = not (node.parent.black)
                    uncle.black = not uncle.black
                    node.parent.parent.black = not node.parent.parent.black
                    node = node.parent.parent
                else:  # uncle is black and its on the right and node is on the left of parent
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    node.parent.black = True
                    node.parent.parent.black = False
                    self.rotate_right(node.parent.parent)
                    # swap color
                    # break;
            else:
                uncle = node.parent.parent.left
                if uncle != None and node.parent.black == False:
                    node.parent.black = not (node.parent.black)
                    uncle.black = not uncle.black
                    node.parent.parent.black = not node.parent.parent.black
                    node = node.parent.parent
                else:  # uncle is red and its on the right
                    # case 2b: uncle node is black
                    if node == node.parent.left:
                        self.rotate_right(node.parent)

                    node.parent.color = True
                    node.parent.parent.color = False
                    self.rotate_left(node.parent.parent)


    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def rotate_left(self, node):
        right_child = node.right
        if right_child is None:
            return
        node.right = right_child.left

        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def insert(self, data):
        self.root = self.insert_recursive(data, self.root)
        self.root.black = True

a=RBTree()

# a.insert("n")
# a.insert("z")
# a.insert("b")
# # a.insert("aa")
# # a.insert("gg")
# # a.insert("y")
# # a.insert("f")
# # a.insert("d")
# # a.insert("w")
# # a.insert("t")
# # a.insert("v")
#
# # a.insert("h")
# # print(a.root.right.left.data)

f = open("egr.txt","r")

for line in f:
     print(line)
     a.insert(line)
f.close()


print(a.size_of_tree(a.root))

print(a.height_of_tree(a.root))


print(a.size_of_tree(a.root)) # dictionary size is the number of elements
word = input("enter a word to Insert it") #INsert word if it is not int hte dictionary
if a.search(word) is not None:
    messagebox.showinfo("showinfo", f"The word {word} is already in the dictionary can't insert it!")
else:
    a.insert(word)

word = input("enter a word to check if it is in tree or not") #Make sure a specific word in the dictionary
if a.search(word) is not None:
    messagebox.showinfo("showinfo", f"The word {word} is in the dictionary!")









