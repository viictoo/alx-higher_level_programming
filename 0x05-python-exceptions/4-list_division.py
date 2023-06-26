#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    for iter in range(list_length):
        qt = 0
        try:
            qt = my_list_1[iter] / my_list_2[iter]
        except (TypeError,  ValueError):
            print("wrong type")
        except (ZeroDivisionError):
            print("division by 0")
        except (IndexError):
            print("out of range")
        finally:
            my_list.append(qt)
    return my_list
