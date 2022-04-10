from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []

        ch = [[1 for _ in range(len(matrix[0]))]  for _ in range(len(matrix))]
        i, j = 0, -1
        count = len(matrix[0]) * len(matrix)
        d = 'e'
        while count > 0:
            if d == 'e':
                if 0 <= i < len(matrix) and 0 <= j+1 < len(matrix[0]) and ch[i][j+1] == 1:
                    j += 1
                    answer.append(matrix[i][j])
                    ch[i][j] = 0
                    count -= 1
                else:
                    d = 's'
            elif d == 's':
                if 0 <= i+1 < len(matrix) and 0 <= j < len(matrix[0]) and ch[i+1][j] == 1:
                    i += 1
                    answer.append(matrix[i][j])
                    ch[i][j] = 0
                    count -= 1
                else:
                    d = 'w'
            elif d == 'w':
                if 0 <= i < len(matrix) and 0 <= j-1 < len(matrix[0]) and ch[i][j-1] == 1:
                    j -= 1
                    answer.append(matrix[i][j])
                    ch[i][j] = 0
                    count -= 1
                else:
                    d = 'n'
            elif d == 'n':
                if 0 <= i-1 < len(matrix) and 0 <= j < len(matrix[0]) and ch[i-1][j] == 1:
                    i -= 1
                    answer.append(matrix[i][j])
                    ch[i][j] = 0
                    count -= 1
                else:
                    d = 'e'
        return answer

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(matrix))