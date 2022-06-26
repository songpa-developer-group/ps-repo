// https://programmers.co.kr/learn/courses/30/lessons/72413

// 모든 정점에서 각각의 정점으로 향하는 최단 경로

function solution(n, s, a, b, fares) {
  const board = new Array(n).fill().map((_) => new Array(n).fill(Infinity));

  for (let i = 0; i < n; i++) board[i][i] = 0;

  // x에서 y로 향하는 최단경로(최소요금) = weight
  fares.forEach((pos) => {
    const [x, y, weight] = pos;
    board[x - 1][y - 1] = weight;
    board[y - 1][x - 1] = weight;
  });

  // k 경유노드, i 시작노드, j 도착노드
  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (board[i][j] > board[i][k] + board[k][j])
          board[i][j] = board[i][k] + board[k][j];
      }
    }
  }

  // 기본 answer = 두 사람이 따로 가는 경우
  let answer = board[s - 1][a - 1] + board[s - 1][b - 1];

  // 시작점에서 합승지점까지 + 합승지점에서 a까지 + 합승지점에서 b까지
  for (let i = 0; i < n; i++) {
    const shortest = board[s - 1][i] + board[i][a - 1] + board[i][b - 1];
    answer = Math.min(answer, shortest);
  }

  return answer;
}
