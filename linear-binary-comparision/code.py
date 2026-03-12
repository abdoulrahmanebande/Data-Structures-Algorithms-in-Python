import time 

test_case = {
  'input': {
    'cards': list(range(10000000, 0, -1)),
    'query': 2
  },
  'output': 9999998
}

### Linear Search
start_time_linear = time.perf_counter()
def locate_card_linear(cards, query):
  position = 0
  
  while (position < len(cards)):
    if (cards[position] == query):
      return position
    position += 1
      
  return -1

print(locate_card_linear(**test_case['input']) == test_case['output'])
end_time_linear = time.perf_counter()
execution_time_linear = (end_time_linear-start_time_linear)*1000 # in milliseconds
print(f"Linear Search Execution Time: {execution_time_linear:.0f} ms")

### Binary
start_time_binary = time.perf_counter()

def card_direction(cards, query, middle_position):
  if (cards[middle_position] == query):
    if (middle_position-1 >= 0 and cards[middle_position-1] == query):
      return 'left'
    else:
      return 'found'
  elif (cards[middle_position] > query):
    return 'right'
  else:
    return 'left'
  
def locate_card_binary(cards, query):
  start_index = 0
  end_index = len(cards)-1
  
  while start_index <= end_index:
    middle_position = (start_index+end_index) // 2
    direction = card_direction(cards, query, middle_position)
    
    if (direction == 'found'):
      return middle_position
    elif (direction == 'left'):
      end_index = middle_position-1
    else:
      start_index = middle_position+1
  print('Start', start_index)
  print('End', end_index)
  return -1

print(locate_card_binary(**test_case['input']) == test_case['output'])
end_time_binary = time.perf_counter()
execution_time_binary = (end_time_binary-start_time_binary)*1000 # in milliseconds

print(f"Binary Search Execution Time: {execution_time_binary:.2f} ms")