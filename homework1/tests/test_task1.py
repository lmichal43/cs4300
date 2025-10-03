import pytest
from src.task1 import helloWorld

def testTask1(capfd):
    #call func
    helloWorld()
    #captures output printed, had to use internet
    out, err = capfd.readouterr()
    #this checks that the output as in fact hello world just like that exactly
    assert out == "Hello world\n"





