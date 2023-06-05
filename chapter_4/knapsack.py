def knapsack(capacity, weights, values):
    # 初始化一個二維的 dp 矩陣，用來記錄最大值
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        for j in range(1, capacity + 1):
            if weights[i-1] <= j:
                # 如果當前物品重量小於當前背包容量，則考慮將當前物品放入背包
                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j-weights[i-1]])
            else:
                # 如果當前物品重量大於當前背包容量，則不放入當前物品
                dp[i][j] = dp[i-1][j]
    # 回傳最大值
    print(dp)
    return dp[len(weights)][capacity]

# 範例測試
capacity = 10
weights = [2, 2, 6, 5, 4]
values = [6, 3, 5, 4, 6]
print(knapsack(capacity, weights, values))  # 220
