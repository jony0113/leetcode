#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
    """

    def subarraysDivByK(self, A: 'List[int]', K: int) -> int:
        record = {0: 1}

        _sum, ans = 0, 0
        for a in A:
            _sum += a
            mod = _sum % K
            same = record.get(mod, 0)
            ans += same
            record[mod] = same + 1
        return ans
