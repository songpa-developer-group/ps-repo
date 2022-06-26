// https://leetcode.com/problems/path-with-maximum-probability/

var maxProbability = function (n, edges, succProb, start, end) {
  const probabilities = new Array(n).fill(0);
  probabilities[start] = 1;

  for (let i = 0; i < n; i += 1) {
    let betterPathFound = false;
    for (let j = 0; j < edges.length; j += 1) {
      const [from, to] = edges[j];
      if (!probabilities[from] && !probabilities[to]) continue;

      const edgeProb = succProb[j];
      const maxProb =
        Math.max(probabilities[from], probabilities[to]) * edgeProb;
      if (maxProb > probabilities[to]) {
        probabilities[to] = maxProb;
        betterPathFound = true;
      }
      if (maxProb > probabilities[from]) {
        probabilities[from] = maxProb;
        betterPathFound = true;
      }
    }
    if (!betterPathFound) break;
  }
  return probabilities[end];
};
