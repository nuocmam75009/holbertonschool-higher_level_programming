#!/usr/bin/python3
def safe_print_division(a, b):
    """ mettre result=none pour être sur que result a tjr une valeur
        sans initialisé, s'il y a zerodivisionerror, cela va donner NameError
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        """ zerodivisionerror is when program attempts
    a division where denominator is 0
        """
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
