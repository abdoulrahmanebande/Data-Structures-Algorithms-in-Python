def target_direction(nums, target, middle_index):
  middle_value = nums[middle_index]
  
  if (middle_value == target):
    if (middle_index-1 >= 0 and nums[middle_index-1] == target):
      return 'left'
    else:
      return 'found'
  elif (middle_value > target):
    return 'left'
  else: 
    return 'right'
  
def search_target_binary(nums, target):
  start_index, end_index = 0, len(nums)-1
  
  while (start_index <= end_index):
    middle_index = (start_index+end_index) // 2
    search_direction = target_direction(nums, target, middle_index)
    
    if (search_direction == 'found'):
      return middle_index
    elif (search_direction == 'left'):
      end_index = middle_index-1
    else:
      start_index = middle_index+1
  return -1


test_cases = [
  {
    'input': {
      'nums': [-3, 3, 6, 8, 15, 18, 23],
      'target': 3
    }, 
    'output': 1
  },
  {
    'input': {
      'nums': [6, 8, 18, 23],
      'target': 18
    }, 
    'output': 2
  },
  {
    'input': {
      'nums': [6],
      'target': 6
    }, 
    'output': 0
  },
  {
    'input': {
      'nums': [6],
      'target': 18
    }, 
    'output': -1
  },
  {
    'input': {
      'nums': [],
      'target': 18
    }, 
    'output': -1
  },
  {
    'input': {
      'nums': [2, 4, 5, 7, 7, 7, 7, 7, 89, 101],
      'target': 7
    }, 
    'output': 3
  },
]

def evaluate_test_cases(test_cases):
  for i in range(len(test_cases)):
    actual_value = search_target_binary(**test_cases[i]['input'])
    expected_value = test_cases[i]['output']
    
    is_failed = 'FAILED' if actual_value != expected_value else 'SUCCESS'
    print(f"#TEST-CASE {i}: {is_failed}")
    
evaluate_test_cases(test_cases)