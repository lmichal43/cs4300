import pytest
from src.task1 import helloWorld

def testTask1(capfd):
    helloWorld()
    out, err = capfd.readouterr()
    assert out == "Hello world\n"





