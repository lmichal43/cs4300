from src.task3 import check_num, find_primes, sum_ints

#check with different numbers all of which result in a different output to ensure everything works
def test_check_num():
    assert check_num(5) == "Positive"
    assert check_num(-10) == "Negative"
    assert check_num(0) == "Zero"

def test_find_primes():
    #first 10 prime numbers specfically as per the assignemnt
    result = find_primes(10)
    #the first 10 prime numbers listed
    assert result == [2,3,5,7,11,13,17,19,23,29]

def test_sum_ints():
    #the sum of numebrs from 1 to 100 is 5050 and so it checks that 
    assert sum_ints(100) == 5050
    #1+2+3+4+5 = 15
    assert sum_ints(5) == 15
