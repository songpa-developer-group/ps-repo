# https://www.acmicpc.net/problem/14503

class Robot:
    def __init__(self, y, x, d, map, N, M):
        self.map = map
        self.dy, self.dx = [-1, 0, 1, 0], [0, 1, 0, -1]
        self.pos = [y, x]
        self.direction = d
        self.is_visited = [[False for _ in range(M)] for _ in range(N)]
        self.clean_count = 0

    def operate(self):
        self._clean()
        first_dir = self.direction
        while 1:
            if self._is_left_cleanable():
                self._turn_left()
                self._go_straight()
                self._clean()
                first_dir = self.direction
            else:
                self._turn_left()

            if first_dir == self.direction:
                if self._is_wall_back():
                    return
                else:
                    self._go_back()

    def _is_wall_back(self):
        _back_direction = self.direction - \
            2 if self.direction >= 2 else self.direction + 4 - 2
        _back_block = [
            self.pos[0]+self.dy[_back_direction],
            self.pos[1]+self.dx[_back_direction],
        ]
        if self.map[_back_block[0]][_back_block[1]] == 1:
            return True
        return False

    def _go_straight(self):
        self.pos = [
            self.pos[0]+self.dy[self.direction],
            self.pos[1]+self.dx[self.direction],
        ]

    def _go_back(self):
        self.pos = [
            self.pos[0]-self.dy[self.direction],
            self.pos[1]-self.dx[self.direction],
        ]

    def _left_direction(self):
        return self.direction - 1 if self.direction > 0 else 3

    def _turn_left(self):
        self.direction = self._left_direction()

    def _clean(self):
        self.is_visited[self.pos[0]][self.pos[1]] = True
        self.clean_count += 1

    def _is_left_cleanable(self):
        _left_block = [
            self.pos[0] + self.dy[self._left_direction()],
            self.pos[1] + self.dx[self._left_direction()],
        ]
        if self.is_visited[_left_block[0]][_left_block[1]] or self.map[_left_block[0]][_left_block[1]] == 1:
            return False
        return True


N, M = map(int, input().split())
R, C, D = map(int, input().split())
_map = [list(map(int, input().split()))for _ in range(N)]
robot = Robot(R, C, D, _map, N, M)
robot.operate()
print(robot.clean_count)
