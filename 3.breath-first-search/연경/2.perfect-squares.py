import math
import sys


class Solution:
    def numSquares(self, n: int) -> int:

        dp = [sys.maxsize for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = 1

        if n <= 1:
            return dp[n]
        # 1 + 1
        dp[2] = 2
        # # 1 + 1 + 1
        # dp[3] = 3
        # dp[4] = 1
        # # 1 + 4
        # dp[5] = 2
        for i in range(3, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]

if __name__ == "__main__":
    n = 6
    print(Solution().numSquares(n))