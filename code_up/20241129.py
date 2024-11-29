# code up - python 100제

# 72
n = int(input())
while n != 0:
    print(n)
    n = n-1

# 73
n = int(input())
while n != 0:
    n = n-1
    print(n)

# 74
c = ord(input())
t = ord('a')            # 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환
while t <= c:
    print(chr(t), end=' ')  # 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환
    t += 1

# 75
n = int(input())
m = 0
while m <= n:
    print(m)
    m += 1

# 76
n = int(input())

for i in range(n+1):
    print(i)

# 77
n = int(input())
sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum = sum+i

print(sum)

# 78
while True:
    n = input()
    print(n)
    if n == 'q':
        break

# 79
n = int(input())
a = 0
b = 0
while a < n:
    b = b+1
    a = a+b
print(b)

# 80
n, m = input().split()
n = int(n)
m = int(m)
for i in range(1, n+1):
    for l in range(1, m+1):
        print(i, l)
