import pytest
from app import add, subtract
def test_addition():
 assert add(2, 3) == 5
def test_subtraction():
 assert subtract(8, 3) == 5
