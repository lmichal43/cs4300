from src.task7 import numpy_array

def test_numpy_array():
    arr = [1,2,3,4,5]

    result = numpy_array(arr)
    expected_result = {
        "this is the sum": 15, "this is the mean":3, "this is the max": 5,
    }

    assert result == expected_result

def test_numpy_array_neg():

    arr = [-5,-4,-3,-2,-1]

    result = numpy_array(arr)

    expected_result = {
        "this is the sum": -15, "this is the mean": -3, "this is the max": -1,
    }






