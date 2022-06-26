const { dir } = require("console");
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const NM = input.shift().split(" ");
const N = Number(NM.shift());
const M = Number(NM.shift());
const init = input.shift().split(" ");
let curY = Number(init[0]);
let curX = Number(init[1]);
let curDiraction = Number(init[2]);
const MAX = 50;
let answer = 0;

// 북 동 남 서
let diraction = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];

let room = new Array(MAX);
for (let i = 0; i < MAX; i++) {
  room[i] = new Array(MAX).fill(1);
}
for (let i = 0; i < N; i++) {
  let temp = input.shift().split(" ");
  for (let j = 0; j < M; j++) {
    room[i][j] = Number(temp[j]);
  }
}

let visited = new Array(MAX);
for (let i = 0; i < MAX; i++) {
  visited[i] = new Array(MAX).fill(false);
}

let test = 1;
while (1) {
  // 1단계.
  if (!visited[curY][curX]) {
    visited[curY][curX] = true;
    answer++;
    //console.log('stage1');
  }

  // 2단계 setting
  let nextDiraction = curDiraction - 1;
  if (curDiraction - 1 < 0) nextDiraction = 3;
  let nextY = curY + diraction[nextDiraction][0];
  let nextX = curX + diraction[nextDiraction][1];

  // 2단계.
  // step 1.  왼쪽 방향에 청소하지 않은 공간이 존재하면, 그 방향으로 회전하고 다음 한 칸을 전진하고 1번부터 진행한다.
  if (room[nextY][nextX] === 0 && !visited[nextY][nextX]) {
    // 회전한다.
    curDiraction--;
    if (curDiraction < 0) curDiraction = 3;
    // 회전한 방향으로 한 칸을 전진한다.
    curY = nextY;
    curX = nextX;
    //console.log('step1');
    continue;
  }

  // step 3.  네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다. 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
  let check = 0;
  for (let next = 0; next < 4; next++) {
    let nextY2 = curY + diraction[next][0];
    let nextX2 = curX + diraction[next][1];
    if (room[nextY2][nextX2] === 1 || visited[nextY2][nextX2]) {
      check++;
    }
  }

  if (check === 4) {
    // 북쪽
    if (curDiraction === 0) {
      if (room[curY + 1][curX] === 1) {
        //console.log('north');
        break;
      }
      curY++;
      continue;
    }
    // 동
    if (curDiraction === 1) {
      if (room[curY][curX - 1] === 1) {
        //console.log('east');
        break;
      }
      curX--;
      continue;
    }
    // 남
    if (curDiraction === 2) {
      if (room[curY - 1][curX] === 1) {
        //console.log('south');
        break;
      }
      curY--;
      continue;
    }
    // 서
    if (curDiraction === 3) {
      if (room[curY][curX + 1] === 1) {
        //console.log('west');
        break;
      }
      curX++;
      continue;
    }
  }

  // step 2.
  if (room[nextY][nextX] === 1 || visited[nextY][nextX]) {
    //console.log('step2');
    curDiraction--;
    if (curDiraction < 0) curDiraction = 3;
    continue;
  }
}

console.log(answer);
