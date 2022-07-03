## https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    nicknames = dict()

    for chat in record:
        split = chat.split(' ')
        if len(split) == 3:
            action, user_id, nickname = split
        elif len(split) == 2:
            action, user_id = split

        if action == 'Enter':
            nicknames[user_id] = nickname
        elif action == 'Change':
            nicknames[user_id] = nickname

    for chat in record:
        split = chat.split(' ')
        if len(split) == 3:
            action, user_id, nickname = split
        elif len(split) == 2:
            action, user_id = split

        if action == 'Enter':
            answer.append(nicknames[user_id] + '님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(nicknames[user_id] + '님이 나갔습니다.')

    return answer

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi",
              "Enter uid4567 Prodo",
              "Leave uid1234",
              "Enter uid1234 Prodo",
              "Change uid4567 Ryan"]
    print(solution(record))