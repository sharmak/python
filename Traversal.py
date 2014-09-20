# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 09:40:08 2014

@author: kishor
"""

class GraphNode(object):
    def __init__(self, value, links=None):
        self.value = value
        self.links = links
    def __str__(self):
        return str(self.value)

class Link(object):
    def __init(self, g1, g2, wt):
        self.start = g1
        self.end   = g2
        self.wt    = wt        
class Graph(object):
    def __init__(self, root):
        self.root = root
    def _dfs(cls, root):
        if root is not None:
            print root
            if root.links is  not None:
                for link in root.links:
                    cls._dfs(link)
    def dfs(self):
        self._dfs(self.root)
    def _bfs(cls, root):
        q = list()
        if root is not None:
            q.append(root)
        while len(q) != 0:
            ele = q.pop(0)
            print ele
            if ele.links is not None:
                for l in ele.links:
                    q.append(l)
            
    def bfs(self):
        self._bfs(self.root)
        
if __name__ == '__main__':
    # 5->6 ->9
    #  ->7 ->10
    #  ->8        
    g1 = GraphNode(5)
    g2 = GraphNode(6)
    g3 = GraphNode(7)
    g4 = GraphNode(8)
    g5 = GraphNode(9) 
    g6 = GraphNode(10)
    g1.links = [g2, g3, g4]
    g2.links = [g5]
    g3.links = [g6]
    #print g.value
    gr = Graph(g1)
    gr.dfs()
    gr.bfs()
    
    