# hypotenuse.py - Versi sederhana
import math

print("pythagorean theorem")
a = float(input("input length a: "))
b = float(input("input length b: "))

c = math.sqrt(a**2 + b**2)
print(f"hypotenuse: {c:.2f}")