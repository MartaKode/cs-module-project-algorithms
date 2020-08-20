# when are we done with plannig?
# if you can explain problem simply
# ELI5
# good pseudocode

# code a factorial function
# first recursively, then iteratively

# U (Understand)
# Clarify goal:
# Calculate factorial of n

# might google, look up definition of factorial
# 5!
## 5 * 4 * 3 * 2 * 1
# 4! = 4 * 3 * 2 * 1

# 2! = 2
# 1! = 1
# 0! = 1

# P (Plan)
# recursive

# figure out the base case
# maybe 1, if number ==1 return number
# maybe 2, if number == 2 return 2

# how to approach the base
# recurse with n-1

# need to multiply the numbers
# return n * funcname(n-1)

# E (Execute)

def recursive_factorial(n):
    if n < 0:
        return 0
    # Base case
    if n < 2:
        return 1

    return n*recursive_factorial(n-1)

print(recursive_factorial(2))
print(recursive_factorial(1))
print(recursive_factorial(0))
print(recursive_factorial(5))

# R (Review)
# negative numbers
# Handle non-integers
# Handle if return value >> Python's max value
# Used to be BigInt in Python
# now there is no upper bound

# SPace and time complexity?
# Linear in time and space O(n)

# Iteratively
# U
# Plan
# Loop
# for loop
# while loop
# down to 1

# while we're not at 1
# multiply total by the number
# and decrement number

## E
def iterative_factorial(n):
    total = 1

    while n > 1:
        total *= n
        n -= 1

    return total

## run, right, fast

# Review
## Test with 0, 1, 2
print(iterative_factorial(5))
print(iterative_factorial(0))
print(iterative_factorial(2))

## Space and time complexity?
### Linear time O(n)
### Space: we only made 1 variable and are updating it not adding more so 
### Constant space O(1)

# Understand, Plan, Execute, Review

## "intuitive explanation of recursion"
###  3Blue1Brown
### BetterExplained

## Fiagram

## Power!
## Write a function which given a number and an exponent, returns the number raised to that power
## don't use the built-in Python operator

## U
### multiply number by itself that many times
## 2**0.5

### what about if power i 0? -->  1

#   -What is a power
#   -What is an exponent
#   -What is a base
# Constrains (Dont use python operator)

## What about a negative base?
### flips between positive and negative
### in our functions we have to wrap int in parens

## What about a negative exponent?
### 2**(-2)
### 1/(2**2)
### 1/2 * 1/2

## P
### multiply int by itself recursively
### base case is 0
### if power is 0, return 1

## otherwise, recurse with exponent -1

## return number times recursion result

## E
### multiply int by itself recursively
def recursive_power(base, exp):
### base case is 0
### if power is 0, return 1
    if exp == 0:
        return 1

## if exp is 0, make whole thing a fraction
## change exp to positive
    if exp < 0:
        return 1/(base*recursive_power(base, -exp -1))

## otherwise, recurse with exponent -1
## return number times recursion result
    return base * recursive_power(base, exp -1)

## Review
### Check basics
print(recursive_power(2,2))
print(recursive_power(2,3))
### Checked negative bases
print(recursive_power(-2,2))
print(recursive_power(-2,3))
### Check negative exp
print(recursive_power(2,-2))
print()

# should we handle all edge cases on first pass, in E?
## Run
# or wait until review?
## Right, fast

## law of complex systems?
### successful ones have evolved from simple systems

## Iterative version
## Understand
## Plan
#### before loop, check for 0 or negative exponents
#### Use exp as counter
#### loop through multiplying the base

#### if neg exp, return as fraction

## Execute
def iterative_power(base, exp):
#### before loop, check for 0 or negative exponents
    total = 1
    counter = exp
    if exp == 0:
        return 1
#### if neg exp, return as fraction
    if exp < 0:
        counter = -counter # make it positive
        base = 1/base

#### Use exp as counter
    while counter > 0:
#### loop through multiplying the base
        total *= base
        counter -= 1
    return total

## Review
### Check basics
print(iterative_power(0,0)) # 1
print(iterative_power(2,0)) # 1
print(iterative_power(2,2)) # 4
print(iterative_power(2,3)) # 8
### Checked negative bases
print(iterative_power(-2,2)) # 4
print(iterative_power(-2,3)) # -8
### Check negative exp
print(iterative_power(2,-2)) # .25
print(iterative_power(2,-3)) # .125