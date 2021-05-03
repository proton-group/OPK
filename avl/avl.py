from autotest import tester
class Node:
    def __init__(self):
        self.balance = 0
        self.left = ""
        self.right = ""
        self.value = 0
        self.ancestor = ""
        self.height = 0

class avl:
    def __init__(self):
        self.root = Node()
        self.check = True
        self.node_ctr = 1
        self.height = 0
    
    def small_rot(self, n, direction):
        if direction == "left":
            if n.ancestor != "":
                if n == n.ancestor.left:
                    n.ancestor.left = n.left
                else:
                    n.ancestor.right = n.left
            n.left.right = n
            
        if direction == "right":
            if n.ancestor != "":
                if n == n.ancestor.left:
                    n.ancestor.left = n.right
                else:
                    n.ancestor.right = n.right
            n.right.left = n

    
    def big_rot(self, n, direction):
        if direction == "right":
            if n.ancestor != "":
                if n == n.ancestor.left:
                    n.ancestor.left = n.right.left
                else:
                    n.ancestor.right = n.right.left
            left_buf = n.right.left
            n.right.left.right, n.right.left = n.right, n.right.left.right
            left_buf.left, n.right = n, left_buf.left

        if direction == "left":
            if n.ancestor.ancestor != "":
                if n == n.ancestor.left:
                    n.ancestor.left = n.left.right
                else:
                    n.ancestor.right = n.left.right
            right_buf = n.left.right
            n.left.right.left, n.left.right = n.left, n.left.right.left
            right_buf.right, n.left = n, right_buf.right
            
    def setheight(self, n):
        height_l = 0
        height_r = 0
        if n.left != "":
            height_l += 1
            self.setheight(n.left)
        if n.right != "":
            height_r += 1
            self.setheight(n.right)
        self.height = max(height_l, height_r) + 1
        
    
    def balancer(self, n):
        height_left = 0
        height_right = 0
        if n != "":
            if n.left != "":
                self.setheight(n.left)
                height_left = self.height
            if n.right != "":
                self.setheight(n.right)
                height_right = self.height
            #if n.left != "":
            #   height_left = n.left.height - n.height
            #if n.right != "":
            #    height_right = n.right.height - n.height
            n.balance = height_right - height_left
            if n.balance > -2 and n.balance < 2:
                self.balancer(n.ancestor)
            else:
                if n.left != "":
                    if n.balance < -1 and n.left.balance <= 0:
                        self.small_rot(n, "left")
                    if n.balance < -1 and n.left.balance > 0:
                        self.big_rot(n, "left")
                if n.right != "":
                    if n.balance > 1 and n.right.balance >= 0:
                        self.small_rot(n, "right")
                    if n.balance > 1 and n.right.balance < 0:
                        self.big_rot(n, "right")
              

    def insert(self, data):
        if self.check:
            self.root.value = data
            self.check = False
        else:
            self.insert_r(data, self.root) 

    def insert_r(self, data, n):
        if n.value > data:
            if n.left != "":
                self.insert_r(data, n.left)
            else:
                n.left = Node()
                self.node_ctr += 1
                n.left.value = data  
                n.left.ancestor = n 
                self.balancer(n.left)
        if n.value < data:
            if n.right != "":
                self.insert_r(data, n.right)
            else:
                n.right = Node()
                self.node_ctr += 1
                n.right.value = data
                n.right.ancestor = n
                self.balancer(n.right)
                
    def search(self,data):
        return self.search_r(data, self.root)
    def search_r(self, data, n):
        if n.value > data:
            if n.left != "":
                self.search_r(data, n.left)
            else:
                return False
        if n.value < data:
            if n.right != "":
                self.search_r(data, n.right)
            else:
                return False
        return n        
    
    def clear(self):
        self.root = Node()
        self.node_ctr = 0
        self.check = True
        
    def get_size(self):
        return self.node_ctr
    
    def foreach(self, fun):
        self.foreach_r(fun, self.root)
    
    def foreach_r(self, fun, n): #LNR           
        if n.left != "":
            self.foreach_r(fun, n.left)
        fun(n) 
        if n.right != "":
            self.foreach_r(fun, n.right)

tester(avl)