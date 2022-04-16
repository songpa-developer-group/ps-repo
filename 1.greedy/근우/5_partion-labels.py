from typing import List

# 1 <= s.length <= 500


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_idx_by_idx = []
        answer = []
        for i in range(len(s)):
            end_idx = i
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    end_idx = j
            end_idx_by_idx.append(end_idx)
        cur_max, l = 0, 0
        for i in range(len(end_idx_by_idx)):
            cur_max = max(cur_max, end_idx_by_idx[i])
            if i == cur_max:
                answer.append(i + 1 - l)
                l = i + 1
        if l != len(s):
            answer.append(len(s) - l)
        return answer


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
