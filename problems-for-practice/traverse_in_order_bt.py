from collections import deque
class BTNode:
  def __init__(self, key):
    self.key = key 
    self.left = None 
    self.right = None 
    
  def __str__(self):
    return f"BTNode({self.key}, {self.left}, {self.right})"
  
  @staticmethod
  def parse_list(root):
    # The root variable here refers to the list of numbers
    if (not root or root[0] is None):
      return None 
    
    node = BTNode(root[0]) 
    queue = deque([node])
    i = 1
    
    while (queue and i < len(root)):
      current = queue.popleft()
      
      # Add left child 
      if (i<len(root) and root[i] != None):
        current.left = BTNode(root[i])
        queue.append(current.left)
      i +=1 
      
      # Add right child
      if (i<len(root) and root[i] != None):
        current.right = BTNode(root[i])
        queue.append(current.right)
      i += 1 
      
    return node
  
  @staticmethod
  def traverse_in_order(self):
    if self is None:
      return []
    
    return BTNode.traverse_in_order(self.left) + [self.key] + BTNode.traverse_in_order(self.right)
        

test_cases = [
  {
    'input': {
      'root': [1,None,2,3]
    },
    'output': [1,3,2]
  },
    {
    'input': {
      'root':[1,2,3,4,5,None,8,None,None,6,7,9]
    },
    'output': [4,2,6,5,7,1,3,9,8]
  },
      {
    'input': {
      'root': []
    },
    'output': []
  },
  {
    'input': {
      'root': [1]
    },
    'output': [1]
  },
  {
    'input': {
      'root': [None]
    },
    'output': []
  }
]

def evaluate_test_cases(test_cases):
  print('EVALUATION OF TESTS')
  for i in range(len(test_cases)):
    actual_value = BTNode.traverse_in_order(BTNode.parse_list(**test_cases[i]['input']))
    expected_value = test_cases[i]['output']
    
    success = 'TEST PASSED!' if actual_value == expected_value else 'TEST FAILED!'
    print(f"TEST CASE #{i+1}: {success}")
    
evaluate_test_cases(test_cases)

