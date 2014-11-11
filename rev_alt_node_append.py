# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 07:17:38 2014

@author: kishor
"""

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next  = next
class LinkedList(object):
    def __init__(self, head):
        if isinstance(head, Node):        
            self.head = head
        else:
            head = Node(head)
            self.head = head
    def Append(self, value):
        curPtr = self.head
        while curPtr.next is not None:
            curPtr = curPtr.next
        newNode = Node(value)
        curPtr.next = newNode
    def Print(self):
        curPtr = self.head
        while curPtr is not None:
            print curPtr.value
            curPtr = curPtr.next
    def _Rev(self, head):
        if head.next is None:
            self.head = head
        else:
            self._Rev(head.next)
            head.next.next = head
            head.next = None
    def Rev(self):
        self._Rev(self.head)
        
    @staticmethod
    def Split(L):
        OP = L.head
        EP = L.head.next
        O = OP
        E = EP
        while EP is not None:
            OP.next = EP.next
            OP = EP
            EP = EP.next
        return LinkedList(O), LinkedList(E)

    @staticmethod
    def Concat(L1, L2):
        L1H = L1.head
        while L1H.next is not None:
            L1H = L1H.next
        L1H.next = L2.head
        return L1        
            
if __name__ == '__main__':
    L = LinkedList(1)
    L.Append(2)
    L.Append(3)
    L.Append(4)
    L.Append(5)
    L.Append(6)
    #L.Print()
    #L.Rev()
    #L.Print()
    O, E = LinkedList.Split(L)
    #O.Print()
    E.Rev()
    #E.Print()
    LinkedList.Concat(O, E).Print()