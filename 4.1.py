a = int(input())
b = int(input())
c = int(input())

if (c**2 == a**2 + b**2) or (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2):
    print("equilateral")
    elif (c**2 < a**2 + b**2) or (a**2 < b**2 + c**2) or (b**2 < a**2 + c**2):
        print("isosceles")
    elif (c**2 > a**2 + b**2) or (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2):
        print("rectangular")
    else:
        print("versatile")