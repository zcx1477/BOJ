N = int(input())
dp = [[0] * 3 for i in range(N)]
for i in range(3):
    dp[0][i] = 1

for i in range(1, N):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901

answer = 0

for i in range(3):
    answer += dp[N-1][i]
print(answer%9901)