from helper import is_positive_integer, is_alphabetic_string

# Test the helper functions
def test_is_positive_integer():
    assert is_positive_integer('5') is True
    assert is_positive_integer('-1') is False
    assert is_positive_integer('0') is False
    assert is_positive_integer('abc') is False
    assert is_positive_integer('3.5') is False

def test_is_alphabetic_string():
    assert is_alphabetic_string('hello') is True
    assert is_alphabetic_string('world123') is False
    assert is_alphabetic_string('123') is False
    assert is_alphabetic_string('!@#') is False
    assert is_alphabetic_string('HelloWorld') is True