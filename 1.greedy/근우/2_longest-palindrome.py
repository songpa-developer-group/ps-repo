# 1 <= s.length <= 2000
# "abccccdd"
# 홀수는 1개만 가능
class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer = 0
        count_by_char = {}
        for c in s:
            if c in count_by_char:
                count_by_char[c] += 1
            else:
                count_by_char[c] = 1
        odd_count = 0
        for _, v in count_by_char.items():
            if v % 2 == 0:
                answer += v
            elif odd_count == 0:
                odd_count = 1
                answer += v
            else:
                answer += v - 1
        return answer


print(
    Solution().longestPalindrome(
        "abccccdd"
    )
)
