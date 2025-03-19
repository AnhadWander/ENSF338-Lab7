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
        while current is not None:
            left_height = current.left.height if current.left else 0
            right_height = current.right.height if current.right else 0
            
            current.height = 1 + max(left_height, right_height)
            current.balance = right_height - left_height
            
            current = current.parent
    
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


def run_experiment(num_tasks=200):  
    integers = list(range(1, 1001))
    
    results = []
    
    for i in range(num_tasks):
        bst = BinarySearchTree()
        
        shuffled_integers = integers.copy()
        random.shuffle(shuffled_integers)
        
        for num in shuffled_integers:
            bst.insert(num)
        
        sample_integers = random.sample(integers, 100)
        
        start_time = time.time()
        for num in sample_integers:
            bst.search(num)
        end_time = time.time()
        
        avg_search_time = (end_time - start_time) / len(sample_integers)
        
        max_abs_balance = bst.get_max_abs_balance()
        
        results.append((max_abs_balance, avg_search_time))
    
    return results


def plot_results(results):
    balances, times = zip(*results)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(balances, times, alpha=0.5)
    plt.title('BST Search Performance vs Balance')
    plt.xlabel('Maximum Absolute Balance')
    plt.ylabel('Average Search Time (seconds)')
    plt.ylim(0.5e-6, 1.0e-6)  
    plt.grid(True)
    
    z = np.polyfit(balances, times, 1)
    p = np.poly1d(z)
    plt.plot(balances, p(balances), "r--", linewidth=2)

    plt.show()


if __name__ == "__main__":
    results = run_experiment()
    plot_results(results)
