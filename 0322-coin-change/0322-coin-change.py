class Solution(object):
    def change(self, coins, amount, dp):
        if amount == 0:
            return 0
        if amount < 0:
            return 9999999
        if dp[amount] != -1:
            return dp[amount]
        mini = 9999999
        for i in range(len(coins)):
            ans = self.change(coins, amount - coins[i], dp)
            if ans != 9999999:
                mini = min(ans + 1, mini)
        dp[amount] = mini
        return mini
    def coinChange(self, coins, amount):
        dp = [-1] * (amount + 1)
        ans = self.change(coins, amount, dp)
        if ans == 9999999:
            return -1
        return ans
      