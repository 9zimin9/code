# code up - python 100제

# 66
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

if a % 2 == 0:
    print("even")
else:
    print("odd")
if b % 2 == 0:
    print("even")
else:
    print("odd")
if c % 2 == 0:
    print("even")
else:
    print("odd")

# 67
n = int(input())
if n < 0:
    if n % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if n % 2 == 0:
        print('C')
    else:
        print('D')

# 68
n = int(input())
if n >= 90:
    print('A')
else:
    if n >= 70:
        print('B')
    else:
        if n >= 40:
            print('C')
        else:
            print('D')

# 69
n = input()

if n == 'A':
    print("best!!!")
elif n == 'B':
    print("good!!")
elif n == 'C':
    print("run!")
elif n == 'D':
    print("slowly~")
else:
    print("what?")

# 70
"""
12, 1, 2 : winter
3, 4, 5 : spring
6, 7, 8 : summer
9, 10, 11 : fall
"""
n = int(input())

if n//3 == 1:
    print("spring")
elif n//3 == 2:
    print("summer")
elif n//3 == 3:
    print("fall")
else:
    print("winter")

# 71
while True:
    n = int(input())
    if (n == 0):
        break
    print(n)
