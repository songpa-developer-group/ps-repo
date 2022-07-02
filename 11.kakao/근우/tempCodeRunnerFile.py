def solution(p):
    def devide_balanced(p):
        left_bracket = right_bracket = 0
        for i, c in enumerate(p):
            if c == '(':
                left_bracket+=1
            if c == ')':
                right_bracket+=1
            if left_bracket>0 and right_bracket>0 and left_bracket == right_bracket:
                return p[:i+1], p[i+1:]

    def check_correct_balanced_str(p):
        left_bracket_num = 0
        for i, c in enumerate(p):
            if c == '(':
                left_bracket_num+=1
            if c == ')':
                left_bracket_num-=1
            if left_bracket_num<0:
                return False
        return True

    def process(p):
        if check_correct_balanced_str(p):
            return p
        u, v = devide_balanced(p)
        if check_correct_balanced_str(u):
            return u + process(v)
        else:
            v = "(" + process(v) + ")"
            u = u[1:-1]
            map(lambda a: ')' if a=='(' else '(',u)
            return v + u
    return process(p)