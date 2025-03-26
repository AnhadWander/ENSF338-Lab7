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
            print(f"Case #1: Pivot not detected for {key}")
        
        elif pivot.balance >= 1:
            if new_node.key <= pivot.key:
                print(f"Case #2: A pivot exists, and a node was added to the shorter subtree for {key}")
            else:
                if new_node.key > pivot.right.key:
                    print(f"Case #3a: adding a node to an outside subtree for {key}")
                    self._left_rotate(pivot)
                else:
                    print(f"Case #3b: performing RL rotation for {key}")
                    self._rl_rotate(pivot)
        
        elif pivot.balance <= -1:
            if new_node.key > pivot.key:
                print(f"Case #2: A pivot exists, and a node was added to the shorter subtree for {key}")
            else:
                if new_node.key < pivot.left.key:
                    print(f"Case #3a: adding a node to an outside subtree for {key}")
                    self._right_rotate(pivot)
                else:
                    print(f"Case #3b: performing LR rotation for {key}")
                    self._lr_rotate(pivot)
        
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
        
        if pivot is self.root:
            self.root = son
        else:
            ancestor = self.find_ancestor(pivot)
            if ancestor.left == pivot:
                ancestor.left = son
            else:
                ancestor.right = son
        
        self.calculate_balance()
    
    def _lr_rotate(self, pivot):
        """Left-Right rotation (LR)"""
        self._left_rotate(pivot.left)
        self._right_rotate(pivot)
    
    def _rl_rotate(self, pivot):
        """Right-Left rotation (RL)"""
        self._right_rotate(pivot.right)
        self._left_rotate(pivot)
    
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
    # Example test array of small numbers
    test_numbers = [15, 25, 10, 5, 1, 12, 20, 30, 8, 18]

    tree = BinarySearchTree()
    
    for num in test_numbers:
        print(f"Inserting {num}")
        tree.insert(num)
    
if __name__ == "__main__":
    main()
