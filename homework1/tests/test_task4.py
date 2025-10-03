from src.task4 import calculate_discount

#Write pytest test cases to test the calculate_discount function with various types (integers, floats) for price and discount
def test_valid_discount():
    #testing using different types like using decimal stuff and 0
    assert calculate_discount(100,20) == 80
    assert calculate_discount(99.99,10) == 89.991
    assert calculate_discount(200,12.5) == 175.0
    assert calculate_discount(50,0) == 50
    assert calculate_discount(50,100) == 0 

#testing also for the ones that technically would be invalid such as negative or over 100
def test_invalid_discounts():
    assert calculate_discount(100,-5) == 100
    assert calculate_discount(100,150) == 100



