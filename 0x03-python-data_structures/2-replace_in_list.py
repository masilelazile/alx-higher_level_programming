#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
  if 0 <= idx < len(my_list):
    ew_list = my_list[:idx] + [element] + my_list[idx+1:]
    return new_list
  else:
    return my_list
