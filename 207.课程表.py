#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections
from typing import List

class Solution:
    '''
    你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
    在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，
    其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程ai则 必须 先学习课程bi 。
    例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
    请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        depends_num = [0] * numCourses

        depends = collections.defaultdict(list)
        
        for back, pre in prerequisites:
            depends[pre].append(back)
            depends_num[back] += 1
        
        queue = [ x for x in range(numCourses) if depends_num[x] == 0 ]

        satisfy = 0

        while queue:
            course = queue.pop()
            satisfy += 1

            for i in depends[course]:
                depends_num[i] -= 1
                if depends_num[i] == 0:
                    queue.append(i)
        
        if satisfy == numCourses:
            return True
        return False