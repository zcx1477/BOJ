s = set([])
N = int(input())
for _ in range(N):
    s.update(list(map(int, input().split())))
if len(s)<3*N:
    print("1")
else:
    print("0")
