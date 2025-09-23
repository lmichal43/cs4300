#function to check check if a given number is positive,negative, or zero. 
def check_num(num):
    if num == 0:
        return "Zero"
    return "Positive" if num > 0 else "Negative"

#find the first 10 prime numbers
def find_primes(num_primes):
    counter = 0
    number = 2
    primes = []

    while counter < num_primes:

        # Iterates through each int until it either has a remainder of 0 or it reaches its own value
        for i in range(2, number + 1):

            # If i reaches number then it means it is a prime number
            if number == i:
                primes.append(number)
                counter = counter+ 1
                break
            elif (number % i == False):
                break



        # Increments to check the next number
        number += 1

#returns the list of primes
    return primes

#function to find the sum of all numbers from 1 to 100
def sum_ints(number):
    return number * (number + 1) // 2

