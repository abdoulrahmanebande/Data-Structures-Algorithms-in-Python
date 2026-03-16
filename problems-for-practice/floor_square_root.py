def floor_square_root(n):
  low = 1
  high = n 
  result = 1
  
  while (low <= high):
    middle = (low+high) // 2
    
    if (middle*middle <= n):
       result = middle
       low = middle+1
    else:
      high = middle-1
      
  return result

def evaluate_test_cases(test_cases):
  for i in range(len(test_cases)):
    actual_value = floor_square_root(**test_cases[i]['input'])
    expected_value = test_cases[i]['output']
    
    success = 'PASSED' if actual_value == expected_value else 'FAILED'
    print(f'TEST CASE #{i+1}: {success}')
    
test_cases = [
  {
    'input': {
      'n': 4
    },
    'output': 2
  },
  {
    'input': {
      'n': 11
    },
    'output': 3
  }, 
  {
    'input': {
      'n': 56
    },
    'output': 7
  }
]

evaluate_test_cases(test_cases)