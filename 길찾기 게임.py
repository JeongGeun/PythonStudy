import sys
sys.setrecursionlimit(10**6)
post=[]
pre=[]

class Node:
    def __init__(self,x,y,left,right,num):
        self.x=x
        self.y=y
        self.left=left
        self.right=right
        self.num=num

def makeTree(root,node):
    if root.x<node.x:
        if root.right==None:
            root.right=node
        else:
            makeTree(root.right,node)
    else:
        if root.left==None:
            root.left=node
        else:
            makeTree(root.left,node)

def postorder(root):
    if root!=None:
        post.append(root.num)
    if root.left!=None:
        postorder(root.left)
    if root.right!=None:
        postorder(root.right)


def preorder(root):
    if root.left != None:
        preorder(root.left)
    if root.right != None:
        preorder(root.right)
    if root != None:
        pre.append(root.num)


def solution(nodeinfo):
    answer = [[]]
    v=[]
    for i, val in enumerate(nodeinfo):
        a,b=val
        v.append([[b,a],i+1])
    v=sorted(v,key=lambda x:[-x[0][0],x[0][1]] )
    root=None
    for i,node in enumerate(v):
        if i==0:
            root=Node(node[0][1],node[0][0],None,None,node[1])
        else:
            makeTree(root,Node(node[0][1],node[0][0],None,None,node[1]))
    postorder(root)
    preorder(root)
    return [post,pre]
solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])







