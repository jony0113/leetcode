#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    '''
    给你两个只包含 1 到 9 之间数字的数组 nums1 和 nums2 ，
    每个数组中的元素 互不相同 ，请你返回 最小 的数字，
    两个数组都 至少 包含这个数字的某个数位。
    '''
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in nums1:
            if i in nums2:
                return i
                
        m1 = nums1[0]
        m2 = nums2[0]
        
        if m1 > m2 :
            m1,m2 = m2,m1
            
        return m1*10 + m2