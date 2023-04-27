class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

class splayTree():
    def __init__(self):
        self.root = None
        self.height = 0 
             
    def left_rotate(self,x):
         y = x.right
         x.right = y.left
         if y.left != None:
            y.left.parent = x
         y.parent = x.parent
         if x.parent == None:
            self.root = y   
         elif x == x.parent.left:
             x.parent.left = y
         elif x == x.parent.right:
            x.parent.right = y
         y.left = x          
         x.parent = y
         self.heightCheck(x)
     
    def right_rotate(self,x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x 
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
              x.parent.left = y
        elif  x== x.parent.right:
              x.parent.right = y
        y.right = x      
        x.parent = y
        self.heightCheck(x)   
    
    def splay(self,x):
        if x==None:return
        while x.parent!=None:
            if x.parent.parent == None:
                if x == x.parent.left:
                    self.right_rotate(x.parent)    
                else:
                    self.left_rotate(x.parent)
            elif x== x.parent.left and x.parent == x.parent.parent.left:
                self.right_rotate(x.parent.parent)
                self.right_rotate(x.parent)
            elif x== x.parent.right and x.parent == x.parent.parent.right:
                self.left_rotate(x.parent.parent)
                self.left_rotate(x.parent)
            elif x== x.parent.left and x.parent == x.parent.parent.right:
                self.right_rotate(x.parent)
                self.left_rotate(x.parent)
            else:
                self.left_rotate(x.parent)
                self.right_rotate(x.parent)
                
                
                        
    def insert(self,key,case):
        node = Node(key)
        current = self.search(node)
        if current == None:
            self.root = node
        elif current.key == node.key:
               self.splay(node)
               return                     
        elif node.key<current.key:
            current.left = node
        else:
            current.right = node
        node.parent = current
        node.height = 1
        self.adjustHeight(node)
        self.splay(node)
        if(case==True):
            print(self.root.height)        

    def search(self,node):
        root = self.root
        current = None
        while root!=None:
            current = root
            if  node.key<current.key :
                root = root.left
            elif node.key == current.key:
                break    
            else:
                root = root.right
        return current        
    
    
    
    def adjustHeight(self,node):
        current = node.parent
        if current == None:
            self.heightSafe(self.root)
        while current != None:
            if current.left == None and current.right == None:
                current.height = 1 
            elif current.left == None:
                current.height = current.right.height+1
            elif current.right == None:
                current.height = current.left.height+1 
            else:                      
                current.height = max(current.left.height,current.right.height)+1
            current = current.parent

           
    
    def inOrderTraversal(self,node):
        if node == None:
            return
        self.inOrderTraversal(node.left)
        print(node.key,end=' ')
        self.inOrderTraversal(node.right)
        
    def delete(self,x,case):
        x = Node(x)
        root = self.root
        node = None
        current = None
        t = 0
        while(root!=None):
            current = root
            if current.key == x.key:
                node = current
                break
            elif x.key<current.key:
                root = root.left
            else:
                root = root.right
        if node == None:
            self.splay(current)
            return -1    
        elif node.left == None:
            self.transplant(node,node.right)
            self.splay(node.parent)
        elif node.right == None:
            self.transplant(node,node.left)
            self.splay(node.parent)
        else:
            successor = self.treeMinimum(node.right)
            if successor != node.right:
                self.transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.transplant(node,successor)    
            successor.left = node.left
            successor.left.parent  = successor
            self.adjustHeight(successor)
            self.splay(successor.parent)
            root = self.root
        if(case==True):
            print(self.root.height)   
    
    
    
    def transplant(self,u,v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v!=None:
            v.parent = u.parent
            self.adjustHeight(v)
        else:
            self.adjustHeight(u.parent)        
      
    
    def treeMinimum(self,x):
        while x.left !=None:
            x = x.left
        return x            

    def heightSafe(self,current):
        if current.left == None and current.right == None:
                current.height = 1 
        elif current.left == None:
                current.height = current.right.height+1
        elif current.right == None:
                current.height = current.left.height+1 
        else:                      
            current.height = max(current.left.height,current.right.height)+1 

    def heightCheck(self,current):
        while current!=None:
            if current.left == None and current.right == None:
                    current.height = 1 
            elif current.left == None:
                    current.height = current.right.height+1
            elif current.right == None:
                    current.height = current.left.height+1 
            else:                      
                current.height = max(current.left.height,current.right.height)+1 
            current = current.parent
if __name__ == "__main__":        
    tree = splayTree()
    tree.insert(15)             
    tree.insert(10)             
    tree.insert(17)  
    tree.insert(7)             
    tree.insert(13)             
    tree.insert(16)
    tree.delete(13)             
    tree.inOrderTraversal(tree.root)