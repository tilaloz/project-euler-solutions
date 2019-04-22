# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 05:39:17 2019

A solution for Project Euler Problem #12
First triangle number with 500 divisors

@author: Owner
"""
import math
from collections import Counter

def next_possible_prime(n):
    """yield the next possible prime up to n (skipping by 2s and 3s)"""
    current = 5
    increment = 2
    while current <= n:
        yield current
        current += increment
        increment = 6 - increment
        
def next_prime(n):
    """yield the next prime <= n"""
    yield 2
    yield 3
    # For the rest use the sieve
    sieve = [ True ]*(n + 1)
    for candidate in next_possible_prime(n):
        if sieve[candidate]:
            yield candidate
            for i in range(candidate*candidate,n,candidate):
                sieve[i] = False

def primes(n):
    """Return a list of all primes <= n"""
    primes = [2,3]
    sieve = [ True ]*(n + 1)
    for candidate in next_possible_prime(n):
        if sieve[candidate]:
            primes.append(candidate)
            for i in range(candidate*candidate,n,candidate):
                sieve[i] = False
    return primes
            
def factor(n):
    """Return the list of prime factors for n"""
    remaining = n
    factors = []
    for prime in next_prime(int(math.sqrt(n))+1):
        while not remaining % prime:
            factors.append(prime)
            remaining = remaining/prime
        if remaining == 1: return factors 
    
def divisor_function(n):
    factors = factor(n)
    c = Counter(factors)
    sigma = 1
    for v in c.values():
        sigma *=(v+1)
    return sigma

def triangle_number(n):
    return n*(n+1)/2    
    
if __name__ == "__main__":
    n_divisors = 0
    n = 10
    while not n_divisors == 500:
        n += 1
        n_divisors = divisor_function(triangle_number(n))
        print(n,n_divisors)
    
   