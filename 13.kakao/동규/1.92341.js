// https://school.programmers.co.kr/learn/courses/30/lessons/92341/

function solution(fees, records) {
  let answer = [];
  let recordsArr = [];
  for (let i = 0; i < records.length; i++) {
    let current = records[i].split(" ");
    recordsArr.push(current);
  }

  recordsArr.sort((a, b) => {
    if (a[1] === b[1]) {
      return a[0] - b[0];
    }
    return a[1] - b[1];
  });

  let previousTime = 0;
  let totalCostTime = 0;

  while (recordsArr.length) {
    let current = recordsArr.shift();
    let time = current[0].split(":");
    let totalTime = Number(time[0]) * 60 + Number(time[1]);
    if (recordsArr.length && recordsArr[0][1] === current[1]) {
      if (current[2] === "IN") {
        previousTime = totalTime;
      } else {
        let usedTime = totalTime - previousTime;
        totalCostTime += usedTime;
      }
    } else {
      if (current[2] === "IN") {
        let usedTime = 1439 - totalTime;
        totalCostTime += usedTime;
      } else {
        let usedTime = totalTime - previousTime;
        totalCostTime += usedTime;
      }
      if (totalCostTime <= fees[0]) {
        answer.push(fees[1]);
      } else {
        let cost =
          fees[1] + Math.ceil((totalCostTime - fees[0]) / fees[2]) * fees[3];
        answer.push(cost);
      }
      totalCostTime = 0;
    }
  }

  return answer;
}
