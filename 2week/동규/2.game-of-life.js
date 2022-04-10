// 살아있는 세포
//  - 이웃이 3 명 초과면 사망
//  - 이웃이 2, 3 명이면 현재 상태 그대로 진행
//  - 이웃이 2 명 미만이면 사망
// 죽은 세포
//  - 이웃이 3 명이면 생존
//  - 그 외에는 현재 상태 그대로

function gameOfLife(board) {
  const n = board.length;
  const m = board[0].length;

  var tmp = [];
  for (var i = 0; i < n; i++) tmp[i] = [];

  var dir = [
    [1, 0],
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1],
  ];

  for (var i = 0; i < n; i++)
    for (var j = 0; j < m; j++) {
      var item = board[i][j];
      var liveNeighbours = 0;
      for (var k = 0; k < 8; k++) {
        var x = i + dir[k][0];
        var y = j + dir[k][1];
        if (x < 0 || x >= n || y < 0 || y >= m) continue;
        liveNeighbours += board[x][y];
      }

      if (item) {
        if (liveNeighbours === 2 || liveNeighbours === 3) tmp[i][j] = 1;
        else tmp[i][j] = 0;
      } else {
        if (liveNeighbours === 3) tmp[i][j] = 1;
        else tmp[i][j] = 0;
      }
    }

  for (var i = 0; i < n; i++)
    for (var j = 0; j < m; j++) board[i][j] = tmp[i][j];
}
