# https://programmers.co.kr/learn/courses/30/lessons/60057

# https://loosie.tistory.com/440
# https://pearlluck.tistory.com/589

def solution(s):
    answer = len(s)
    if len(s) == 1:
        return 1
    for slice in range(1, len(s) // 2 + 1):
        cnt = 0
        tmp = s[:slice]
        pattern = ''
        for cur in range(slice - slice, len(s) + slice, slice):
            if s[cur:cur+slice] == tmp:
                cnt += 1
            else:
                if cnt == 1:
                    pattern += (tmp)
                if cnt > 1:
                    pattern += (str(cnt)+tmp)
                    cnt = 1
                tmp = s[cur:cur+slice]
        answer = min(answer, len(pattern))
    return answer


print(solution('xababcdcdababcdcd'))
