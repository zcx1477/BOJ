# *s3..g4 %ko !@$me

d = [0] * 1000010
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, 1000003):
    d[i] = (d[i-1] + d[i-2] + d[i-3]) % 1000000009
T = int(input())
for _ in range(T):
    N = int(input())
    print(d[N])
