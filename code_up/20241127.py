# code up - python 100제

# 48
a, b = input().split()
n = int(a)
m = int(b)
if n < m:
    print("True")
else:
    print("False")

# 49
a, b = input().split()
a = int(a)
b = int(b)
print(a == b)

# 50
a, b = input().split()
a = int(a)
b = int(b)
print(a <= b)

# 51
a, b = input().split()
a = int(a)
b = int(b)
print(a != b)

# 52
n = int(input())
print(bool(n))

# 53
n = bool(int(input()))
print(not n)

# 54
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# 55
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

# 56
a, b = input().split()
n = bool(int(a))
m = bool(int(b))
print((n and (not m)) or ((not n) and m))

# 57
a, b = input().split()
print(not a != b)      # != 는 두 값이 다르면 true 반환

# 58
a, b = input().split()
n = bool(int(a))
m = bool(int(b))
print(not n and not m)

# 59
a = int(input())
print(~a)

# 60
a, b = input().split()
print(int(a) & int(b))

# 61
a, b = input().split()
print(int(a) | int(b))

# 62
a, b = input().split()
print(int(a) ^ int(b))

# 63
a, b = input().split()
a = int(a)
b = int(b)
c = (a if (a >= b) else b)   # a>=b 비교연산 결과가 true면 a반환, false면 b반환
print(int(c))

# 64
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
d = a if a < b else b
e = d if d < c else c
print(e)

# 65
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

if a % 2 == 0:
    print(a)

if b % 2 == 0:
    print(b)

if c % 2 == 0:
    print(c)
