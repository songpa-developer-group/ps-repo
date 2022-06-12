# https://leetcode.com/problems/min-cost-to-connect-all-points/

import heapq
from typing import List


class KruskalsAlgorithm:
    def __init__(self, size: int) -> None:
        self.parent = [0] * size

        # 각 정점이 포함된 그래프가 어디인지 저장
        for i in range(size):
            self.parent[i] = i

    def findParent(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionParent(self, node1: int, node2: int) -> bool:
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        self.parent[parent2] = parent1


class KruskalsSolution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        len_points = len(points)
        edges = []

        for curr_node in range(len_points):
            for next_node in range(curr_node + 1, len_points):
                distance = abs(points[curr_node][0] - points[next_node][0]) + \
                    abs(points[curr_node][1] - points[next_node][1])
                edges.append((distance, curr_node, next_node))

        edges.sort()

        mst = KruskalsAlgorithm(len_points)
        mst_cnt = 0
        edges_used = 0

        while True:
            for distance, node1, node2 in edges:
                if edges_used == len_points - 1:
                    break
                if mst.findParent(node1) != mst.findParent(node2):
                    mst.unionParent(node1, node2)
                    mst_cnt += distance
                    edges_used += 1
            return mst_cnt


##################################################################

class PrimSolution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        len_points = len(points)

        # Min-heap to store minimum weight edge at top.
        heap = [(0, 0)]

        # Track nodes which are included in MST.
        edges = [False] * len_points

        mst_cnt = 0
        edges_used = 0

        while edges_used < len_points:
            distance, curr_node = heapq.heappop(heap)

            # If node was already included in MST we will discard this edge.
            if edges[curr_node]:
                continue

            edges[curr_node] = True
            mst_cnt += distance
            edges_used += 1

            for next_node in range(len_points):
                # If next node is not in MST, then edge from curr node
                # to next node can be pushed in the priority queue.
                if not edges[next_node]:
                    next_distance = abs(points[curr_node][0] - points[next_node][0]) +\
                        abs(points[curr_node][1] - points[next_node][1])

                    heapq.heappush(heap, (next_distance, next_node))

        return mst_cnt


print(KruskalsSolution().minCostConnectPoints(
    [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))


print(PrimSolution().minCostConnectPoints(
    [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
