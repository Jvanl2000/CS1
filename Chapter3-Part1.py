import sys


#Returns the sum of all of the square value added together
def sum_squares(list):
  value = 0
  for num in list:
    value += num ** 2
  print(value)
  return value

#Returns the factorial of the number (n) given
def factorial(n):
  value = 1
  for i in range(1, n + 1):
    value = value * i
  print(value)
  return value

#Returns the sumtorial of the number (n) given
def sumtorial(n):
  value = 0
  for i in range(1, n + 1):
    value = value + i
  print(value)
  return value

#Sums n amount of odds (1 + 3 + 5 + 7 ...)
def sum_n_odds(n):
  value = 0
  odd_value = 1
  for i in range(0, n):
    value += odd_value
    odd_value += 2
  print(value)
  return value

#Returns the sum of any odd number between 0 and n
def sum_odds_to_n(n):
  value = 0
  for i in range(1, n + 1):
    if i % 2 != 0:
      value += i
  print(value)
  return value

#Returns the Nth digit of the Fibonacci Sequence
def fib(n):
  a, b = 1, 0
  for i in range(n):
    b = a
    a = a + b
  return a

#Returns the Nth digit of the Tribonacci Sequence
def trib(n):
  a, b, c = 1, 0, 0
  for i in range(n):
    c = b
    b = a
    a = b + c
  return a

#Returns the harmonic series to the Nth precision
def harmonic_series(n):
  value = 0
  for i in range(1, n + 1):
    value += 1/i
  print(value)
  return value

#Returns the value of the sum of the Nth alternating sequence (1 - 2 + 3 - 4...)
def alt_signs(n):
  if n % 2 == 0:
    return int((n/2)**2 - (n/2) * ((n/2) + 1))
  elif n % 2 != 0:
    return int(((n + 1)/2)**2 - ((n - 1)/2) * ((n + 1)/2))

#Aproximates PI to a persision of n
def pi_approx(n):
  odd_values = 1
  value = 0
  for i in range(1, n + 1):
    if i % 2 != 0:
      value += (1/odd_values)
      odd_values += 2
    elif i % 2 == 0:
      value -= (1/odd_values)
      odd_values += 2
  print(value * 4)
  return 4 * value

#Generates any possible geometric series
def geometric_series(i, n, r):
  value = 0
  for iter in range(0, n):
    value += i * (r ** iter)
  print(value)
  return value

#Returns the sum of 1/1 + 3/(1+3) + 5/(1+3+5)+...
def iter_iter(n):
  value = 0
  up_odd_value = 1
  down_odd_value = 1
  for i in range(1, n + 1):
    value += (up_odd_value/down_odd_value)
    up_odd_value += 2
    down_odd_value = sum_n_odds(i + 1)
  print(value)
  return value

#Addition via repeated +1 addition
def addition(a, n):
  value = a
  for i in range(0, n):
    value += 1
  print(value)
  return value

#Multiplication via repeated addition
def multiplication(a, n):
  value = a
  for i in range(1, n):
    value = addition(value, a)
  print(value)
  return value

#Exponentiation via reapeated multiplication
def exponentiation(a, n):
  value = a
  for i in range(1, n):
    value = multiplication(value, a)  
  print(value)
  return value

#Tetration via repeated exponentiation
def tetration(a, n):
  sys.set_int_max_str_digits(999999)
  if n == 0:
    return 1
  return a ** tetration(a, n - 1)

print(trib(1))
print(trib(8))
print(trib(16))