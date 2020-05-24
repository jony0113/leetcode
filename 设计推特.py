#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Desc:
File: 设计推特.py
Author: fangeng
Date: 2020/4/13 21:39
"""
import time


class Twitter:
    """
    题目：
    设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，
    能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

    postTweet(userId, tweetId): 创建一条新的推文
    getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。
    推文必须按照时间顺序由最近的开始排序。
    follow(followerId, followeeId): 关注一个用户
    unfollow(followerId, followeeId): 取消关注一个用户
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweet_list = {}
        self.follow_dict = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        tweets = self.tweet_list.get(userId, [])
        tweets.append((tweetId, time.time()))
        self.tweet_list[userId] = tweets

    def getNewsFeed(self, userId: int) -> 'List[int]':
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed
        must be posted by users who the user followed or by the user herself. Tweets must be
        ordered from most recent to least recent.
        """
        tweet_ids = [userId]
        tweet_ids.extend(self.follow_dict.get(userId, set()))
        tweets = []
        for tweet_id in tweet_ids:
            tweets.extend(self.tweet_list.get(tweet_id, []))
        tweets.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        followers = self.follow_dict.get(followerId, set())
        if followeeId not in followers:
            followers.add(followeeId)
            self.follow_dict[followerId] = followers

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        followers = self.follow_dict.get(followerId, set())
        if followeeId in followers:
            followers.remove(followeeId)
            self.follow_dict[followerId] = followers

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
