from collections import deque

class BTNode:
  def __init__(self, key):
    self.key = key 
    self.left = None 
    self.right = None 
    
  def __str__(self):
    return f"BTNode({self.key}, {self.left}, {self.right})"
  
  @staticmethod 
  def parse_list(data):
    if (not data or data[0] is None):
      return None 
    
    node = BTNode(data[0])
    queue = deque([node])
    i = 1 
    
    while (i<len(data)):
      current = queue.popleft()
      
      # Add left child 
      if (i<len(data) and data[i] != None):
        current.left = BTNode(data[i])
        queue.append(current.left)
        
      i +=1 
      
      # Add right child 
      if (i<len(data) and data[i] != None):
        current.right = BTNode(data[i])
        queue.append(current.right)
        
      i += 1
    return node 
  
  def traverse_post_order(self):
    if self is None:
      return []
    
    return BTNode.traverse_post_order(self.left) + BTNode.traverse_post_order(self.right) + [self.key]


test_cases = [
  {
    'input': {
      'data': [1,None,2,3]
    },
    'output': [3,2,1]
  },
    {
    'input': {
      'data':[1,2,3,4,5,None,8,None,None,6,7,9]
    },
    'output': [4,6,7,5,2,9,8,3,1]
  },
      {
    'input': {
      'data': []
    },
    'output': []
  },
  {
    'input': {
      'data': [1]
    },
    'output': [1]
  },
  {
    'input': {
      'data': [None]
    },
    'output': []
  }
]

def evaluate_test_cases(test_cases):
  print('EVALUATION OF TESTS')
  for i in range(len(test_cases)):
    actual_value = BTNode.traverse_post_order(BTNode.parse_list(**test_cases[i]['input']))
    expected_value = test_cases[i]['output']
    
    success = 'TEST PASSED!' if actual_value == expected_value else 'TEST FAILED!'
    print(f"TEST CASE #{i+1}: {success}")
    
evaluate_test_cases(test_cases)