from collections import deque
class BTreeNode:
  def __init__(self, key):
    self.key = key 
    self.left = None
    self.right = None
    
  def __str__(self):
    return f"BTreeNode({self.key}, children({self.left}, {self.right}))"
  
  @staticmethod
  def parse_list(data):
    node = BTreeNode(data[0])
    queue = deque([node])
    
    i = 1 
    while (i < len(data) and queue):  # queue is not empty check
      current = queue.popleft()
      
      # Adding left child
      if (i < len(data) and data[i] != None):
        current.left = BTreeNode(data[i])
        queue.append(current.left)
      i += 1
      
      # Adding right child
      if (i < len(data) and data[i] != None):
        current.right = BTreeNode(data[i])
        queue.append(current.right)
      i += 1
    return node
  
  # def height(self):
  #   if self is None:
  #     return 0 
  #   return 1 + max(BTreeNode.height(self.left), BTreeNode.height(self.right)) 
  
  def diameter(self): #Optmized code
    if self is None:
      return 0, 0 # diameter and height
    
    left_diameter, left_height = BTreeNode.diameter(self.left)
    right_diameter, right_height = BTreeNode.diameter(self.right)
    
    current_height = 1 + max(left_height, right_height)
    current_diameter = max(left_height+right_height, left_diameter, right_diameter)
    
    return current_diameter, current_height
  
  # def diameter(self):
  #   if self is None:
  #     return 0 
  #   left_height = BTreeNode.height(self.left) 
  #   right_height = BTreeNode.height(self.right) 
    
  #   left_diameter =  BTreeNode.diameter(self.left)
  #   right_diameter = BTreeNode.diameter(self.right) 
    
  #   return max(left_height+right_height, left_diameter, right_diameter)
  #   # The longest path that must pass through the current node. 
  #   # left_diameter: The longest path that stays entirely inside the left subtree.

test_cases = [
    {
    'input': {
      'data': [3,1,None,None,2]
    },
    'output': 2
  },
  {
    'input': {
      'data': [1,2,3,4,5]
    },
    'output': 3
  },
  {
    'input': {
      'data': [1,2]
    },
    'output': 1
  },
   {
    'input': {
      'data': [1]
    },
    'output': 0
  },
]

def evaluate_test_cases(test_cases):
  print('EVALUATION OF TESTS')
  for i in range(len(test_cases)):
    actual_value = BTreeNode.diameter(BTreeNode.parse_list(**test_cases[i]['input']))[0]
    expected_value = test_cases[i]['output'] 
    
    success = 'TEST PASSED!' if actual_value == expected_value else 'TEST FAILED!'
    print(f"TEST CASE #{i+1}: {success}")
    
evaluate_test_cases(test_cases)