#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，
    判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

    说明：
        拆分时可以重复使用字典中的单词。
        你可以假设字典中没有重复的单词。
    """

    def wordBreak(self, s: str, wordDict: 'List[str]') -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[n]
