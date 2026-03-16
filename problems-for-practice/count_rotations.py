def search_direction(nums, middle_position):
  middle_value, before_middle_value = nums[middle_position], nums[middle_position-1]
  first_list_element, last_list_element = nums[0], nums[len(nums)-1]
  
  if (middle_value > before_middle_value):
    if (middle_value < last_list_element):
      return 'left'
    else:
      return 'right'
  else:
    if (middle_value == first_list_element):
      return 'full-rotation'
    else:
      return 'found'   
     
def count_rotations(nums):
  
  if (len(nums) == 0):
    return 0
  elif (len(nums) == 1):
    return 1
  
  start_index, end_index = 0, len(nums)-1
  while (start_index <= end_index):
    middle_position = (start_index+end_index) // 2
    direction = search_direction(nums, middle_position)
    
    if (direction == 'found'):
      return middle_position
    elif (direction == 'left'):
      end_index = middle_position-1
    elif (direction == 'right'):
      start_index = middle_position+1
    else:
      return len(nums)
  return 1 

test_cases = [
  {
    'input': {
      'nums': [5, 6, 9, 0, 2, 3, 4] 
    },
    'output': 3 
  },
  {
    'input': {
      'nums': [1, 3, 5],
    },
    'output': 3
  },
  {
    'input': {
      'nums': [3],
    },
    'output': 1
  },
  {
    'input': {
      'nums': [],
    },
    'output': 0
  },
  {
    'input': {
      'nums': [4, 6, 7, 2],
    },
    'output': 3
  } 
] 

def evaluate_test_cases(test_cases):
  for i in range(len(test_cases)):
    actual_value = count_rotations(**test_cases[i]['input'])
    expected_value = test_cases[i]['output']
    
    print(actual_value == expected_value)
    
evaluate_test_cases(test_cases)
