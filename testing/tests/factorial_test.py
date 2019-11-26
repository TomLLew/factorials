import pytest
from function import factorial

def test_factorial01():
    assert factorial.factorial(6)==3

def test_factorial02():
    assert factorial.factorial(18)=='none'

def test_factorial03():
    assert factorial.factorial(120)==5

def test_factorial05():
    assert factorial.factorial(3628800)==10

def test_factorial06():
    assert factorial.factorial(479001600)==12


