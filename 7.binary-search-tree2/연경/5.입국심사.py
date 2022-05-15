# https://programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    # 모든 사람이 심사를 받는데 걸리는 시간
    max_time = max(times) * n
    left, right = 1, max_time
    answer = right
    while left <= right:
        mid = (left + right) // 2

        total = 0
        for time in times:
            total += mid // time
        if total < n:
            left = mid + 1
        elif total >= n:
            right = mid - 1
            answer = min(answer, mid)

    return answer

if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times))
