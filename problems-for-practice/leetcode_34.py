def target_direction(nums, target, middle_index, position_type):
  if (nums[middle_index] == target):
    if (position_type == 'first' and middle_index-1 >= 0 and nums[middle_index-1] == target):
      return 'left'
    elif (position_type == 'last' and middle_index+1 <= len(nums)-1 and nums[middle_index+1] == target):
      return 'right'
    else: 
      return 'found'
  elif (nums[middle_index] > target):
    return 'left'
  else:
    return 'right'
  
def find_first_position(nums, target):
  """
  Find First Position of Element in Sorted Array
  """
  start_index, end_index = 0, len(nums)-1
  
  while (start_index <= end_index):
    middle_index = (start_index+end_index) // 2
    direction = target_direction(nums, target, middle_index,'first')
    
    if (direction == 'found'):
      return middle_index
    elif (direction == 'left'):
      end_index = middle_index-1
    else:
      start_index = middle_index+1
  return -1
  
def find_last_position(nums, target):
  """
  Find Last Position of Element in Sorted Array
  """
  start_index, end_index = 0, len(nums)-1
  while(start_index <= end_index):
    middle_index = (start_index+end_index) // 2
    direction = target_direction(nums, target, middle_index, 'last')
    
    if (direction == 'found'):
      return middle_index
    elif (direction == 'left'):
      end_index = middle_index-1
    else:
      start_index = middle_index+1
  return -1

def find_first_and_last_position(nums, target):
  return [find_first_position(nums, target), find_last_position(nums, target)]

def evaluate_test_cases(test_cases):
  for i in range(len(test_cases)):
    actual_value = find_first_and_last_position(**test_cases[i]['input'])
    expected_value = test_cases[i]['output']
    
    print(f"#TEST CASE {i+1}:")
    if (actual_value == expected_value):
      print(" TEST PASSED!")
    else:
      print(" TEST FAILED!")
    
test_cases = [
  {
    'input': {
      'nums': [5,7,7,8,8,10], 
      'target': 8
    },
    'output': [3,4]
  },
  {
    'input': {
      'nums': [5,7,7,8,8,10],
      'target': 6
    },
    'output': [-1,-1]
  },
  {
    'input': {
      'nums': [],
      'target': 0
    },
    'output': [-1,-1]
  },
  {
    'input': {
      'nums': [3],
      'target': 3
    },
    'output': [0,0]
  },
    {
    'input': {
      'nums': [5,5],
      'target': 5
    },
    'output': [0,1]
  }
]

print(evaluate_test_cases(test_cases))