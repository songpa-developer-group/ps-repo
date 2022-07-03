## 2. [longest-palindrome](https://leetcode.com/problems/longest-palindrome/)
class Solution:
    def longestPalindrome(self, s: str) -> int:

        dic = dict()
        for c in s:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1

        answer = 0
        for k, v in dic.items():
            n = v // 2
            answer += (n * 2)
            dic[k] -= (n * 2)

        for k, v in dic.items():
            if v == 1:
                answer += 1
                break
        return answer


if __name__ == "__main__":
    s = "bb"
    print(Solution().longestPalindrome(s))