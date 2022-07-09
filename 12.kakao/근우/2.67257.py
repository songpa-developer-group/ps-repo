## https://programmers.co.kr/learn/courses/30/lessons/67257/

#"100-200*300-500+20"
# expression은 길이가 3 이상 100 이하인 문자열입니다.
# 숫자는 999이하
# calculate(num1, op, num2, index_num)
"""
 - < + < * < / 4!
 5-10-7+8*5+20*7
연산자의 우선순위가 자기보다 같거나 낮은놈이 오게 되면 이때 연산을 처리한다.
 - 현재 읽게 되는 연산자의 레벨이 다음 읽게 되는놈보다 작아질때까지 처리를 한다.
     5-10+7*8
"""
import itertools
import re


def solution(expression):
    def _exec_calculate(num_stack, operator_stack):
        def _exec(num1 ,num2 , op):
            num1 = int(num1)
            num2 = int(num2)
            if op == '+':
                return num1 + num2
            if op == '*':
                return num1 * num2
            if op == '/':
                return num1/num2
            if op == '-':
                return num1-num2
        cur_op = operator_stack.pop()
        num2 , num1 = num_stack.pop(), num_stack.pop()
        num_stack.append(_exec(num1, num2, cur_op))

    list_expression = re.split(r'(\D)', expression)
    operator_set = set(['+','-','*'])
    operator_permutation = list(itertools.permutations(['+','-','*']))
    answer = -2e9
    for c in operator_permutation:
        op_priority = {
            op : priority
            for priority, op in enumerate(c)
        }
        num_stack = []
        operator_stack = []
        for cur in list_expression:
            if cur in operator_set:
                while operator_stack and op_priority[operator_stack[-1]] >= op_priority[cur]:
                   _exec_calculate(num_stack,operator_stack)
                operator_stack.append(cur)
            else:
                num_stack.append(cur)

        while operator_stack:
            _exec_calculate(num_stack,operator_stack)
        answer = max(answer,abs(num_stack[0]))
    return answer
assert solution("100-200*300-500+20") == 60420
assert solution("50*6-3*2") == 300