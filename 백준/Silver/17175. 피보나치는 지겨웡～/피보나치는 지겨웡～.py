dp = [1, 1]
for i in range(int(input())-1):
    dp.append((dp[i]+dp[i+1]+1)%1000000007)
print(dp[len(dp)-1])