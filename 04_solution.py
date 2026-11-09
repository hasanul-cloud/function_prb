import math

def circle_states(redius):
   area = round(math.pi * redius ** 2, 2)
   circum = round(2* math.pi * redius, 2)
   return area , circum


a,b = circle_states(3)

print(f"Area: {a}, Circum: {b}")