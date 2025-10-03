import pytest
from src.task2 import returnInt, returnFloat, returnString, returnBool

#testing integer
def testInt():
    #call func and store the return in result
    result = returnInt()
    #checking that the function is in fact returning that type, in this case an int
    assert isinstance(result, int)
    #and that the number is in fcat 5
    assert result ==5
#testing float
def testFloat():
    result = returnFloat()
    #checks that the func is in fcat returning the type float
    assert isinstance(result,float)
    #checks that it in fcat returned 3.14
    assert result == 3.14
#testing string
def testString():
    result = returnString()
    assert isinstance(result, str)
    #checks that the result was in fact hello world written like this
    assert result == "Hello world"
#testing bool
def testBool():
    result = returnBool()
    assert isinstance(result, bool)
    #check that the result was true (correct bool)
    assert result is True




