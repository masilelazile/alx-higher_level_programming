#!/usr/bin/python3
def delete_at(my_list, idx):
    if 0 <= idx < len(my_list):
        new_list = []
        for i in range(len(my_list)):
            if i != idx:
                new_list.append(my_list[i])
        return new_list
    else:
        return my_list
