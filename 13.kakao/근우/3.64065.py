## https://school.programmers.co.kr/learn/courses/30/lessons/64065/
from collections import defaultdict
import re

def solution(s):
    s = list(map(lambda a: int(a),filter(lambda a: a!='',re.split('[{},]',s))))
    count_map = defaultdict(int)
    for i in s:
        count_map[i]+=1
    a = sorted([[-v,k] for k,v in count_map.items()])
    return [ num for _, num in a]