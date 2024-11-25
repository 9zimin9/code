# code up - python 100제

# 16
a, b = input().split()
print(b, a)

# 17
computerscience = input()
print(computerscience, computerscience, computerscience)

# 18
a, b = input().split(':')
print(a, b, sep=':')

# 19
y, m, d = input().split('.')
print(d, m, y, sep='-')

# 20
a, b = input().split('-')
print(a, b, sep='')

# 21
# hello
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 22
s = input()
print(s[0:2], s[2:4], s[4:6])

# 23
a, b, c = input().split(":")
print(b)

# 24
w1, w2 = input().split()
s = w1 + w2
print(s)

# 25
a, b = input().split()
s = int(a) + int(b)
print(s)

# 26
a = input()
b = input()
s = float(a) + float(b)
print(s)

# 27
a = input()
n = int(a)
print('%x' % n)

# 28
a = input()
n = int(a)
print('%X' % n)

# 29
a = input()
n = int(a, 16)
print('%o' % n)

# 30
print(ord(input()))

# 31
s = int(input())
print(chr(s))
