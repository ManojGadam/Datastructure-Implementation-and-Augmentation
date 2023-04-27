import random
class Node:
    def __init__(self,key=None,level=0):
        self.key = key
        self.forward = [None] *(level+1)

class skipList:
    def __init__(self,maxLevel = 5, p = 0.5):
        self.head = Node(-1,maxLevel)
        self.level = 0
        self.maxLevel = maxLevel
        self.p = p
        

    
    def randomLevel(self):
           level = 0
           while random.random()<=self.p and level < self.maxLevel:
               level+=1
           return level        
            
    def insert(self,item):
        [cur,update] = self.search(item)
        if cur and cur.key == item:
            return
        else:
             level = self.randomLevel()
             level = 5
             if level > self.level:
                 update[self.level+1:level+1] = [self.head]*(level-self.level)
                 self.level = level
             cur = Node(item,level)
             for i in range(level+1):
                 cur.forward[i] = update[i].forward[i]
                 update[i].forward[i] = cur       
    
    def delete(self,item):
        [node,update] = self.search(item)
        if node == None or (node and node.key!=item):
            return -1
        for i in range(len(node.forward)):
            update[i].forward[i] = node.forward[i]
            if update[i].forward[i] == node:
                update[i].forward[i] = node.forward[i]
        while self.level > 0 and not self.head.forward[self.level]:
            self.level -= 1
    
    def search(self,item):
        node = self.head
        update = [None]* (self.level+1)
        for i in range(self.level,-1,-1):
            while node.forward[i] and node.forward[i].key<item:
                node = node.forward[i]
            update[i] = node
        node = node.forward[0]
        return [node,update]               
    
    def display(self):
        head = self.head
        i=0
        #for i in range(self.level+1):
        output=""
        node = head.forward[i]
        while(node!=None):
            output += str(node.key) + " "                
            node = node.forward[i]
        print(output)    

if __name__ == "__main__":        
    skip = skipList()
    skip.insert(1)            
    skip.insert(2)            
    skip.insert(3)            
    skip.insert(4)            
    skip.insert(5)            
    skip.delete(3)

       
#case 1 
# skip.insert(1)            
# skip.insert(2)            
# skip.insert(3)            
# skip.insert(4)            
# skip.insert(5)            
# skip.delete(3) 


#case 2
# skip.insert('apple ipod')            
# skip.insert('baseball')
# skip.insert('cat race')            
# skip.insert('dogs and rain')            
# skip.insert('lion sin')              
# skip.delete('cat race')            


#case 3
#skip.insert(10.5)    
#skip.delete(10.5)    
        
           
                 
# cur = self.head
# update = [None]*(self.maxLevel+1)
# for i in range(self.level,-1,-1):
#     while cur.forward[i] and cur.forward[i].key < item:
#         cur = cur.forward[i]
#     update[i]=cur    
# cur = cur.forward[0] 