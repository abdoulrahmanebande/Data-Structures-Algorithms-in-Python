def test_location(cards, middle_position, query):
  
  if (cards[middle_position] == query):
    if (middle_position-1 >= 0 and cards[middle_position-1] == query):
      return 'left'
    else:
      return 'found'
  elif (cards[middle_position] > query):
    return 'left'
  else:
    return 'right'
  
  
def locate_card(cards, query):
  first_position = 0
  last_position = len(cards)-1
  
  while first_position <= last_position:
    middle_position = (first_position+last_position) // 2
    
    result = test_location(cards, middle_position, query)
    if (result == 'found'):
      return middle_position
    elif (result == 'left'):
      last_position = middle_position-1
    else:
      first_position = middle_position+1
      
  return -1

def evalutate_test_cases(test_cases):
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
      'cards': [-3, 3, 6, 8, 15, 18, 23],
      'query': 3
    }, 
    'output': 1
  },
  {
    'input': {
      'cards': [6, 8, 18, 23],
      'query': 18
    }, 
    'output': 2
  },
  {
    'input': {
      'cards': [6],
      'query': 6
    }, 
    'output': 0
  },
  {
    'input': {
      'cards': [6],
      'query': 18
    }, 
    'output': -1
  },
  {
    'input': {
      'cards': [],
      'query': 18
    }, 
    'output': -1
  },
  {
    'input': {
      'cards': [2, 4, 5, 7, 7, 7, 7, 7, 89, 101],
      'query': 7
    }, 
    'output': 3
  },
]

evalutate_test_cases(test_cases)