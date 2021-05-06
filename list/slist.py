from test import tester
import warnings
class Node:
    def __init__(self):
        self.next = None
        self.past = None
        self.data = None

class Slist:
    def __init__(self):
        self.base = Node()
    def append(self, data):
        def append_r(dat, n):
            if n.next != None:
                append_r(data, n.next)
            else:
                n.next = Node()
                n.next.data = dat
                n.next.past = n
        if self.base.data == None:
            self.base.data = data
        else:        
            append_r(data, self.base)
        
    def prepend(self, data):
        def prepend_r(dat, n):
            if n.past != None:
                prepend_r(data, n.past)
            else:
                n.past = Node()
                n.past.next = n
                n.past.data = dat
                self.base = n.past
        prepend_r(data, self.base)

    def append_from_key(self, key, data): #insert between
        n = self.base
        if type(key) is int:
            for i in range(key):
                if n.next != None:
                    n = n.next
                else:
                    return "array out of bounds" 
        else:
            warnings.warn("expected int", Warning)
        new = Node()
        new.data = data
        new.next = n
        if n.past != None:
            n.past.next = new
        else:
            self.base = new
        new.past = n.past
        n.past = new

    def get(self,key):
        n = self.base
        if type(key) is int:
            for i in range(key):
                if n.next != None:
                    n = n.next
                else:
                    return "array out of bounds"
        else:
            warnings.warn("expected int", Warning)
        return n.data

    def length(self):
        n = self.base
        count = 0
        while(1):
            if n != None:
                n = n.next
                count += 1
            else:
                return count
    def remove(self, key):
        n = self.base
        if type(key) is int:
            for i in range(key):
                if n.next != None:
                    n = n.next
                else:
                    return "array out of bounds"
        else:
            warnings.warn("expected int", Warning)
        if n.next != None:
            n.next.past = n.past
        if n.past != None:
            n.past.next = n.next
        if self.base == n:
            self.base = n.next
    
    def concat(self, lst2):
        n = self.base
        while(1):
            if n.next != None:
                n = n.next
            else:
                n.next = lst2.base
                break

    def copy(self):
        return self.base
    
    def remove_all(self):
        self.base = Node()

tester(Slist)