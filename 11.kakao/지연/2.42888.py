# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    user = {}
    ACTION, ID, NICKNAME = 0, 1, 2

    for i in record:
        prompt = i.split(' ')
        if prompt[ACTION] == 'Enter':
            user[prompt[ID]] = prompt[NICKNAME]
        if prompt[ACTION] == 'Change':
            user[prompt[ID]] = prompt[NICKNAME]

    for i in record:
        prompt = i.split(' ')
        if prompt[ACTION] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(user[prompt[ID]]))
        if prompt[ACTION] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(user[prompt[ID]]))

    return answer
