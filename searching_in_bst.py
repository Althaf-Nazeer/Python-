# Python program to implement search operation in the binary search tree  
  
# Creating a constructor class that will create the node object  
class Node:  
 # Defining the method to create a new node and the left and right pointers of this node.  
 def __init__(self, val):  
  self.val = val  
  self.left = None  
  self.right = None  
  
# Defining a function that will search the given value of x in the tree  
def search(root, x):  
    
  # The base conditions are  
  # If the given root is a Null Node  
  # Or if the value we are searching for is present at the root only  
  if root is None or root.val == x:  
    return root.val  
  
  # If the value of x is greater than the value of the root node  
  if root.val < x:  
    # We will search in the right subtree  
    return search(root.right, x)  
  
  # If the value of x is smaller than the value of the root node  
  # We will search in the left subtree  
  return search(root.left, x)  
  
# Creating a binary search tree and searching for x in the tree  
root = Node(9)  
root.left = Node(1)  
root.right = Node(10)  
root.left.left = Node(0)  
root.left.right = Node(3)  
root.left.right.right = Node(4)  
x = 4  
v = search(root, x)  
print("The node we are searching for is present in the given BST: ", v)  
