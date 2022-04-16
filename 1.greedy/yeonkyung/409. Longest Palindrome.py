def longestPalindrome(s):

    upper = [0 for _ in range(26)]
    lower = [0 for _ in range(26)]

    for c in s:
        if c.isupper():
            upper[ord(c) - ord('A')] += 1
        else:
            lower[ord(c) - ord('a')] += 1

    answer = 0
    for i in range(len(upper)):
        u = upper[i]
        tmp = (u // 2) * 2
        answer += tmp
        upper[i] -= tmp

    for i in range(len(lower)):
        l = lower[i]
        tmp = (l // 2) * 2
        answer += tmp
        lower[i] -= tmp

    return answer + 1 if sum(upper) > 0 or sum(lower) > 0 else answer

if __name__ == "__main__":
    s = "abccccdd"
    print(longestPalindrome(s))