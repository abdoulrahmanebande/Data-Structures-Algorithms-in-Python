class TreeNode:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    
  def height(self):
    """
    Largest path from the root node to its leaf node.
    """
    if (self is None):
      return 0
    return 1+max(TreeNode.height(self.left), TreeNode.height(self.right))
  
  def size(self):
    """
    Total number of nodes in a tree.
    """
    if (self is None):
      return 0
    return 1+TreeNode.size(self.left)+TreeNode.size(self.right)
  
  def traverse_in_order(self):
    if (self is None):
      return []
    return (TreeNode.traverse_in_order(self.left)+[self.key]+TreeNode.traverse_in_order(self.right))
  
  def traverse_pre_order(self):
    if (self is None):
      return []
    return ([self.key]+TreeNode.traverse_in_order(self.left)+TreeNode.traverse_in_order(self.right))
  
  def traverse_post_order(self):
    if (self is None):
      return []
    return (TreeNode.traverse_in_order(self.left)+TreeNode.traverse_in_order(self.right)+[self.key])
  
  def to_tuple(self):
    """
    Parsing a given tree to a tuple.
    """
    if (self is None):
      return None
    elif (self.left is None and self.right == None):
      return self.key
    return (TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right))
  
  @staticmethod
  def parse_tuple(data):
    """
    Parsing a given tuple to a tree.
    """
    if (isinstance(data, tuple) and len(data) == 3):
      node = TreeNode(data[1])
      node.left = TreeNode.parse_tuple(data[0])
      node.right = TreeNode.parse_tuple(data[2])
    elif (data is None):
      node = None 
    else:
      node = TreeNode(data)
    return node
  
  def remove_none(nums):
    return [x for x in nums if x is not None]
  
  def is_bst(self):
    """
    This method checks if a given binary tree is a BST and it
    returns the minimum and maximum value of the binary tree
    """
    if (self is None):
      return True, None, None 
    
    is_bst_left, min_left, max_left = TreeNode.is_bst(self.left)
    is_bst_right, min_right, max_right = TreeNode.is_bst(self.right)
    
    is_bst = (is_bst_left and is_bst_right 
        and (max_left is None or max_left < self.key)
        and (min_right is None or self.key < min_right)
        )
    min_key = min(TreeNode.remove_none([min_left, self.key, max_left]))
    max_key = max(TreeNode.remove_none([min_right, self.key, max_right]))
    
    return is_bst, min_key, max_key
      
tree = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(tree.size())
print(tree.height())
print(tree.traverse_in_order())
print(tree.traverse_post_order())
print(tree.traverse_pre_order())
print(tree.to_tuple())
print(tree.is_bst())


tree2 = TreeNode.parse_tuple((('Aakash', 'Biraj', 'Hemanth'), 'Jadhesh', ('Siddhant', 'Sonaksh', 'Vishal')))
print(tree2.size())
print(tree2.height())
print(tree2.traverse_in_order())
print(tree2.traverse_post_order())
print(tree2.traverse_pre_order())
print(tree2.to_tuple())
print(tree2.is_bst())