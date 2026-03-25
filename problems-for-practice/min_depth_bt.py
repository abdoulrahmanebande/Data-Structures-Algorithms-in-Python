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
  
  def min_depth(self):
    if self is None:
      return 0
    
    if self.left is None and self.right is None:
      return 1 
    
    if self.left is None:
      return 1 + BTreeNode.min_depth(self.right)
    
    if self.right is None:
      return 1 + BTreeNode.min_depth(self.left)
    
    return 1 + min(BTreeNode.min_depth(self.left), BTreeNode.min_depth(self.right))

test_cases = [
  {
    'input': {
      'data': [3,9,20,None,None,15,7]
    },
    'output': 2
  },
  {
    'input': {
      'data': [2,None,3,None,4,None,5,None,6]
    },
    'output': 5
  },
  {
    'input': {
      'data': [1,None,2]
    },
    'output': 2
  },
  {
    'input': {
      'data': [1]
    },
    'output': 1
  },
]

def evaluate_test_cases(test_cases):
  print('EVALUATION OF TESTS')
  for i in range(len(test_cases)):
    actual_value = BTreeNode.min_depth(BTreeNode.parse_list(**test_cases[i]['input']))
    expected_value = test_cases[i]['output']
    
    success = 'TEST PASSED!' if actual_value == expected_value else 'TEST FAILED!'
    print(f"TEST CASE #{i+1}: {success}")
    
evaluate_test_cases(test_cases)