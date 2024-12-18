#1. Task 3: Find the second largest number in a list
def second_largest(numbers):
  unique_numbers = list(set(numbers))                
  unique_numbers.sort()                                      
  return unique_numbers[-2]                               
numbers = [10, 20, 4, 45, 99]
output = second_largest(numbers)
print(output)
