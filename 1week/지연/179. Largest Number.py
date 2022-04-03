class LargerNumKey(str):
    # 스페셜 메소드 -> 인스턴스(객체) 생성 시 사용할 수 있는 메소드로 인스턴스 사이의 비교 연산자 (<, <=, >, >=, ==. != 등) 을 사용할 때 호출하는 비교 메서드 등이 있다.
    # __lt__ : less than 비교 연산자
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


print(Solution().largestNumber([3, 30, 34, 5, 9]))
