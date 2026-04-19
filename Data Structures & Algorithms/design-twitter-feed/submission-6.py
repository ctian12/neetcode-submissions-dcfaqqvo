class Twitter:

    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        out = []
        users = self.followMap[userId]
        users.add(userId)

        for user in users:
            if user in self.tweetMap:
                idx = len(self.tweetMap[user]) - 1
                heapq.heappush(heap, [self.tweetMap[user][idx][0], self.tweetMap[user][idx][1], user, idx - 1])
        
        while heap and len(out) < 10:
            count, tweetId, user, nextIdx = heapq.heappop(heap)
            out.append(tweetId)
            if nextIdx >= 0:
                heapq.heappush(heap, [self.tweetMap[user][nextIdx][0], self.tweetMap[user][nextIdx][1], user, nextIdx - 1])
        
        return out


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
