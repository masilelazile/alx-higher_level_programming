#!/usr/bin/python3
my_list = [10, 20, 30, 40, 50]
index = 2
result = element_at(my_list, index)

if result is not None:
  print(f"The element at index {index} is: {result}")
else:
  print(f"Invalid index {index}")
