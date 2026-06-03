
'''
Write a function(s) to implement the Sieve of Eratosthenes algorithm 

https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes  

This algorithm is used to find all the prime numbers less than or equal to a given integer \verb+n+.  

You should write 2 functions.  One function should implement the Sieve of Eratosthenes algorithm using a list stored as a global variable.  The second function should print whether the given integer is prime or not prime by using the generated list from the first function
'''

primes = []

# Function to implement the Sieve of Eratosthenes algorithm
def sieve_algo(limit):
    global primes
    primes = [True] * (limit + 1) # Begin by assuming all numbers are prime

    # Beginning at 2, we set 0 and 1 to not primes, using index as the number.
    primes[0] = False
    primes[1] = False

    # Begin Algorith - Sieve of Erotsthenes
    for p in range(2, limit + 1):
        if primes[p]:
            for multiple in range(2 * p, limit + 1, p): # Setting muliples of p to False, ie not prime.
                primes[multiple] = False



# Function to print whether the given integer is prime or not prime by using the list from the first function
def isPrime(number):
   limit = number + 1
   sieve_algo(limit)
   if primes[number]:
      print(str(number) + '  is a prime number.')
   else:
      print(str(number) + ' is not a prime number.')

# Testing
isPrime(15)
isPrime(3)
isPrime(100)