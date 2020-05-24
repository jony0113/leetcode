#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 地图分析.py
Author: fangeng
Date: 2020/3/29 21:10
"""
import queue


class Solution:
    """
    题目：
    你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。
    其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？
    请返回该海洋区域到离它最近的陆地区域的距离。
    我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：
    (x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
    如果我们的地图上只有陆地或者海洋，请返回 -1。

    [[1,0,1],[0,0,0],[1,0,1]] -> 2
    [[1,0,0],[0,0,0],[0,0,0]] -> 4
    """

    def maxDistance(self, grid: 'List[List[int]]') -> int:
        if not grid or len(grid) < 2:
            return -1
        distance = -1
        length = len(grid)

        for i in range(0, length):
            for j in range(0, length):
                if grid[i][j] == 0:
                    ds = self.get_min(grid, i, j, length)
                    if ds == -1:
                        return -1

                    if ds > distance:
                        distance = ds

        return distance

    def get_min(self, grid, x, y, length):
        already = set()
        q = [(x, y)]
        ds = 0
        flag = False
        now = 1
        after = 0
        s = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while len(q) > 0:
            i, j = q.pop(0)
            if grid[i][j] == 1:
                flag = True
                break
            now -= 1
            p = [(i + m, j + n) for (m, n) in s if 0 <= i + m < length and 0 <= j + n < length
                 and not (i + m, j + n) in already]
            already.update(p)
            q.extend(p)
            after += len(p)
            if now == 0:
                ds += 1
                now = after
                after = 0

        if flag:
            return ds
        else:
            return -1

    def maxDistance1(self, grid: 'List[List[int]]') -> int:
        """
        利用Dijkstra，使用优先队列，
        存储当前节点到海洋的最近的距离
        """

        if not grid or len(grid) < 2:
            return -1
        length = len(grid)
        # 初始化所有节点都是海洋
        distance = [[1000] * length for _ in range(0, length)]
        # 插入到最近的陆地的距离，以及节点位置
        q = queue.PriorityQueue()
        dealt = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(0, length):
            for j in range(0, length):
                # 当前节点是陆地时，更新distance数组，放入队列
                if grid[i][j] == 1:
                    distance[i][j] = 0
                    q.put((0, i, j))

        while not q.empty():
            # 当前节点
            d, i, j = q.get()
            # 临近的节点
            p = [(i + m, j + n) for (m, n) in dealt if 0 <= i + m < length and 0 <= j + n < length]
            for x, y in p:
                # 临近节点通过当前节点到达陆地的距离比原来存储的值小时，更新临近节点到达陆地的值，并放入队列
                if d + 1 < distance[x][y]:
                    distance[x][y] = d + 1
                    q.put((d + 1, x, y))

        res = -1
        for i in range(0, length):
            for j in range(0, length):
                # 排除全部为陆地和全部为海洋的情况
                if 0 < distance[i][j] < 1000:
                    res = max(res, distance[i][j])

        return res
