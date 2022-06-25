// https://leetcode.com/problems/cheapest-flights-within-k-stops/

var findCheapestPrice = function (n, flights, src, dst, k) {
  let prevArr = new Array(n).fill(Infinity);
  let currentArr = new Array(n).fill(Infinity);
  prevArr[src] = 0;
  currentArr[src] = 0;
  for (let i = 0; i < k + 1; i++) {
    for (let [from, to, price] of flights) {
      if (
        price + prevArr[from] < prevArr[to] &&
        price + prevArr[from] < currentArr[to]
      ) {
        currentArr[to] = price + prevArr[from];
      }
    }
    prevArr = [...currentArr];
  }
  return currentArr[dst] === Infinity ? -1 : currentArr[dst];
};
