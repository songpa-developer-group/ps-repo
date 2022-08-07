from collections import deque


def solution(relation):
    answer = []
    def _putCandidate(candidates):
        answer.append(set(candidates))

    def _checkMinimality(candidates):
        next_candidate = set(candidates)
        for c in answer:
            if c - next_candidate == set():
                return False
        return True

    def _checkUniqueness(candidates):
        check_set = set()
        for r in relation:
            cur = ''
            for c in candidates:
                cur += str(r[c])
            if cur in check_set:
                return False
            check_set.add(cur)
        return True

    column_len = len(relation[0])
    que = deque([[i] for i in range(column_len)])
    while que:
        candidates = que.popleft()
        if _checkMinimality(candidates) and _checkUniqueness(candidates):
            _putCandidate(candidates)
            continue
        last_idx = candidates[-1]
        for _next in range(last_idx+1,column_len):
            que.append(candidates + [_next])
    return len(answer)

# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
# print(solution([["a","b","c"],["a1","b1","c1"],["a2","b2","c2"]]))
print(solution([["a","b","c"],["a","b","d"],["b","b","d"]])) # 1개로만 분별가능



# 0,1,2
#