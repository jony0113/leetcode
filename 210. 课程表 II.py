#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 210. 课程表 II.py
Author: fangeng
Date: 2020/5/17 19:23
"""
import collections


class Solution:
    """
    现在你总共有 n 门课需要选，记为 0 到 n-1。
    在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，
    我们用一个匹配来表示他们: [0,1]
    给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
    可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。
    """

    def findOrder(self, numCourses: int, prerequisites: 'List[List[int]]') -> 'List[int]':
        # 存储每门课程的入度
        in_edge = [0] * numCourses

        # 存储每门课依赖的课程
        depends = collections.defaultdict(list)

        ans = []

        for back_course, pre_course in prerequisites:
            depends[pre_course].append(back_course)
            in_edge[back_course] += 1

        queue = [x for x in range(numCourses) if in_edge[x] == 0]

        while queue:
            course = queue.pop(0)
            ans.append(course)

            for i in depends[course]:
                # 该课程依赖的课程减少一个
                in_edge[i] -= 1
                if in_edge[i] == 0:
                    queue.append(i)

        if len(ans) != numCourses:
            return []
        return ans
