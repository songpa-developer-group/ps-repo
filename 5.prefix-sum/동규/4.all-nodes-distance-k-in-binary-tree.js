// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

const distanceK = function (root, target, K) {
  let graph = {};

  const dfs = function BinaryTreeIntoGraph(node, parent) {
    if (node === null) return; // ending 조건 : null 일 때 그냥 return
    let neighbor = [parent, null, null]; // 초기화
    if (node.left) {
      neighbor[1] = node.left.val; // 있으면 값 갱신
      dfs(node.left, node.val); // 왼쪽 노드에 대해서도 dfs
    }
    if (node.right) {
      neighbor[2] = node.right.val; // 있으면 값 갱신
      dfs(node.right, node.val); // 오른쪽 노드에 대해서도 dfs
    }
    graph[node.val] = neighbor; // graph 에 저장 [parent, left.value, right.value];
  };
  dfs(root, null);
  console.log(graph);

  // Graph BFS Algorithm : using [Queue:unvisited and Set:visited]
  const unvisitedQueue = [{ value: target.val, distance: 0 }];
  const visitedSet = new Set();
  const result = [];

  while (unvisitedQueue.length > 0) {
    const { value, distance } = unvisitedQueue.shift(); // 현재 탐색할 노드 Queue 에서 꺼냄

    if (visitedSet.has(value)) continue; // 미리 봤다면, 아래 과정을 거칠 필요가 없음
    visitedSet.add(value); // 먼저 set 에 넣어준다. 다음번에 반복을 피하기 위해서

    if (distance === K && value !== null) result.push(value); // 거리가 같고, null 이 아니라면 push
    if (distance < K && value !== null) {
      // 아직 거리에 도달하지 못 했다면, 탐색을 계속한다.
      // 탐색을 지속한다는 의미는 queue 에다가 탐색 할 애들을 넣어주는 것
      const neighbor = graph[value]; // neighbor array [parent, left, right];
      neighbor.forEach((each) =>
        unvisitedQueue.push({ value: each, distance: distance + 1 })
      ); // distance 1을 증가시킨다.
    }
  }
  return result;
};
