#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List
import math

class Solution:
    '''
    给你一个整数数组 ranks ，表示一些机械工的 能力值 。
    ranksi 是第 i 位机械工的能力值。能力值为 r 的机械工
    可以在 r * n2 分钟内修好 n 辆车。

    同时给你一个整数 cars ，表示总共需要修理的汽车数目。
    请你返回修理所有汽车 最少 需要多少时间。
    
    注意：所有机械工可以同时修理汽车。
    '''
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()
        begin = 1
        end = ranks[0]*cars*cars
        
        while begin<end:
            hours = int((begin + end) / 2)
            if self.can(ranks,hours,cars):
                end = hours
            else:
                begin = hours+1
        return begin
    
    
    def can(self, ranks: List[int], hours:int, cars:int) -> bool:
        total = 0
        for rank in ranks:
            total += int(math.sqrt(int(hours/rank)))
            if total >= cars:
                return True
        return False