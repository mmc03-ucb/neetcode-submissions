"""
we need to keep track of the following
which user follows whom: {followerId: followeeId} # every user follows themselves
posts of each user: {userId: [(tweetId, timeStamp)]} use queues to pop out left when over 10

when getNewsFeed is called
    newsFeed = []
    for followeeId in follows[followerId]:
        for tweetId in tweets[followeeId]:
            heapq.heappush(newsFeed, (timeStamp, tweedId))
            if len(newsFeed) > 10:
                heapq.heappop(newsFeed)
    
    return [tid for _, tid in heapq.heappop(newsFeed)]
"""
class Twitter:

    def __init__(self):
        self.timeStamp = 1
        self.follows = defaultdict(set) # {followerId: followeeId}
        self.tweets = defaultdict(deque) # {userId: queue}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follows:
            self.follows[userId].add(userId)
        
        if userId not in self.tweets:
            self.tweets[userId] = deque()
        
        q = self.tweets[userId]
        q.append((self.timeStamp, tweetId))
        if len(q) > 10:
            q.popleft()

        self.timeStamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        for followeeId in self.follows[userId]:
            for timeStamp, tweetId in self.tweets[followeeId]:
                heapq.heappush(newsFeed, (timeStamp, tweetId))
                if len(newsFeed) > 10:
                    heapq.heappop(newsFeed)
        
        output = []
        while newsFeed:
            output.append(heapq.heappop(newsFeed)[1])
        
        return output[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        userId = followerId
        if userId not in self.follows:
            self.follows[userId].add(userId)
        self.follows[userId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        userId = followerId
        if userId not in self.follows:
            self.follows[userId].add(userId)

        self.follows[followerId].discard(followeeId)
        
