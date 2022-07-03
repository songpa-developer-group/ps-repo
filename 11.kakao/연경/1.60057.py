## https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):

    answer = len(s)
    size = len(s)

    for i in range(1, size):
        tmp = []
        j = 0
        last = None
        while j < size:

            if last is None:
                last = s[j:j + i]
                tmp.append(1)
            else:
                if last == s[j:j + i]:
                    tmp[-1] += 1
                else:
                    tmp.append(last)
                    last = s[j:j + i]
                    tmp.append(1)
            j += i

        tmp.append(last)
        length = 0
        for c in tmp:
            if c != 1:
                length += len(str(c))
        answer = min(length, answer)
    return answer

if __name__ == "__main__":
    s = "xababcdcdababcdcd"
    print(solution(s))