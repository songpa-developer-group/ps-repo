## https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    name_by_id = {}
    for r in record:
        if r[:5] == "Leave":
            continue
        cmd, id, name = r.split()
        if cmd == "Enter" or cmd == "Change":
            name_by_id[id] = name
    for r in record:
        if r[:5] == "Enter":
            _, id, _ = r.split()
            answer.append("{}님이 들어왔습니다.".format(name_by_id[id]))
        if r[:5] == "Leave":
            _, id = r.split()
            answer.append("{}님이 나갔습니다.".format(name_by_id[id]))
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
a = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]