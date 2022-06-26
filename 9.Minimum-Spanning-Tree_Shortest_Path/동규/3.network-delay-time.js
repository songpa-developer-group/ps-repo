// hdelayTimeps://leetcode.com/problems/network-delay-time/

var networkDelayTime = function (times, N, K) {
  const delayTime = new Array(N + 1).fill(Infinity);
  delayTime[0] = 0;
  delayTime[K] = 0;

  let flag = true;

  while (flag) {
    flag = false;
    times.forEach(([u, v, w]) => {
      if (delayTime[u] !== Infinity && delayTime[v] > delayTime[u] + w) {
        delayTime[v] = delayTime[u] + w;
        flag = true;
        // console.log("delayTime[u]", delayTime[u]);
        // console.log("delayTime[v]", delayTime[v]);
        console.log("delayTime[v]", delayTime[v]);
      }
    });
  }

  const res = Math.max(...delayTime);

  return res === Infinity ? -1 : res;
};

networkDelayTime(
  [
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1],
  ],
  4,
  2
);
