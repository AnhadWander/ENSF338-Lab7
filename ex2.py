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

        # Find the insertion point
        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        # Create and insert the new node
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
        # Track the inserted node's data for case identification
        inserted_data = node.data
        
        # Start with the parent of the inserted node
        current = node.parent
        pivot = None
        case_printed = False  # Flag to ensure only one case is printed
        
        # Update heights and balances going up from inserted node
        while current is not None:
            # Calculate heights
            left_height = current.left.height if current.left else 0
            right_height = current.right.height if current.right else 0
            
            # Update height and balance
            current.height = 1 + max(left_height, right_height)
            old_balance = current.balance
            current.balance = right_height - left_height
            
            # Check for pivot (node with balance factor of ±2)
            if pivot is None and abs(current.balance) >= 2:
                pivot = current
                
            current = current.parent
        
        # Handle cases based on pivot identification
        if pivot is None and not case_printed:
            print("Case #1: Pivot not detected")
            case_printed = True
        elif pivot is not None and not case_printed:
            # Determine if insertion was in shorter or taller subtree
            if self._is_in_shorter_subtree(pivot, inserted_data):
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
                case_printed = True
            else:
                print("Case 3 not supported")
                case_printed = True
    
    def _is_in_shorter_subtree(self, pivot, inserted_data):
        """Check if the inserted node is in the shorter subtree of the pivot"""
        # Determine which subtree is shorter
        left_height = pivot.left.height if pivot.left else 0
        right_height = pivot.right.height if pivot.right else 0
        
        # If right-heavy pivot (balance > 0), left is shorter
        if pivot.balance > 0:
            # Check if insertion was to left subtree
            return inserted_data < pivot.data
        # If left-heavy pivot (balance < 0), right is shorter
        else:
            # Check if insertion was to right subtree
            return inserted_data > pivot.data
    
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
    

def test_case_1():
    print("Test Case 1: No Pivot")
    print('-'*50)
    bst = BinarySearchTree()
    bst.insert(10)  # Root
    bst.insert(5)   # Left child
    bst.insert(15)  # Right child
    print("Expected output: Case #1: Pivot not detected")
    print()

def test_case_2():
    print("Test Case 2: Pivot exists, adding to shorter subtree (now corrected to Case #1)")
    print('-'*50)
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(80)
    bst.insert(90)  # Creates pivot at 70
    bst.insert(20)  # Corrects pivot, now no pivot exists
    print("Expected output: Case #1: Pivot not detected")
    print()

def test_case_3():
    print("Test Case 3: Case 3 - Adding to already taller subtree")
    print('-'*50)
    bst = BinarySearchTree()
    bst.insert(50)  # Root
    bst.insert(30)  # Left child
    bst.insert(70)  # Right child
    bst.insert(80)  # Right's right child
    bst.insert(90)  # Right's right's right child - creates right imbalance
    # At this point, pivot is root with balance +2, right is taller
    bst.insert(100) # Adding to taller (right) subtree
    print("Expected output: Case 3 not supported")
    print()

def test_case_4():
    print("Test Case 4: Left-heavy case 3")
    print('-'*50)
    bst = BinarySearchTree()
    bst.insert(50)  # Root
    bst.insert(30)  # Left child
    bst.insert(70)  # Right child
    bst.insert(20)  # Left's left child
    bst.insert(10)  # Left's left's left child - creates left imbalance
    # At this point, pivot is root with balance -2, left is taller
    bst.insert(5)   # Adding to taller (left) subtree
    print("Expected output: Case 3 not supported")
    print()

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()