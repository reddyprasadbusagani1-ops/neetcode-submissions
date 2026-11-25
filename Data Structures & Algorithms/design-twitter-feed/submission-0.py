import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        users = self.following[userId] | {userId}
        heap = []

        for uid in users:
            tweets = self.tweets[uid]

            if tweets:
                index = len(tweets) - 1
                time, tweetId = tweets[index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, uid, index)
                )

        result = []

        while heap and len(result) < 10:
            neg_time, tweetId, uid, index = heapq.heappop(heap)

            result.append(tweetId)

            if index > 0:
                index -= 1
                time, next_tweetId = self.tweets[uid][index]

                heapq.heappush(
                    heap,
                    (-time, next_tweetId, uid, index)
                )

        return result

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)