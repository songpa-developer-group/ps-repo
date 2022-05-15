## https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x
        answer = 0
        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= x:
                answer = max(mid, answer)
                left = mid + 1
            else:
                right = mid - 1

        return answer

if __name__ == "__main__":
    x = 8
    print(Solution().mySqrt(x))