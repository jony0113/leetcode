#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    """
    给定一个经过编码的字符串，返回它解码后的字符串。
    编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
    你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
    此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
    """

    def decodeString(self, s: str) -> str:
        stack = list()
        length = len(s)
        i = 0
        while i < length:
            ch = s[i]
            if ch.isdigit():
                num = int(ch)
                i += 1
                while s[i].isdigit():
                    num = (num * 10 + int(s[i]))
                    i += 1
                stack.append(num)
            elif ch == '[' or ch.isalpha():
                stack.append(ch)
                i += 1
            elif ch == ']':
                temp = ''
                while stack[-1] != '[':
                    temp = stack.pop() + temp
                stack.pop()
                num = stack.pop()
                stack.append(temp * num)
                i += 1
        return "".join(stack)
