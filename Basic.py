class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.parent=None
        self.black=False

class RBTree:
    def __init__(self):
        self.root=None
    def searchRec(self, word, node):
        if node == None:
            return None
        elif node.data < word:
            return self.searchRec(word, node.right)
        elif node.data > word:
            return (self).searchRec(word, node.left)
        return node
    def search(self,data):
        return self.searchRec(data,a.root)


    def insert_recursive(self,data,node):
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
        while  node.parent != None and node.parent.black == False:
            if node.parent.parent.left == node.parent:
                uncle= node.parent.parent.right
                if uncle !=None and uncle.black == False :
                    node.parent.black= not (node.parent.black)
                    uncle.black = not uncle.black
                    node.parent.parent.black = not node.parent.parent.black
                    node = node.parent.parent
                else:
                    print("a")
                    break;
            else:
                uncle = node.parent.parent.left
                if uncle !=None and uncle.black == False :
                    node.parent.black= not (node.parent.black)
                    uncle.black = not uncle.black
                    node.parent.parent.black = not node.parent.parent.black
                    node = node.parent.parent
                else:
                    print("a")
                    break;




    def insert(self, data):
        self.root = self.insert_recursive(data, self.root)
        self.root.black = True

a=RBTree()
a.insert("n")
a.insert("z")
a.insert("b")
a.insert("aa")


print(a.root.left.left.black)
#print(a.root.right)






