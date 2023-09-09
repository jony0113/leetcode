#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。
    例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），
    该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。
    编写一个方法判断value字符串是否匹配pattern字符串。
    """

    def patternMatching(self, pattern: str, value: str) -> bool:
        if not value:
            return len(pattern) in [0, 1]

        if not pattern:
            return False

        def match(len_a, len_b):
            a = ""
            b = ""
            index = 0
            for s in pattern:
                if s == 'a':
                    temp_a = value[index:index + len_a]
                    index += len_a
                    if a == "":
                        a = temp_a
                    if temp_a != a:
                        return False
                if s == 'b':
                    temp_b = value[index:index + len_b]
                    index += len_b
                    if b == "":
                        b = temp_b
                    if temp_b != b:
                        return False
            if a == b:
                return False
            return True

        count_a, count_b = 0, 0
        for s in pattern:
            if s == 'a':
                count_a += 1
            elif s == 'b':
                count_b += 1
            else:
                return False

        len_value = len(value)
        if count_a == 0:
            if count_b * (len_value // count_b) == len_value and match(0, len_value // count_b):
                return True
            else:
                return False

        max_a_len = (len_value // count_a) + 1
        if count_b == 0:
            if count_a * (max_a_len - 1) == len_value and match(max_a_len - 1, 0):
                return True
            else:
                return False

        for len_a in range(max_a_len):
            len_b = (len_value - len_a * count_a) // count_b
            if len_b * count_b + len_a * count_a == len_value and match(len_a, len_b):
                return True

        return False
