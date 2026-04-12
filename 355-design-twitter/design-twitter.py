class Twitter:

    def __init__(self):
        self.d = defaultdict(list) #user : tweet
        self.l = defaultdict(set) #user : following
        self.o = [] #tweet order

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.o.append(tweetId)
        self.d[userId].append(tweetId)
        self.l[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        f = self.l[userId]
        tweets = {}
        for i in f:
           for j in self.d[i]:
                tweets[j] = self.o.index(j)
        sorted_tweets = dict(sorted(tweets.items(), key = lambda x : x[-1], reverse = True))
        return list(sorted_tweets.keys())[:10]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.l[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.l[followerId]:
            self.l[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)