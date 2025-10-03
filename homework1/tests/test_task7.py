from src.task7 import numpy_array

def test_numpy_array():
    #testing with a normal array
    arr = [1,2,3,4,5]
    #call function
    result = numpy_array(arr)
    #listing the expected results
    expected_result = {
        "this is the sum": 15, "this is the mean":3, "this is the max": 5, 
    }
    #checking that it matches
    assert result == expected_result

#this i tested with a negative array
def test_numpy_array_neg():
    #using negative numbers just to check
    arr = [-5,-4,-3,-2,-1]
    result = numpy_array(arr)
    #listing the expected results
    expected_result = {
        "this is the sum": -15, "this is the mean": -3, "this is the max": -1,
    }
    #checking that it is what we expected
    assert result == expected_result








