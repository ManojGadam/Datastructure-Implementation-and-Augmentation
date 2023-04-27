import bst,hash,rbt,splay

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
def BSTree(filename):
    linecount = 0
    bsobj=bst.BST()
    with open(filename, 'r') as f:
        for line in f:
            z = line.strip().split()
            linecount+=1
            if z[0]=='1':
                bsobj.insert(z[1],True)
            else:
                x=bsobj.delete(z[1],True)
                if x==-1:
                    print("delete object in Line {} not found in the tree.".format(linecount))
def SplayTree(filename):
    linecount = 0
    splayobj=splay.splayTree()
    with open(filename, 'r') as f:
        for line in f:
            z = line.strip().split()
            linecount+=1
            if z[0]=='1':
                splayobj.insert(z[1],True)
            else:
                x=splayobj.delete(z[1],True)
                if x==-1:
                    print("delete object in Line {} not found in the tree.".format(linecount))
def RBTree(filename):
    linecount = 0
    rbobj=rbt.RBTree()
    with open(filename, 'r') as f:
        for line in f:
            z = line.strip().split()
            linecount+=1
            if z[0]=='1':
                rbobj.insert(z[1],True)
            else:
                x=rbobj.delete(z[1],True)
                if x==-1:
                    print("delete object in Line {} not found in the tree.".format(linecount))
input_string = input()
input_list = input_string.split()
choice=input_list[0]
if choice == '0':
    print("Hashtable height not available!")
elif choice == '1':
    BSTree(input_list[1])
elif choice == '2':
    SplayTree(input_list[1])
elif choice == '3':
    print("Skip list height not available!")
elif choice == '4':
    RBTree(input_list[1])     