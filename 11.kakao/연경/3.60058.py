## https://programmers.co.kr/learn/courses/30/lessons/60058

def check(s):
    result = False

    stack = []
    for c in s:

        if stack:
            if stack[-1] == '(':
                if c == '(':
                    stack.append(c)
                else:
                    stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    return not stack


def recursive(p):

    if p == '':
        return p

    i = 0
    l, r = 0, 0
    while i < len(p):
        c = p[i]
        if c == '(':
            l += 1
        else:
            r += 1

        if l == r:
            break
        i += 1

    u = p[0:i + 1]
    v = p[i + 1:]
    if check(u):
        return u + recursive(v)
    else:
        tmp = ''.join(['(' if c == ')' else ')' for c in u[1:-1]])
        return '(' + recursive(v) + ')' + tmp

def solution(p):

    if check(p):
        return p
    else:
        return recursive(p)


if __name__ == "__main__":
    p = "()))((()"
    print(solution(p))
