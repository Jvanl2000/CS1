#Defines PI
PI = 3.14159

#Returns the quotient (without remainder)
def quotient(m: int, n: int) -> int:
  return m // n

#Returns the remainder of a division problem
def remainder(m: int, n: int) -> int:
  return m % n

#Returns the area of a circle
def circle_area(radius: float) -> float:
  return PI * (radius ** 2)

#Calculates Fahrenheit to Celsius
def f_to_c(fahrenheit: float) -> float:
  return (fahrenheit - 32) * (5/9)

#Calculates Celsius to Fahrenheit
def c_to_f(celsius: float) -> float:
  return (celsius * (9/5)) + 32

#Calculates the semester grade while give quarter 1, quarter 2, and final exam grade
def hg_grade(q1: float, q2: float, final: float) -> float:
  return (q1 * 0.4) + (q2 * 0.4) + (final * 0.2)

#Returns the grade you will need to get a certian semester grade
def grade_needed(grade_wanted: float, q1: float, q2: float) -> float:
  return (grade_wanted - ((q1 * 0.4) + (q2 * 0.4))) / 0.2

#Returns the Y cordinate based on the slope, Y intersept, and X cordinate
def linear_eq(slope: float, y_int:float, x_cord: float) -> float:
  return slope * x_cord + y_int

#Returns the cubed root of a number
def cube_rt(number: float) -> float:
  return number ** (1/3)

#Returns the N root of m
def nth_rt(m: float, n: float) -> float:
  return m ** (1/n)

#Returns the distance between two points on a cordinate plane
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
  return nth_rt(((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

#Returns the absoulute value of a number
def abs_val(number: float) -> float:
  return nth_rt((number ** 2), 2)

#Returns the N digit from the right of the number m
def digit_chop(m: float, n: float) -> float:
  return (m // (10 ** (n - 1))) % 10

#Returns what time it will be when alarm will go off (24-hour clock)
def alarm_clock(current_time: float, wait_time: float) -> float:
  return (current_time + wait_time) % 24

#To make perfect change (Like a cashier)
def make_change(cents: int) -> tuple:
  qs = cents // 25
  cents = cents - (qs * 25)
  ds = cents // 10
  cents = cents - (ds * 10)
  ns = cents // 5
  cents = cents - (ns * 5)
  ps = cents // 1
  cents = cents - (ps * 1)
  return qs, ds, ns, ps

#Return the distance between a point and the closest point on a line
def pt_to_line(x: float, y: float, slope: float, y_int: float) -> float:
  a = slope * -1
  b = 1
  c = y_int * -1

  nom = abs(((a) * (x)) + ((b) * (y)) + c)
  dnom = nth_rt(((a)**2) + ((b)**2), 2)

  distance = nom / dnom
  
  return distance