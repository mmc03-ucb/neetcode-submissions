class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        q = self.tweets[userId]
        q.append((self.t, tweetId))

        if len(q) > 10:
            q.popleft()

        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.follows[userId]:
            self.follows[userId].add(userId)

        feed = []
        for uid in self.follows[userId]:
            for time, tid in self.tweets[uid]:
                heapq.heappush(feed, (time, tid))
                if len(feed) > 10:
                    heapq.heappop(feed)
        
        output = []
        while feed:
            output.append(heapq.heappop(feed)[1])
        
        return output[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
