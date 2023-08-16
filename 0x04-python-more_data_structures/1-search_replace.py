#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if element == search else element for element in my_list]
    return new_list

original_list = [1, 2, 3, 2, 4, 2, 5]
new_list = search_replace(original_list, 2, 99)
print(new_list)
