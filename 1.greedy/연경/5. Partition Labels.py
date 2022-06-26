## 5. [partion-labels](https://leetcode.com/problems/partition-labels/)
def partitionLabels(s):

    location = [-1 for _ in range(26)]
    cur = 1
    location[ord(s[0]) - ord('a')] = cur
    for i in range(1, len(s)):
        c = s[i]
        if location[ord(c) - ord('a')] == -1:
            cur += 1
            location[ord(c) - ord('a')] = cur
        else:
            cur = location[ord(c) - ord('a')]
            for j in range(len(location)):
                if location[j] > cur:
                    location[j] = cur
    answer = [0 for _ in range(max(location))]
    for i, c in enumerate(s):
        idx = location[ord(c) - ord('a')] - 1
        answer[idx] += 1

    return answer

if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    #s = "caedbdedda"
    print(partitionLabels(s))