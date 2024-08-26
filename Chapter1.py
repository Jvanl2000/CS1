import math

#0 degrees Fahrenheit to Celsius
fahrenheit = 0
celsius = round(((fahrenheit - 32) * 5/9), 2)
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius!")

#100 degrees Fahrenheit to Celsius
fahrenheit = 100
celsius = round(((fahrenheit - 32) * 5/9), 2)
print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius!")

#My age in seconds
age_in_yrs = 51
secs_in_min = 60
mins_in_hr = 60
hrs_in_day = 24
days_in_yr = 365
age_in_secs = age_in_yrs * days_in_yr * hrs_in_day * mins_in_hr * secs_in_min
print(f"I am {age_in_yrs} years old, this is approximately {age_in_secs} seconds!")

#My dogs age in seconds
age_in_yrs = 9
age_in_secs = age_in_yrs * days_in_yr * hrs_in_day * mins_in_hr * secs_in_min
print(f"My dog is {age_in_yrs} years old, this is approximately {age_in_secs} seconds!")

#Surface area and volume of a sphere with radius of 6
radius = 6
surface_area_of_sphere = 4 * math.pi * (radius ** 2)
rounded_surface_area_of_sphere = round(surface_area_of_sphere, 2)
volume_of_sphere = 4/3 * math.pi * (radius ** 3)
rounded_volume_of_sphere = round(volume_of_sphere, 2)
print(f"A sphere with a radius of {radius}, has a surface area of {rounded_surface_area_of_sphere}, and a volume of {rounded_volume_of_sphere}!")

#Surface area and volume of a sphere with radius of 18
radius = 18
surface_area_of_sphere = 4 * math.pi * (radius ** 2)
rounded_surface_area_of_sphere = round(surface_area_of_sphere, 2)
volume_of_sphere = 4/3 * math.pi * (radius ** 3)
rounded_volume_of_sphere = round(volume_of_sphere, 2)
print(f"A sphere with a radius of {radius}, has a surface area of {rounded_surface_area_of_sphere}, and a volume of {rounded_volume_of_sphere}!")

#Extract third digit from an_int
an_int = 13579
third_digit_from_right = (an_int // 100) % 10
print(f"The third digit from the right of {an_int} is {third_digit_from_right}!")

#Extract third digit from another_int
another_int = 246810
third_digit_from_right = (another_int // 100) % 10
print(f"The third digit from the right of {another_int} is {third_digit_from_right}!")

##Surface area and volume of a sphere with radius of INPUT
radius = int(input("What is the radius of the sphere? "))
surface_area_of_sphere = 4 * math.pi * (radius ** 2)
rounded_surface_area_of_sphere = round(surface_area_of_sphere, 2)
volume_of_sphere = 4/3 * math.pi * (radius ** 3)
rounded_volume_of_sphere = round(volume_of_sphere, 2)
print(f"A sphere with a radius of {radius}, has a surface area of {rounded_surface_area_of_sphere}, and a volume of {rounded_volume_of_sphere}!")