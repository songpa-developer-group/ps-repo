class Solution:
    def partitionLabels(self, testcase: str):
        # 1. 각 글자의 end_idx를 구한다.
        testcase_end_idx = []
        for word in testcase:
            word_end_idx = 0
            for cur_idx in range(len(testcase)):
                # 각 word 마다 list를 탐색
                if(word == testcase[cur_idx]):
                    # word의 idx를 계속 update해서 end_idx 찾음
                    word_end_idx = cur_idx
                else:
                    continue
            testcase_end_idx.append(word_end_idx)
        # 2. end_idx를 구했으면 해당 단어의 집합이 끝나는 지점의 값을 구한다.
        partition = []
        max_idx = 0
        partition_length = 0
        for cur_idx in range(len(testcase_end_idx)):
            max_idx = max(max_idx, testcase_end_idx[cur_idx])
            print("현재 %d번째 %s ..%d번까지는 읽어야 한다." %(cur_idx, testcase[cur_idx], testcase_end_idx[max_idx]))
            if(cur_idx == testcase_end_idx[max_idx]):
                partition.append(partition_length + 1)
                partition_length = 0
            else:
                partition_length += 1
        return partition


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
