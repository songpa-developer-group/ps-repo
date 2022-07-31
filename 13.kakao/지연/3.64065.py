# https://school.programmers.co.kr/learn/courses/30/lessons/64065/
from os import remove
import re


def solution(s):
    answer = []
    array = list(set(re.split('[,{}]', s)))

    for i in range(len(array)):
        if array[i] == '':
            continue
        else:
            answer.append(int(array[i]))
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
