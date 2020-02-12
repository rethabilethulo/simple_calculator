from simple_calculator.calculator import *

def test_add_two_numbers():
    assert add(1,2) == 3

def test_add_multiple_numbers():
    assert add(1,2,3,4) == 10

def test_multiply_two_numbers():
    assert multiply(1,3) == 3

def test_multiply_many_numbers():
    assert multiply(1,2,3,4,5) == 120