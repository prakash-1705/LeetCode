class Solution(object):
    def solve(self,cost,n,dp):
        if(n==0 or n==1):
            return cost[n]
        if(dp[n] != -1):
            return dp[n]
        dp[n] = cost[n] + min(self.solve(cost,n-1,dp),self.solve(cost,n-2,dp))
        return dp[n]
    def minCostClimbingStairs(self, cost):
          n = len(cost)
          dp = [-1]*(n+1)
          ans = min(self.solve(cost,n-1,dp),self.solve(cost,n-2,dp))
          return ans