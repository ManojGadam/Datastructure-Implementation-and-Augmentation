import bst,hash,rbt,skip,splay
import time
def Hashtable(filename):
    linecount = 0
    hsobj=hash.hashSet()
    with open(filename, 'r') as f:
        for line in f:
            z = line.strip().split()
            linecount += 1
            if z[0]=='1':
                hsobj.insert(z[1])
            else:
                x=hsobj.delete(z[1])
                if x==-1:
                    print("delete object in Line {} not found in the tree.".format(linecount))
    hsobj.print()

def BSTree(filename):
    linecount = 0
    bsobj=bst.BST()
    x=time.time()
    with open(filename, 'r') as f:
        for line in f:
            z = line.strip().split()
            linecount+=1
            if z[0]=='1':
                bsobj.insert(z[1],False)
            else:
                x=bsobj.delete(z[1],False)
                if x==-1:
                    print("delete object in Line {} not found in the tree.".format(linecount))
    bsobj.inOrderTraversal(bsobj.root)

def SplayTree(filename):
    linecount = 0
    splayobj=splay.splayTree()
    with open(filename, 'r') as f:
        for line in f:
            z = line.strip().split()
            linecount+=1
            if z[0]=='1':
                splayobj.insert(z[1],False)
            else:
                x=splayobj.delete(z[1],False)
                if x==-1:
                    print("delete object in Line {} not found in the tree.".format(linecount))
    splayobj.inOrderTraversal(splayobj.root)

def Skiplist(filename):
    linecount = 0
    skipobj=skip.skipList()
    with open(filename, 'r') as f:
        for line in f:
            z = line.strip().split()
            linecount+=1
            if z[0]=='1':
                skipobj.insert(z[1])
            else:
                x=skipobj.delete(z[1])
                if x==-1:
                    print("delete object in Line {} not found in the tree.".format(linecount))
    skipobj.display()
def RBTree(filename):
    linecount = 0
    rbobj=rbt.RBTree()
    with open(filename, 'r') as f:
        for line in f:
            z = line.strip().split()
            linecount+=1
            if z[0]=='1':
                rbobj.insert(z[1],False)
            else:
                x=rbobj.delete(z[1],False)
                if x==-1:
                    print("delete object in Line {} not found in the tree.".format(linecount))
    rbobj.inorder_traversal(rbobj.root)
input_string = input("Enter data structure and file name with tab separated space:\n")
x=time.time()
input_list = input_string.split()
choice=input_list[0]
if choice == '0':
    Hashtable(input_list[1])
elif choice == '1':
    BSTree(input_list[1])
elif choice == '2':
    SplayTree(input_list[1])
elif choice == '3':
    Skiplist(input_list[1])
elif choice == '4':
    RBTree(input_list[1])     
y=time.time()
print()
print(y-x)