import re 

# input validation for num_jokes
def is_positive_integer(value):
    try:
        num = int(value)
        return num > 0
    except ValueError:
        return False

# input validation for search_term
def is_alphabetic_string(value):
    return bool(re.match("^[a-zA-Z]+$", value))