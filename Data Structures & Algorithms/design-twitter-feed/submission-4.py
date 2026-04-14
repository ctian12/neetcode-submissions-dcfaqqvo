class Twitter:

    def __init__(self):
        self.following = defaultdict()
        self.findUser = defaultdict()
        self.allTweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.findUser[tweetId] = userId
        self.allTweets.append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for i in range(len(self.allTweets) - 1, -1, -1):
            tweet = self.allTweets[i]
            user = self.findUser[tweet]
            if user == userId:
                feed.append(tweet)
            if userId in self.following and user in self.following[userId]:
                feed.append(tweet)
            if len(feed) == 10:
                return feed
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.following:
            self.following[followerId] = [followeeId]
        elif followeeId in self.following[followerId]:
            return
        else:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
