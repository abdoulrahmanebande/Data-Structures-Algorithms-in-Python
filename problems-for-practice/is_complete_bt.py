from collections import deque
class BTreeNode:
  def __init__(self, key):
    self.key = key
    self.left = None 
    self.right = None 
    
  def __str__(self):
    return f"BTreeNode({self.key}, children:({self.left}, {self.right}))"


  @staticmethod
  def parse_list(data):
    if data is None:
      return None
    
    node = BTreeNode(data[0])
    queue = deque([node])
    
    i = 1
    while (queue and i < len(data)):
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

  def is_perfect_bst(self):
    if self is None:
      return True, 0, 0  # is_complete, height, nodes_count
    
    is_complete_bst_left, height_left, nodes_count_left = BTreeNode.is_complete_bst(self.left)
    is_complete_bst_right, height_right, nodes_count_right = BTreeNode.is_complete_bst(self.right)
    
    is_complete_bst_left = 2**(height_left-1) == nodes_count_left 
    is_complete_bst_right = 2**(height_right-1) == nodes_count_right
    
    height = 1+max(height_left, height_right)
    nodes_count = 1+nodes_count_left+nodes_count_right
    is_complete_bst = is_complete_bst_left and is_complete_bst_right

    return is_complete_bst, height, nodes_count

test_cases = [
  {
    'input': {
      'data': [1,2,3,4,5,6],
    },
    'output': True
  },
    {
    'input': {
      'data': [1,2,3,4,5,None,7],
    },
    'output': False
  },
  {
    'input': {
      'data': [1,2],
    },
    'output': True
  },
  {
    'input': {
      'data': [1]
    },
    'output': False
  },
  {
    'input': {
      'data': [None]
    },
    'output': True
  }
]
print(BTreeNode.is_complete_bst(BTreeNode.parse_list(**test_cases[1]['input'])))

# def evaluate_test_cases(test_cases):
#   print('EVALUATION OF TESTS')
#   for i in range(len(test_cases)):
#     actual_value = BTreeNode.max_depth(BTreeNode.parse_list(**test_cases[i]['input']))
#     expected_value = test_cases[i]['output']
    
#     success = 'TEST PASSED!' if actual_value == expected_value else 'TEST FAILED!'
#     print(f"TEST CASE #{i+1}: {success}")
    
# evaluate_test_cases(test_cases)