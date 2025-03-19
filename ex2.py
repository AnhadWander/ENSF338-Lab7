import time
import random
import matplotlib.pyplot as plt
import numpy as np


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.balance = 0  
        self.height = 1   

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        current = self.root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        newnode = Node(data, parent)    
        if self.root is None:
            self.root = newnode
        elif data <= parent.data:
            parent.left = newnode
        else:
            parent.right = newnode
            
        self._update_balance_after_insert(newnode)
        
        return newnode
    
    def _update_balance_after_insert(self, node):
        current = node.parent
        pivot = None

        while current is not None:
            left_height = current.left.height if current.left else 0
            right_height = current.right.height if current.right else 0
            
            current.height = 1 + max(left_height, right_height)
            current.balance = right_height - left_height
            
            if abs(current.balance) > 1:
                pivot = current  # First imbalanced node
                break
            
            current = current.parent

        if pivot is None:
            print("Case #1: Pivot not detected")
        else:
            self._identify_case(pivot, node)

    def _identify_case(self, pivot, inserted_node):
        left_height = pivot.left.height if pivot.left else 0
        right_height = pivot.right.height if pivot.right else 0
        inserted_subtree = pivot.left if inserted_node.data < pivot.data else pivot.right

        # Case #2: Inserted node in the shorter subtree
        if ((left_height < right_height and inserted_subtree == pivot.left) or 
            (right_height < left_height and inserted_subtree == pivot.right)):
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            return
        
        # Case #3: Inserted node in the taller subtree
        if ((left_height > right_height and inserted_subtree == pivot.left) or 
            (right_height > left_height and inserted_subtree == pivot.right)):
            print("Case #3: A pivot exists, and a node was added to the taller subtree")
            return
    
    def search(self, data):
        current = self.root
        
        while current is not None:
            if current.data == data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
                
        return False
    
    def get_max_abs_balance(self):
        return self._get_max_abs_balance_recursive(self.root, 0)
    
    def _get_max_abs_balance_recursive(self, node, current_max):
        if node is None:
            return current_max
        
        abs_balance = abs(node.balance)
        if abs_balance > current_max:
            current_max = abs_balance
        
        left_max = self._get_max_abs_balance_recursive(node.left, current_max)
        right_max = self._get_max_abs_balance_recursive(node.right, current_max)
        
        return max(current_max, left_max, right_max)
    

def test_case_1():
    print("Test Case 1")
    print('-'*50)
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    print("Expected output: Case #1: Pivot not detected")
    print()

def test_case_2():
    print("Test Case 2")
    print('-'*50)
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(4)
    print("Expected output: Case #2: A pivot exists, and a node was added to the shorter subtree")
    print()

def test_case_3():
    print("Test Case 3")
    print('-'*50)
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(8)
    print("Expected output: Case #3: A pivot exists, and a node was added to the taller subtree")
    print()

def test_case_4():
    print("Test Case 4")
    print('-'*50)
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    print("Expected output: Case #3: A pivot exists, and a node was added to the taller subtree")
    print()

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()

