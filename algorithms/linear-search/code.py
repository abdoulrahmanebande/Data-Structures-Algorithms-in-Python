def locate_card(cards, query):
  position = 0
  
  while position < len(cards):
    if (query == cards[position]):
      return position
    position += 1
  
  return -1

def evaluate_test_cases(test_cases):
  for i in range(len(test_cases)):
    actual_value = locate_card(**test_cases[i]['input'])
    expected_value = test_cases[i]['output']
    
    print('#TEST CASE {}'.format(i+1))
    if (actual_value == expected_value):
      print('  TEST PASSED!')
    else:
      print('  TEST FAILED!')
    
    
test_cases = [
  {
    'input': {
      'cards': [15, 3, 8, -3, 6, 8],
      'query': 8
    },
    'output': 2
  },
  {
    'input': {
      'cards': [3, 2, 2, 2, 0, 1],
      'query': 2
    },
    'output': 1
  },
    {
    'input': {
      'cards': [1, 3, -1, 2],
      'query': 7
    },
    'output': -1
  },
      {
    'input': {
      'cards': [7],
      'query': 7
    },
    'output': -1
  },
]

evaluate_test_cases(test_cases)