# code up - python 100제

# 93
n = int(input())    # 출석 번호를 부른 횟수
a = input().split()

for i in range(n):
    a[i] = int(a[i])

for i in range(n-1, -1, -1):
    print(a[i], end=' ')

# 94
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

print(min(a))

# 95
# 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때, n개의 흰 돌이 놓인 위치를 출력
a = []
for i in range(20):
    a.append([])
    for l in range(20):
        a[i].append(0)   # 리스트 안에 들어있는  리스트 안에 0 추가해 넣기

n = int(input())
for i in range(n):
    x, y = input().split()
    a[int(x)][int(y)] = 1

for i in range(1, 20):
    for l in range(1, 20):
        print(a[i][l], end=' ')
    print()

# 96
d = []

for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(19):
    a = input().split()
    for j in range(19):
        d[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n):
    x, y = input().split()
    for j in range(1, 20):
        if d[j][int(y)] == 0:
            d[j][int(y)] = 1
        else:
            d[j][int(y)] = 0

        if d[int(x)][j] == 0:
            d[int(x)][j] = 1
        else:
            d[int(x)][j] = 0
for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()
