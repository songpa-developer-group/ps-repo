// https://leetcode.com/problems/min-cost-to-connect-all-points/

var minCostConnectPoints = function (points) {
  let d = new Map();
  points.forEach((x, i) => (i == 0 ? d.set(x, 0) : d.set(x, Infinity)));
  //   console.log(d);

  let res = 0;
  while (d.size != 0) {
    let a;
    let mind = Infinity;
    for (let [p, dis] of d) {
      dis < mind ? ([a, mind] = [p, dis]) : null;
    }
    res += mind;
    d.delete(a);
    for (let [p] of d) {
      d.set(
        p,
        Math.min(d.get(p), Math.abs(p[0] - a[0]) + Math.abs(p[1] - a[1]))
      );
    }
  }
  //   console.log(res);
  return res;
};

minCostConnectPoints([
  [0, 0],
  [2, 2],
  [3, 10],
  [5, 2],
  [7, 0],
]);
