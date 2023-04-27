
class Node():
    def __init__(self,data):
        self.data = data                                   
        self.parent = None                               
        self.left = None                                 
        self.right = None                                
        self.color = 1                                 
        self.height = 0
class RBTree():
    def __init__(self):
        self.NULL = Node ( None )
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL
        self.height = 0
    def insert(self, key,case):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   
        y = None
        x = self.root

        while x != self.NULL :                          
            y = x
            if node.data < x.data :
                x = x.left
            elif node.data==x.data:
                return
            else :
                x = x.right

        node.parent = y                              
        if y == None :                            
            self.root = node
        elif node.data < y.data :                        
            y.left = node
        else :
            y.right = node
        node.parent = y
        node.height = 1
        self.adjustHeight(node)
        if node.parent == None :                         
            node.color = 0
            if case==True:
                print(self.root.height)
            return

        if node.parent.parent == None :  
            if case==True:             
                print(self.root.height)
            return

        self.fix_Insert ( node )
        if case==True:                   
            print(self.root.height)
    def fix_Insert(self, k):
        while k.parent.color == 1:                       
            if k.parent == k.parent.parent.right:        
                u = k.parent.parent.left                 
                if u.color == 1:                         
                    u.color = 0                           
                    k.parent.color = 0
                    k.parent.parent.color = 1             
                    k = k.parent.parent                   
                else:
                    if k == k.parent.left:                
                        k = k.parent
                        self.right_rotate(k)                        
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:                                         
                u = k.parent.parent.right                 
                if u.color == 1:                          
                    u.color = 0                           
                    k.parent.color = 0
                    k.parent.parent.color = 1             
                    k = k.parent.parent                   
                else:
                    if k == k.parent.right:               
                        k = k.parent
                        self.left_rotate(k)                        
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)              
            if k == self.root:                            
                break
        self.root.color = 0  
    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node
    def left_rotate ( self , x ) :
        y = x.right                                      
        x.right = y.left
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent                        
        if x.parent == None : 
            self.root = y  
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y
        self.heightCheck(x)
    def right_rotate ( self , x ) :
        y = x.left                                       
        x.left = y.right                             
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent                             
        if x.parent == None :                          
            self.root = y                               
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y 
        self.heightCheck(x)
    def fix_Delete ( self , x ) :
        while x != self.root and x.color == 0 :           
            if x == x.parent.left :                       
                s = x.parent.right                        
                if s.color == 1 :                         
                    s.color = 0                           
                    x.parent.color = 1                    
                    self.left_rotate ( x.parent )                  
                    s = x.parent.right
                
                if s.left.color == 0 and s.right.color == 0 :
                    s.color = 1                           
                    x = x.parent
                else :
                    if s.right.color == 0 :               
                        s.left.color = 0                  
                        s.color = 1                       
                        self.right_rotate ( s )                     
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0                    
                    s.right.color = 0
                    self.left_rotate ( x.parent )                  
                    x = self.root
            else :                                        
                s = x.parent.left                         
                if s.color == 1 :                         
                    s.color = 0                           
                    x.parent.color = 1                    
                    self.right_rotate ( x.parent )                  
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0 :
                    s.color = 1
                    x = x.parent
                else :
                    if s.left.color == 0 :                
                        s.right.color = 0                 
                        s.color = 1
                        self.left_rotate ( s )                     
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate ( x.parent )
                    x = self.root
        x.color = 0
        
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
    
    def transplant ( self , u , v ) :
        if u.parent == None :
            self.root = v
        elif u == u.parent.left :
            u.parent.left = v
        else :
            u.parent.right = v
        if v!=None:
            v.parent = u.parent
            self.adjustHeight(v)
        else:
            self.adjustHeight(u.parent) 
    def delete ( self , data ,case) :
        node=self.root        
        z = self.NULL
        while node != self.NULL :                          
            if node.data == data :
                z = node

            if node.data < data :
                node = node.right
            else  :
                node = node.left
        if z == self.NULL :                                
            return -1
        y = z
        y_original_color = y.color                          
        if z.left == self.NULL :                            
            x = z.right                                     
            self.transplant ( z , z.right )            
        elif (z.right == self.NULL) :                       
            x = z.left                                      
            self.transplant ( z , z.left )             
        else :                                              
            y = self.minimum ( z.right )                    
            y_original_color = y.color                      
            x = y.right
            if y.parent == z :                              
                x.parent = y                                
            else :
                self.transplant ( y , y.right )
                y.right = z.right
                y.right.parent = y

            self.transplant ( z , y )
            y.left = z.left
            y.left.parent = y
            y.color = z.color
            self.adjustHeight(x)
        if y_original_color == 0 :                          
            self.fix_Delete ( x )
        if(case==True):
            print(self.root.height)
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
    def inorder_traversal(self, node):
        if node == None or node.data == None:
            return
        self.inorder_traversal(node.left)
        print(node.data,end=' ')
        self.inorder_traversal(node.right)

if __name__ == "__main__":
    tree = RBTree()
    tree.insert(10,True)
    tree.insert(20,True)
    tree.insert(30,True)
    tree.insert(5,True)
    tree.insert(4,True)
    tree.insert(2,True)
    tree.insert(4,True)
    tree.delete(2,True)
    tree.delete(20,True)
    tree.delete(50,True)
    tree.inorder_traversal(tree.root)

