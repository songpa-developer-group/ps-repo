## https://school.programmers.co.kr/learn/courses/30/lessons/92335/
# 9:42



# n =11231
def _make_k_binary(n , k):
    digit = 0
    result = ''
    while(n>k):
        n, remain =divmod(n,k)
        result = str(remain) + result
        digit+=1
    return str(n) + result
def check_primary(n):
    return n!=1 and all([n%k != 0 for k in range(2,n)])
def solution(n, k):

    binary_map = {

    }
    binary_num = _make_k_binary(n,k)
    filtered_zero = list(binary_num.split('0'))
    filtered_primary = list(filter(lambda a: a!= '' and check_primary(int(a)),filtered_zero))
    return len(filtered_primary)

# assert solution(437674,	3)  ==	3
assert solution(110011,	10) ==	2