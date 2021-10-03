
import datetime
import string
import math 

'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n < 2:
    return False  
  for i in range(2, n//2):
    if n % i == 0:
      return False
  return True  

'''
P1
'''  
def get_largest_prime_below(n):
  n -= 1
  while n > 1:
    if is_prime(n):
      return n
    n -= 1  
  return -1


'''
P2
'''
def get_age_in_days(birthday):
  bday = datetime.datetime.strptime(birthday, "%d/%m/%Y")
  today = datetime.datetime.today()
  diff = today-bday
  return diff.days

'''
P3
'''
def get_goldbach(n):
  if n < 4:
    return -1
  for i in range(2, n):
    if is_prime(i) and is_prime(n-i):
      return [i, n-i]       
  return -1

'''
P4
'''
def get_newton_sqrt(n, steps):
  r = n
  while steps > 0:
    r = (r + n / r) / 2
    steps -= 1
  return r

'''

P5
'''
def is_palindrome(n):
  return n[::-1] == n

'''
P6
'''
def is_superprime(n):
  l = len(n)
  while l>0:
    if not is_prime(int(n[0: l])):
      return False
    l -= 1
  
  return True

'''
P7
'''
def is_antipalindrome(n):
  l = len(n)
  for i in range(0, l//2):
    if n[i] == n[l-i-1]:
      return False
  return True

'''
P8
'''
def numberToBase(n, b):
    digs = string.digits + string.ascii_letters
    if n < 0:
        sign = -1
    elif n == 0:
        return digs[0]
    else:
        sign = 1

    n *= sign
    digits = []

    while n:
        digits.append(digs[n % b])
        n = n // b

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

def get_base_2(n):
  return numberToBase(int(n), 2)

'''
P9
'''
def get_base_16_from_2(n):
  return numberToBase(int(n), 16)

'''
P10
'''
def factorial(n):
  p = 1
  while n > 0:
    p *= n
    n -= 1
  return p

def get_n_choose_k(n, k):
  n_fact = factorial(int(n))
  k_fact = factorial(int(k))
  n_k_fact = factorial(int(n)-int(k))
  return int(n_fact / (k_fact * n_k_fact))

'''
P11
'''
def is_leap(year):
  if year % 400 == 0:
    return True
  if year % 4 == 0:
    return True
  return False
      
def get_leap_years(year1, year2):
  resp = []
  for y in range(year1, year2):
    if is_leap(y):
      resp.append(y)
  return resp

'''
P12
'''
def get_perfect_squares(start, end):
  resp = []

  for v in range(start, end):
    root = math.sqrt(v)
    if int(root + 0.5)**2 == v:
      resp.append(v)

  return resp

'''
P13
'''
def get_temp(temp, fromScale, toScale):
  if fromScale == 'F' and toScale == 'C':
    return (temp - 32) * 5/9
  elif fromScale == 'C'and toScale == 'F':
    return (temp * 9/5) + 32
  elif fromScale == 'K' and toScale == 'C':
    return temp - 273.15
  elif fromScale == 'C' and toScale == 'K':
    return temp + 273.15
  elif fromScale == 'F' and toScale == 'K':
    return (temp - 32) * 5/9 + 273.15  
  elif fromScale == 'K' and toScale == 'F':
    return (temp - 273.15) * 9/5 + 32      

  return -1

'''
P14
'''
def get_cmmdc(x, y):
  while x != y:
    if x > y:
      x -= y
    else:
      y -= x
  return x

def get_cmmmc(vals):
  resp = vals[0]
 
  for v in range(1, len(vals)):
    resp = get_cmmdc(resp, vals[v])
  
  return resp   

def main():
  # interfata de tip consola aici
  print("""
  Menu:
  1. get_largest_prime_below
  2. get_age_in_days
  3. get_goldbach
  4. get_newton_sqrt
  5. is_palindrome
  6. is_superprime
  7. is_antipalindrome
  8. get_base_2
  9. get_base_16_from_2
  10. get_n_choose_k
  11. get_leap_years
  12. get_perfect_squares
  13. get_temp
  14. get_cmmmc
  0. exit
  """)
  selection = int(input('Selectia:'))
  if selection == 0:
    return
  if selection == 1:
    n = int(input('n='))
    print('Largest prime:', get_largest_prime_below(n));
  elif selection == 2:
    bday = input('Birthday DD/MM/YYYY:');
    print('Age in days:', get_age_in_days(bday))  
  elif selection == 3:
    print('Goldbachs numbers:', get_goldbach(int(input('n='))))
  elif selection == 4:
    print('Newtowns sqrt:', get_newton_sqrt(float(input('n=')), int(input('steps='))))
  elif selection == 5:
    print('Is palindrom:', is_palindrome(input('String to test:')))
  elif selection == 6:
    print('Is super prime:', is_superprime(input('Number:')))
  elif selection == 7:
    print('Is antipalindrom:', is_antipalindrome(input('Number:')))
  elif selection == 8:
    print('Get base 2 from 10:', get_base_2(input('Number:')))
  elif selection == 9:
    print('Get base 16 from 2:', get_base_16_from_2(input('Number:')))
  elif selection == 10:
    print('Get n choose k:', get_n_choose_k(input('n:'), input('k:')))
  elif selection == 11:
    print('Ani bisecti:', get_leap_years(int(input('year1:')), int(input('year2:')))) 
  elif selection == 12:
    print('Perfect squares:', get_perfect_squares(int(input('start:')), int(input('end:')))) 
  elif selection == 13:
    print('Get temp:', get_temp(int(input('temp:')), input('from:'), input('to:'))) 
  elif selection == 14:
    list_of_vals = input('values:').split()
    print('Get cmmdc:', get_cmmmc(list(map(int, list_of_vals))))                           
  main()

if __name__ == '__main__':
  main()
