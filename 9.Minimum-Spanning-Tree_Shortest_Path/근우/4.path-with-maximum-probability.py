## https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        graph = defaultdict(dict)

        for edge, prob in zip(edges, succProb):
            graph[edge[0]][edge[1]] = prob
            graph[edge[1]][edge[0]] = prob

        queue = [[-1, start]]
        visited = set()

        while queue:
            prob, node = heapq.heappop(queue)

            if node == end:
                return -prob

            visited.add(node)

            for next_node, next_prob in graph[node].items():
                if next_node in visited:
                    continue

                heapq.heappush(queue, [prob * next_prob, next_node])

        return 0