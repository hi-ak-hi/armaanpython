from time import sleep
from fractions import Fraction

print("------first point-------")
#sleep(1)
x1 = int(input("X: "))
y1 = int(input("Y: "))

print("------second point-------")
#sleep(1)
x2 = int(input("X: "))
y2 = int(input("Y: "))

top = y2 - y1
bottom = x2 - x1

slope = top/bottom
temp = float(slope)*x1
y_int = y1-temp
slope = Fraction(slope)

if y_int >= 0:
    print("y = " + str(slope) + "x" + " + " + str(y_int))
if y_int < 0:
    print("y = " + str(slope) + "x" + " - " + str(y_int))