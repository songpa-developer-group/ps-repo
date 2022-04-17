// dp(n) = min(dp(n-X)+1)  => X는 n을 넘기지 않는 완전 제곱수
// dp(13)은 9를 완전제곱수로 선택 후 dp(13-9)+1 과 같이 표현

function numSquares(n) {
  const dp = new Array(n + 1).fill(Infinity);
  dp[0] = 0;

  for (let i = 1; i <= n; i++) {
    let p = 1;
    while (p ** 2 <= i) {
      dp[i] = Math.min(dp[i], dp[i - p ** 2] + 1);
      p += 1;
    }
  }
  return dp[n];
}
