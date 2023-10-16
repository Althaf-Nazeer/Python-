# Python program to show how to insert a value in the binary search tree  
  
# Creating a constructor class that will create the node object  
class Node:  
 # Defining the method to create a new node and the left and right pointers of this node.  
 def __init__(self, val):  
  self.val = val  
  self.left = None  
  self.right = None  
  
  
# Defining a function to insert the given value of x into the tree  
def insert(root, x):  
  # If the given tree is empty, we will return a node with the given value  
  if root is None:  
    return Node(x)  
  else:  
    # We will check if the value of the current node is equal to the value we want to insert  
    if root.val == x:  
      # If yes, then there is no need to modify the tree, and we will return the root node  
      return root  
    # If the value of x is greater than the value of the root node  
    elif root.val < x:  
      # We will insert the node in the right subtree  
      root.right = insert(root.right, x)  
    # If the value of x is smaller than the value of the root node  
    else:  
      # We will insert the node in the left subtree  
      root.left = insert(root.left, x)  
  return root  
  
  
# Creating a function to traverse the tree to check the final results  
def inorderTraversal(root):  
  if root:  
    inorderTraversal(root.left)  
    print(root.val, end = " ")  
    inorderTraversal(root.right)  
  
  
# Creating a binary search tree and inserting x in the tree  
root = Node(9)  
root.left = Node(1)  
root.right = Node(10)  
root.left.left = Node(0)  
root.left.right = Node(3)  
root.left.right.right = Node(4)  
print("The tree before insertion: ")  
inorderTraversal(root)  
print("\n")  
x = 5  
v = insert(root, x)  
print("The tree after insertion: ")  
inorderTraversal(v)  
