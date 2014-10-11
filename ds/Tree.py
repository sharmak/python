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
    def _diameter(self, root):
        if root is None:
            return 0
        else:
            rh = self._height(root.right)
            lh = self._height(root.left)
            ld = self._diameter(root.left)
            rd = self._diameter(root.right)
            return  max(ld, rd, lh+rh+1)
    def diameter(self):
        return self._diameter(self.root)
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
    def _no_of_leaves(self, root):
        if root.left is None and root.right is None:
            return 1
        else:
            return self._no_of_leaves(root.left) + self._no_of_leaves(root.right)
    def no_of_leaves(self):
        return self._no_of_leaves(self.root)    
    def _is_bst(self, root, min, max):
        if root is None:
            return True
        elif root.node < min or root.node > max:
            return False
        else:
            return self._is_bst(root.left, min, root.node) and \
            self._is_bst(root.right, root.node, max)
    def is_bst(self):
        return self._is_bst(self.root, -9999, 9999)        
    def spiral(self):
        I = True
        l = list()
        l.append(self.root)
        while len(l) != 0:           
            if I:
                print [p.node for p in l]
            else:
                l.reverse()
                print [p.node for p in l]
                l.reverse()
            j = list()
            for n in l:
                if n.left is not None:
                    j.append(n.left)
                if n.right is not None:
                    j.append(n.right)
            
            l = j
            I = not I
    def _child_sum(self, root):
        if root is None:
            return True
        l = self._child_sum(root.left)
        r = self._child_sum(root.right)
        if root.left is None and root.right is not None:
            return root.node == root.right.node and l and r
        elif root.right is None and root.left is not None:
            return root.node == root.left.node and l and r
        elif root.left is not None and root.right is not None:
            return (root.node == root.left.node + root.right.node) and l and r
        else:
            return l and r
             
    def child_sum(self):
        return self._child_sum(self.root)
            
        
        
        
        
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
    node_list = list()
    for i in range(10):
        node_list.append(TreeNode(i))
    n1 = TreeNode(10)
    n2 = TreeNode(8)
    n3 = TreeNode(2)
    n5 = TreeNode(3)
    n4 = TreeNode(5)
    n6 = TreeNode(2)
    n7 = TreeNode(2)
    n2.left = n5
    n2.right = n4
    n6.left = n7
    n1.left = n2
    n1.right = n6    
    t1 = Tree(n1)
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
    #t1.levelOrder()    
    #print t1.no_of_leaves()
    #n6= TreeNode(4, right=n5, left=n3)
    #t3 = Tree(n6)
    #print t3.spiral()
    my_tree = Tree(node_list[0])
    node_list[0].left = node_list[1]
    node_list[0].right = node_list[2]
    node_list[1].left = node_list[3]
    node_list[1].right = node_list[4]
    node_list[2].left = node_list[5]
    node_list[2].right = node_list[6]
    node_list[3].left = node_list[8]
    node_list[4].left = node_list[9]
    #my_tree.spiral()
    print my_tree.child_sum() 
    print t1.child_sum()
    print t1.diameter()
    #t = Tree(r)
    #t.inOrder()
    #t.preOrder()