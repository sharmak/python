# -*- coding: utf-8 -*-
"""
Created on Tue Oct 07 00:01:41 2014

@author: admin
"""
from collections import deque
class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.node = value
        self.left = left
        self.right = right
class Tree(object):
    def __init__(self, root):
        self.root = root
    def _preOrder(self, cur):
        if cur is None:
            return None
        print cur.node
        self._preOrder(cur.left)
        self._preOrder(cur.right)
    def preOrder(self):
        self._preOrder(self.root)
    def _postOrder(self, cur):
        if cur is None:
            return None
        self._postOrder(cur.left)
        self._postOrder(cur.right)
        print cur.node
    def postOrder(self):
        self._postOrder(self.root)
    def _inOrder(self, cur):
        if cur is None:
            return None
        self._inOrder(cur.left)
        print cur.node
        self._inOrder(cur.right)
    def inOrder(self):
        self._inOrder(self.root)
    def _size(self, cur):
        #print cur
        if cur is None:
            return 0
        else:
            return self._size(cur.left) + self._size(cur.right) + 1
    def size(self):
        return self._size(self.root)
    def _height(self, cur):
        if cur is None:
            return 0
        else:
            return 1 + max(self._height(cur.left), self._height(cur.right))
    def height(self):
        return self._height(self.root)
    def levelOrder(self):
        d = deque()
        d.append(self.root)
        while len(d) > 0:
            nod = d.popleft()
            print nod.node
            if nod.left is not None:
                d.append(nod.left)
            if nod.right is not None:
                d.append(nod.right)
        
            
        
        
        
        
def identical(cur1, cur2):
    #print cur1.node
    #print cur2.node
    if cur1 is not None \
        and cur2 is not None \
        and cur1.node == cur2.node:
        return True and identical(cur1.left, cur1.left)\
                    and identical(cur2.right, cur2.right)
    elif cur1 is None and cur2 is None:
        return True
    else:
        return False

def mirror(cur):
    if cur is None:
        return None
    l = mirror(cur.left)
    r = mirror(cur.right)
    cur1 = deepcopy(cur)
    cur1.left = r
    cur1.right = l
    return cur1

        
    
def construct_tree(pre_order, in_order):
    print pre_order
    print in_order
    if len(pre_order) == 0:
        return None
    elif len(pre_order) == 1:
        return TreeNode(pre_order[0])
    elif len(pre_order) == 2:
        n1 = TreeNode(pre_order[0])
        n2 = TreeNode(pre_order[1])
        if pre_order[0] == in_order[0]:
            root = n1
            root.right = n2
            return root
        else:
            root = n2
            root.left = n1
            return root
    else:
        mid = len(pre_order) / 2
        print mid        
        root = TreeNode(pre_order[0])
        mid_index = in_order.index(root.node)
        new_in_order_left = in_order[:mid_index]
        new_in_order_right = in_order[mid_index+1:]
        new_pre_order_left = pre_order[1:mid+1]
        new_pre_order_right = pre_order[mid+1:]
        root.left = construct_tree(new_pre_order_left, new_in_order_left)
        root.right = construct_tree(new_pre_order_right, new_in_order_right)
        return root
        
        
st = list()    
def root_to_leaf_path(cur):
    if cur is None:
        return None
    elif cur.left is None and cur.right is None:
        st.append(cur.node)
        print st
        st.pop()
        return None
    else:
        st.append(cur.node)
        root_to_leaf_path(cur.left)
        root_to_leaf_path(cur.right)
        st.pop()        
        
    
    
from copy import deepcopy    
if __name__ == '__main__':
    n1 = TreeNode(3)
    n2 = TreeNode(2)
    n3 = TreeNode(1, left=n1, right=n2)
    n5 = TreeNode(5)
    n4 = TreeNode(4, left=n5, right=n3)
    t1 = Tree(n4)
    t2 = deepcopy(t1)
    #t.preOrder()
    #t.postOrder()
    #t.inOrder()
    #print t1.size()
    #print identical(t1.root, t2.root)
    #print t1.height()
    #t3 = Tree(mirror(t2.root))
    #t3.preOrder()
    #t2.preOrder();
    #r =  construct_tree([1,2,4,3],[2,1,4,3])
    #root_to_leaf_path(n4)
    t1.levelOrder()    
    #t = Tree(r)
    #t.inOrder()
    #t.preOrder()