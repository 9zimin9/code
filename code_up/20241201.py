# code up - python 100제

# 81
a = int(input(), 16)

for i in range(1, 16):
    print("%X*%X=%X" % (n, i, n*i))

# 82
a = int(input())

for i in range(1, a+1):
    if (i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
        print("X", end=' ')
    else:
        print(i, end=' ')

# 83
r, g, b = input().split()
r, g, b = int(r), int(g), int(b)

for i in range(0, r):
    for j in range(0, g):
        for k in range(0, b):
            print(i, j, k)
print(r*g*b)

# 84
a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
print(round(a*b*c*d/8/1024/1024, 1), "MB")

# 85
a, b, c = input().split()
res = int(a)*int(b)*int(c)/1024/1024/8
print('%.2f' % res, "MB")

# 86
a = int(input())
b = 0
c = 0

while True:
    b = b+c
    c = c+1
    if b >= a:
        break
print(b)

# 87
a = int(input())

for i in range(1, a+1):
    if i % 3 == 0:
        continue
    else:
        print(i, end=' ')

# 88
a, d, n = input().split()
a, d, n = int(a), int(d), int(n)
print(a+d*(n-1))

# 89
a, r, n = input().split()
a, r, n = int(a), int(r), int(n)

for i in range(1, n):
    a = a*r
print(a)

# 90
a, m, d, n = input().split()
a, m, d, n = int(a), int(m), int(n)

for i in range(1, n):
    a = a*m+d
print(a)

# 91
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
i = 1

while i % a != 0 or i % b != 0 or i % c != 0:
    i += 1
print(i)

# 92
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])
d = []
for i in range(24):
    d.append(0)
for i in range(n):
    d[a[i]] += 1
for i in range(1, 24):
    print(d[i], end=' ')
