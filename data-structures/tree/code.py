class User:
  def __init__(self, first_name, last_name, username):
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.email = first_name.lower() + last_name.lower() + "@dquit.com"
    
  def __str__(self):
    return f'User({self.first_name}, {self.last_name}, {self.email})'
    
  def introduce_yourself(self):
    print(f"Hi! I am {self.username} and my email id is {self.email}")
    
class BSTNode:
  """
  Implementing the user database using BST
  """
  def __init__(self, key, value):
    self.key = key  # Stores username
    self.value = value  # Stores User class object
    self.parent = None 
    self.left = None 
    self.right = None  
    
  def height(self):
    if (self is None):
      return 0
    return 1 + max(BSTNode.height(self.left), BSTNode.height(self.right))
  
  def size(self):
    if (self is None):
      return 0
    return 1 + BSTNode.size(self.left) + BSTNode.size(self.right)
  
  def traverse_in_order(self):
    if (self is None):
      return []
    return BSTNode.traverse_in_order(self.left) + [(self.key, self.value)] + BSTNode.traverse_in_order(self.right)
  
  @staticmethod
  def insert(self, key, value):
    if (self is None):
      self = BSTNode(key, value)
    elif (key < self.key):
      self.left =   BSTNode .insert(self.left, key, value)
      self.left.parent = self
    elif (key > self.key):
      self.right =  BSTNode .insert(self.right, key, value)
      self.right.parent = self
    return self

  @staticmethod
  def find(self, key):
    if (self is None):
      return None
    if (key < self.key):
      return BSTNode.find(self.left, key)
    if (key > self.key):
      return BSTNode.find(self.right, key) 
    if (key == self.key):
      return self
  
  @staticmethod
  def update(self, key, value):
    target = BSTNode.find(self, key)
    
    if (target is not None):
      target.value = value
    else: 
      print('This profile does not exist in the DB')
      
  @staticmethod
  def list_all(self):
    if (self is None):
      return []
    return BSTNode.list_all(self.left) + [(self.key, self.value)] + BSTNode.list_all(self.right)
  
  @staticmethod
  def is_balanced_bst(self):
    """
    This method will check if a given binary search tree is balanced
    and it will also return the associated tree height.
    """
    if (self is None):
      return True, 0
    is_balanced_bst_left, height_left = BSTNode.is_balanced_bst(self.left)
    is_balanced_bst_right, height_right = BSTNode.is_balanced_bst(self.right)
    
    is_balanced_bst = is_balanced_bst_left and is_balanced_bst_right and (abs(height_left-height_right) <= 1)
    height = 1 + max(height_left, height_right)
    return is_balanced_bst, height
  
  @staticmethod
  def create_balanced_bst(data, start_index=0, end_index=None, parent=None):
    """
    This method will take any sorted array of key-value pairs and will
    create a balanced BST out of it.
    """
    if (end_index == None):
      end_index = len(data)-1
      
    if (start_index > end_index):
      return None
    
    middle_index = (start_index+end_index) // 2
    key, value = data[middle_index]
    
    root = BSTNode(key, value)
    root.parent = parent
    root.left = BSTNode.create_balanced_bst(data, start_index, middle_index-1, root)
    root.right = BSTNode.create_balanced_bst(data, middle_index+1, end_index, parent=root)
    return root
  
aakash = User('Aakash', 'Rai', 'aakash',)
biraj = User('Biraj', 'Das', 'biraj')
jadhesh = User('Jadhesh', 'Verma', 'jadhesh')
hemanth = User('Hemanth', 'Jain', 'hemanth')
siddhant = User('Siddhant', 'Sinha', 'siddhant')
sonaksh = User('Sonaksh', 'Kumar', 'sonaksh')
vishal = User('Vishal', 'Goel', 'vishal')

tree = BSTNode.insert(None, aakash.username, aakash)
tree = BSTNode.insert(tree, biraj.username, biraj)
tree = BSTNode.insert(tree, jadhesh.username, jadhesh)
tree = BSTNode.insert(tree, hemanth.username, hemanth)
tree = BSTNode.insert(tree, siddhant.username, siddhant)
tree = BSTNode.insert(tree, sonaksh.username, sonaksh)
vishal = BSTNode.insert(tree, vishal.username, vishal)

print(tree.traverse_in_order())
print(tree.is_balanced_bst(tree))
print(f"All profiles: {tree.list_all(tree)}")


# Create a balanced birary search tree from the above right skewed BST
print(tree.is_balanced_bst(tree))  # Proof that thus BST is not balanced
sorted_tree = tree.traverse_in_order()  # Proof it's righ skewed: They will be in sorted manner
print(sorted_tree)


balanced_bst = BSTNode.create_balanced_bst(sorted_tree)
print(balanced_bst)   # We should now get a balanced BST
print(BSTNode.is_balanced_bst(balanced_bst))  # For confirmation

