def count_direction(array, middle_index):
  middle_value = array[middle_index]
  
  if (middle_value == 1):
    return 'right'
  else:
    return 'left'

def count_ones_binary(array):
  start_index, end_index = 0, len(array)-1
  
  while (start_index <= end_index):
    middle_index = (start_index+end_index) // 2 
    direction = count_direction(array, middle_index)
    
    if (direction == 'right'):
      start_index = middle_index+1
    else:
      end_index = middle_index-1
  return middle_index if middle_index != len(array)-1 else middle_index+1
      

test_cases = [
  {
    'input': {
      'array': [1, 1, 0, 0, 0, 0, 0]
    },
    'output': 2
  },
  {
    'input': {
      'array': [1, 1, 1, 1, 1, 1, 1]
    },
    'output': 7
  },
  {
    'input': {
      'array': [0, 0, 0, 0, 0, 0, 0]
    },
    'output': 0
  }
]

def evaluate_test_cases(test_cases):
  for i in range(len(test_cases)):
    actual_value = count_ones_binary(**test_cases[i]['input'])
    expected_value = test_cases[i]['output']
    
    passed = 'PASSED' if actual_value == expected_value else 'FAILED'
    print(f"TEST CASE{i+1}: {passed}")
    
evaluate_test_cases(test_cases)