# -*- coding: utf-8 -*-
"""
Created on Fri Oct 03 23:35:26 2014

@author: admin
"""

class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.connectedTo = dict()
    def addNeighbour(self, v,  cost):
        self.connectedTo[v] = cost
    def getVertex(self):
        return self.key
    def connetions(self):
        return self.connectedTo
    def getWeight(self, v):
        return self.connectedTo[v]
    def __str__(self):
        return  str(self.key) + " Connected to " + \
                str([str(i.key) + " with wt " +  \
                str(self.connectedTo[i])  \
                for i in self.connectedTo.keys()])
class Graph(object): 
    def __init__(self):
        self.vertices = dict()
        self.number_of_vert = 0
    def addVertex(self, key):
        self.vertices[key] = Vertex(key)
        self.number_of_vert = self.number_of_vert + 1
    def addEdge(self, key1, key2, wt):
        self.vertices[key1].addNeighbour(self.vertices[key2], wt)
    def getVertices(self):
        return self.vertices
def prim_mst(G):
    V = G.getVertices()
    MST = Graph()
    firstVertex = V.pop(V.keys()[0])
    MST.addVertex(firstVertex.key)
    # Choose first vertex
    while (len(V) > 0):         
        min_cost = 10000
        for adj in firstVertex.connectedTo.keys():
            cost = firstVertex.connectedTo[adj]
            if cost < min_cost:
                min_cost = cost
                min_vertex = adj
        MST.addVertex(min_vertex.key)
        MST.addEdge(firstVertex.key, min_vertex.key, min_cost)
        V.pop(min_vertex.key)
        firstVertex = min_vertex
    return MST
if __name__ == '__main__':
    g = Graph()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    g.addEdge(1,2,5)
    g.addEdge(1,4,8)
    g.addEdge(2,3,3)
    g.addEdge(4,1,8)
    g.addEdge(3,4,2)
    MST = prim_mst(g)
    for v, c in MST.getVertices().iteritems():
        print v, c
    
    