# code up - python 100제

# 32
n = int(input())
print(-n)

# 33
n = ord(input())  # 아스키 코드로
n = n+1
print(chr(n))    # 유니코드 문자로

# 34
a, b = input().split()
print(int(a)-int(b))

# 35
f1, f2 = input().split()
m = float(f1) * float(f2)
print(m)

# 36
w, n = input().split()
print(w*int(n))

# 37
n = input()
s = input()
print(int(n)*s)

# 38
a, b = input().split()
c = int(a)**int(b)
print(c)

# 39
a, b = input().split()
f1 = float(a)
f2 = float(b)
print(f1**f2)

# 40
a, b = input().split()
print(int(a)//int(b))

# 41
a, b = input().split()
print(int(a) % int(b))

# 42
a = float(input())
print(format(a, ".2f"))

# 43
a, b = input().split()
f1 = float(a)
f2 = float(b)
print(format(f1/f2, ".3f"))

# 44
# 합, 차, 곱, 몫, 나머지, 나눈 값( 소숫점 둘째자리까지)
a, b = input().split()
r1 = int(a)+int(b)
r2 = int(a)-int(b)
r3 = int(a)*int(b)
r4 = int(a)//int(b)
r5 = int(a) % int(b)
r6 = format(int(a)/int(b), ".2f")
print(r1, r2, r3, r4, r5, r6)

# 45
# 합, 평균( 소숫점 둘째 자리까지)
a, b, c = input().split()
n = int(a) + int(b) + int(c)
m = format(n/3, ".2f")
print(n, m)

# 46
n = int(input())
print(n << 1)

# 47
a, b = input().split()
n = int(a)
m = int(b)
print(n << m)
