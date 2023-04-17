from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

messageNode = Tk()
messageNode.withdraw()
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
            return 0

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
                node=node.left     #do not add repeated
            elif data == node.data:
                break
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
        while node.parent is not None and node.parent.black == False:
            if node.parent.parent.left == node.parent:  # uncle on the right
                uncle = node.parent.parent.right
                if uncle is not None and uncle.black == False:  # case 1: uncle is red
                    node.parent.black = not node.parent.black
                    uncle.black = not uncle.black
                    node.parent.parent.black = not node.parent.parent.black
                    node = node.parent.parent
                else:  # case 2: uncle is black and on the right
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.black = not node.parent.black
                    node.parent.parent.black = not node.parent.parent.black
                    self.rotate_right(node.parent.parent)
            else:  # uncle on the left
                uncle = node.parent.parent.left
                if uncle is not None and uncle.black == False:  # case 1: uncle is red
                    node.parent.black = not node.parent.black
                    uncle.black = not uncle.black
                    node.parent.parent.black = not node.parent.parent.black
                    node = node.parent.parent
                else:  # case 2: uncle is black and on the left
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.black = not node.parent.black
                    node.parent.parent.black = not node.parent.parent.black
                    self.rotate_left(node.parent.parent)
        self.root.black = True

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
        node.right = right_child.left

        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
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
# messageNode.mainloop()
while (1):
    choice =simpledialog.askstring(title="Choice", prompt="write the number of your choice\n 1-Load Dictionary   \n 2-insert a word \n 3-search for a word \n 4-return RB tree height \n 5- return RB tree size\n 6-exit \n")
    if choice =='1':
        f = open("egr.txt", "r")

        for line in f:
            a.insert(line)
        f.close()
    elif choice == '2':
        f = open("egr.txt","a")
        word = simpledialog.askstring(title="Choice",prompt="enter a word to Insert it \n ") #INsert word if it is not int hte dictionary
        if a.search(word) is not None:
            messagebox.showinfo( "Inserting Result",f"The word {word} is already in the dictionary can't insert it!",parent =messageNode)
        else:
            a.insert(word)
            f.write("\n")
            f.write(word)
            messagebox.showinfo("inserted successfully",parent =messageNode)
        f.close()

    elif choice == "3":
        word = simpledialog.askstring(title="Choice",prompt="enter a word to check if it is in tree or not\n") #Make sure a specific word in the dictionary
        if a.search(word) is not None:
            messagebox.showinfo("Searching Result",f"The word {word} is in the dictionary!",parent =messageNode)
        else:
            messagebox.showinfo( "Searching Result",f"it is not in the dictionary",parent =messageNode)


    elif choice == "4":
        height = a.height_of_tree(a.root)
        print(height)
        height += 1        # increase one due to null nodes!
        print(height)
        messagebox.showinfo("Height result",f"height of the tree is = {height}",parent =messageNode)

    elif choice == "5":
        messagebox.showinfo("Size result",f"Size of the tree = {a.size_of_tree(a.root)}",parent =messageNode)
    elif choice =="6":
        break
    print("\n\n")
