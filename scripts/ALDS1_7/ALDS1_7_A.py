import sys
sys.setrecursionlimit(10000000)

def judge_type(vertex):
    if V[vertex].parent == -1:
        return 'root'
    elif V[vertex].left_child != -1:
        return 'internal node'
    else:
        return 'leaf'

def calc_depth(vertex, d): # vertex is only a index
    V[vertex].set_depth(d)
    if V[vertex].right_sibling != -1:
        calc_depth(V[vertex].right_sibling, d)
    if V[vertex].left_child != -1:
        calc_depth(V[vertex].left_child, d+1)


class Node(object):
    def __init__(self, idnum):
        self.id = idnum
        self.parent = -1
        self.left_child = -1
        self.right_sibling = -1
        self.depth = -1
        self.type = None

    def set_parent(self, parent):
        self.parent = parent

    def set_left_child(self, left_child):
        self.left_child = left_child

    def set_right_sibling(self, right_sibling):
        self.right_sibling = right_sibling

    def set_type(self, node_type):
        self.type = node_type

    def set_depth(self, depth):
        self.depth = depth

    def set_child_list(self, child_list):
        self.child_list = child_list

    def __str__(self):
        return "node {}: parent = {}, depth = {}, {}, {}".format(\
                self.id,\
                self.parent,\
                self.depth,\
                self.type,\
                self.child_list\
                )

n = int(input())

V = [Node(i) for i in range(n)]
for i in range(n):
    tmp = [int(j) for j in input().split()]
    idnum = tmp[0]
    l = tmp[2:]
    V[idnum].set_child_list(l) # child
    if l:
        V[idnum].set_left_child(l[0]) # left_child
    for j in range(len(l)):
        V[l[j]].set_parent(idnum) # parent
        if j+1 != len(l):
            V[l[j]].set_right_sibling(l[j+1])

#depth and type
for i in range(n):
    V[i].set_type(judge_type(i))
    
    if V[i].parent == -1:
        r = i
calc_depth(r, 0)

for v in V:
    print(v)
