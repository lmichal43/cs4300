import pytest
from src.task2 import returnInt, returnFloat, returnString, returnBool

def testInt():
    result = returnInt()
    assert isinstance(result, int)
    assert result ==5

def testFloat():
    result = returnFloat()
    assert isinstance(result,float)
    assert result == 3.14

def testString():
    result = returnString()
    assert isinstance(result, str)
    assert result == "Hello world"

def testBool():
    result = returnBool()
    assert isinstance(result, bool)
    assert result is True




