from typing import List

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return answer

        c = len(matrix)
        r = len(matrix[0])
        i, j = 0, 0
        up_right = True
        for _ in range(c * r):
            answer.append(matrix[i][j])

            if up_right:
                i -= 1
                j += 1
            else:
                i += 1
                j -= 1

            if i >= c:
                i -= 1
                j += 2
                up_right = True
            elif j >= r:
                i += 2
                j -= 1
                up_right = False

            if i < 0:
                i = 0
                up_right = False
            elif j < 0:
                j = 0
                up_right = True
        return answer

if __name__ == "__main__":
    mat = [[1,2],[3,4]]
    print(Solution().findDiagonalOrder(mat))