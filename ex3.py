import sys


sys.setrecursionlimit(3000)

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.balance = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """Insert a new key into the BST and rebalance if necessary"""
        new_node = TreeNode(key)
        
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if key <= current.key:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
        
        pivot = self.find_pivot(new_node)
        
        if pivot is None:
            print("Case #1: Pivot not detected")
            
        elif pivot.balance >= 1:
            if new_node.key <= pivot.key:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                if new_node.key > pivot.right.key:
                    print("Case #3a: adding a node to an outside subtree")
                    self._left_rotate(pivot)
                else:
                    print("Case 3b not supported")
        
        elif pivot.balance <= -1:
            if new_node.key > pivot.key:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                if new_node.key < pivot.left.key:
                    print("Case #3a: adding a node to an outside subtree")
                    self._right_rotate(pivot)
                else:
                    print("Case 3b not supported")
        
        self.calculate_balance()
    
    def find_pivot(self, new_node):
        """Find the pivot (deepest imbalanced ancestor)"""
        current = self.root
        pivot = None
        
        while current is not new_node:
            if abs(current.balance) >= 1:
                pivot = current  # Last imbalanced node
            if new_node.key <= current.key:
                current = current.left
            else:
                current = current.right
        
        return pivot
    
    def _left_rotate(self, pivot):
        """Left rotation around pivot"""
        son = pivot.right
        if son is None:
            return
        
        pivot.right = son.left
        son.left = pivot
        
        # Update parent link
        if pivot is self.root:
            self.root = son
        else:
            ancestor = self.find_ancestor(pivot)
            if ancestor.left == pivot:
                ancestor.left = son
            else:
                ancestor.right = son
        
        self.calculate_balance()

    def _right_rotate(self, pivot):
        """Right rotation around pivot"""
        son = pivot.left
        if son is None:
            return
        
        pivot.left = son.right
        son.right = pivot
        
        # Update parent link
        if pivot is self.root:
            self.root = son
        else:
            ancestor = self.find_ancestor(pivot)
            if ancestor.left == pivot:
                ancestor.left = son
            else:
                ancestor.right = son
        
        self.calculate_balance()
    
    def find_ancestor(self, pivot):
        """Find parent of a given node"""
        current = self.root
        ancestor = None
        
        while current is not pivot:
            ancestor = current
            if pivot.key < current.key:
                current = current.left
            else:
                current = current.right
        
        return ancestor
    
    def calculate_balance(self):
        """Calculate balance factor for each node"""
        if self.root is None:
            return {}
        
        balance_dict = {}
        self._calculate_heights_and_balance(self.root, balance_dict)
        return balance_dict
    
    def _calculate_heights_and_balance(self, node, balance_dict):
        """Calculate height and balance factor for each node"""
        if node is None:
            return 0
        
        left_height = self._calculate_heights_and_balance(node.left, balance_dict)
        right_height = self._calculate_heights_and_balance(node.right, balance_dict)
        
        balance = right_height - left_height
        node.balance = balance
        balance_dict[node.key] = balance
        
        return max(left_height, right_height) + 1

def main():
    # Test cases
    tree = BinarySearchTree()
    tree.insert(12)  # Root node
    tree.insert(6)   # Should return case 1 (No imbalance)
    tree.insert(17)  # Should return case 2 (No imbalance
    tree.insert(8)   # Should return case 1 (No imbalance)
    tree.insert(10)  # Should return case 3a (Causes Rotation)
    tree.insert(11)  # Should return case 3b

if __name__ == "__main__":
    main()
