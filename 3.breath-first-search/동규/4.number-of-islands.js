function numIslands(grid) {
  const m = grid.length;
  const n = grid[0].length;
  let res = 0;

  const dfs = (x, y) => {
    if (x < 0 || x > m - 1 || y < 0 || y > n - 1) return;

    if (grid[x][y] === "1") {
      grid[x][y] = "visited";

      dfs(x - 1, y);
      dfs(x, y - 1);
      dfs(x + 1, y);
      dfs(x, y + 1);
      return true;
    }
    return false;
  };

  [...Array(m).keys()].forEach((i) => {
    [...Array(n).keys()].forEach((j) => {
      if (dfs(i, j) === true) res += 1;
    });
  });

  return res;
}
