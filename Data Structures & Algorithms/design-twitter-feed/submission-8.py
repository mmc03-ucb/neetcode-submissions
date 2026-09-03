class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(deque) #userId -> (timestamp, tweetId)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following[userId]:
            self.following[userId].add(userId)
        feed = []
        for user in self.following[userId]:
            for time, tweet in self.tweets[user]:
                heapq.heappush(feed, (time, tweet))
                if len(feed) > 10:
                    heapq.heappop(feed)
        
        output = []
        while feed:
            output.append(heapq.heappop(feed)[1])
        
        return output[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
