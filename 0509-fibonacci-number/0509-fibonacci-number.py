dp = [-1]*31
class Solution(object):
    def fib(self, n):
        if (n==1 or n==0):
            return n
        if(dp[n]!=-1):
            return dp[n]
        dp[n] = self.fib(n-1)+self.fib(n-2)
        return dp[n]

        