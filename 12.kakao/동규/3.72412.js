// https://programmers.co.kr/learn/courses/30/lessons/72412/

// 이분 탐색/ 해당 값이 어느 인덱스에 있을지를 탐색하여 결과를 반환
const binarySearch = (arr, target) => {
  let left = 0;
  let right = arr.length - 1;
  let mid = Math.floor((left + right) / 2);
  while (left <= right) {
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;

    mid = Math.floor((left + right) / 2);
  }
  // 기준이 되는 인덱스는 여기서 나온 값보다 항상 1이 더++
  return mid + 1;
};

const getInfos = (info) => {
  const infos = {}; // 유저정보 state
  info.forEach((infoString) => {
    const arr = infoString.split(" ");
    const score = parseInt(arr.pop());
    const key = arr.join(""); // key ex) javabackendjuniorpizza
    if (infos[key]) infos[key].push(score);
    else infos[key] = [score]; // score 배열형태 ex) [150]
  });
  // 다 처리된 이후에 각 키의 점수 배열을 정렬
  for (const key in infos) {
    infos[key].sort((a, b) => a - b);
  }
  return infos;
};

const getResult = (infos, query, score) => {
  const infosKey = Object.keys(infos);
  return infosKey
    .filter((key) => query.every((v) => key.includes(v)))
    .reduce(
      (acc, key) => acc + infos[key].length - binarySearch(infos[key], score),
      0
    );
};

const solution = (info, query) => {
  let answer = [];
  const infos = getInfos(info);
  query
    .map((q) => q.split(/ and | |-/i).filter((v) => v !== ""))
    .forEach((query) => {
      const score = query.pop();
      const result = getResult(infos, query, score);
      answer.push(result);
    });
  return answer;
};
