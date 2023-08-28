#!/usr/bin/python3
def safe_print_list(my_list=[], j=0):
    ret = 0
    for k in range(j):
        try:
            print("{}".format(my_list[k]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
