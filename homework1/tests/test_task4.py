from src.task4 import calculate_discount

def test_valid_discount():

    assert calculate_discount(100,20) == 80
    assert calculate_discount(99.99,10) == 89.991
    assert calculate_discount(200,12.5) == 175.0
    assert calculate_discount(50,0) == 50
    assert calculate_discount(50,100) == 0 

def test_invalid_discounts():
    assert calculate_discount(100,-5) == 100
    assert calculate_discount(100,150) == 100



