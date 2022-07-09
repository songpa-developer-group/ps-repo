## https://programmers.co.kr/learn/courses/30/lessons/72412/
"""
constraint 1<= info <=50000
query 1<=query len <=100000
개발언어는 cpp, java, python 중 하나입니다.
직군은 backend, frontend 중 하나입니다.
경력은 junior, senior 중 하나입니다.
소울푸드는 chicken, pizza 중 하나입니다.
점수 X
appoach
composite index : using chaining index
a,b,c,d
b,a,c,d
c,d,e,a
2^4 마지막에는 score가 rangesearch할 수 , 1 이상 100,000 이하인 자연수입니다. binary정렬되게 저장
"""
from bisect import bisect_left
from collections import defaultdict


def solution(infos, querys):
    infos = [list(i.split()) for i in infos]
    for info in infos:
        info[-1] = int(info[-1])
    infos.sort(key = lambda item: item[-1])

    querys = [[c for c in list(i.split()) if c != 'and'] for i in querys]
    for query in querys:
        query[-1] = int(query[-1])

    # language
        # career
            # food
                # score_sorted_list
    index = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(list))))
    WILD_CARD = '-'
    # make composite index
    for language, position, career, food, score in infos:
        for l in [WILD_CARD, language]:
            for p in [WILD_CARD,position]:
                for c in [WILD_CARD, career]:
                    for f in [WILD_CARD ,food]:
                        index[l][p][c][f].append(score)

    return [len(index[l][p][c][f]) - bisect_left(index[l][p][c][f], s) for l,p,c,f,s in querys]





info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
]
expected = [1,1,1,1,2,4]
assert solution(info, query) == expected

