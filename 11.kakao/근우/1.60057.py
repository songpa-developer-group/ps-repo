## https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):

    def devide_and_make_list(lump, str):
        result = []
        temp = ""
        for j, c in enumerate(str):
            temp += c
            if (j+1)%lump == 0:
                result.append(temp)
                temp = ""
        if len(temp)>0:
            result.append(temp)
        return result

    def make_str_from_list(l):
        result = ""
        temp = ""
        cnt = 0
        for j in l:
            if temp == j:
                cnt+=1
            else:
                if cnt > 1:
                    result += str(cnt)
                result += temp
                temp = j
                cnt = 1
        if cnt>1:
            result += str(cnt)
        result += temp
        return result

    if len(s)==1:
        return 1

    answer = 2e9
    for i in range(1, len(s)):
        l = devide_and_make_list(i, s)
        cur_str = make_str_from_list(l)
        answer = min(answer, len(cur_str))
    return answer


print(solution("aaa"))
