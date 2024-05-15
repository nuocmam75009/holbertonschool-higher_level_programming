#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_results = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            """ TypeError is raised when an operation is performed
            on an incorrect object type
            """
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            """ when item attempted to be accessed is
            out of index range of list
            """
            print("out of range")
        finally:
            my_results.append(result)
    return my_results
