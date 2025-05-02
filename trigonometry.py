import math

a = float(input("Enter an angle in degrees: "))

b = math.radians(a)

c = math.sin(b)
d = math.cos(b)
e = math.tan(b)

print(f"Sin({a}°) = {c}")
print(f"Cos({a}°) = {d}")
print(f"Tan({a}°) = {e}")