# Problem: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
# Score: 20


from collections import defaultdict
n, m = map(int, input().split())
# adding inputs for group A,B
A = [input() for i in range(n)]
B = [input() for i in range(m)]

d = defaultdict(list)
for i in range(n):
    d[A[i]].append(i+1)

for i in B:
    if i in d:
        print(*d[i])
    else:
        print(-1)
