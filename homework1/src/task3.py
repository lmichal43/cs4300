#function to check check if a given number is positive,negative, or zero. 
def check_num(num):
    if (num > 0):
        return "Positive"
    elif (num < 0):
        return "Negative"
    elif (num == 0):
        return "Zero"

#find the first 10 prime numbers
def find_primes(num_primes):
    counter = 0
    number = 2
    primes_list = []

    while counter < num_primes:

        # Iterates through each int until it either has a remainder of 0 or it reaches its own value
        for i in range(2, number + 1):

            # If i reaches number then it means it is a prime number
            if number == i:
                primes_list.append(number)
                counter += 1
                break
            elif number % i == 0:
                break



        # Increments to check the next number
        number += 1

#returns the list of primes
    return primes_list

#function to find the sum of all numbers from 1 to 100
def sum_ints(number):
    counter = 0
    total = 0

    while counter <= number:
        total += counter
        counter += 1

    return total


