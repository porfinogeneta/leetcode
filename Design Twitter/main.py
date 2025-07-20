class Twitter(object):

    def __init__(self):
        self.usersMap = defaultdict(set)  # użytkownicy, mapa user: kogo obserwuje
        self.usersPosts = defaultdict(list)  # posty, mapa user: [counter, postId]
        self.counter = 0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        idea: dodajemy do listy postów posta i zwiększamy counter,
        żeby odróżnić czasy dodawania pozostałych postów
        """
        self.usersPosts[userId].append([self.counter, tweetId])
        self.counter += 1

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        idea: przechodzimy po followerach i dodajemy ich posty na kopiec maksymalny,
        potem wybieramy 10 elementów z ostatnimi wartościami countera, ja wrzucimy dany element usera,
        to wrzucamy jeden jego wcześniejszy post
        O(10*log(k) + k) -> k to liczba followowanych przez userId osób
        """
        res = []
        self.usersMap[userId].add(userId)  # chcemy też uwzględnić posty tego konkretnego usera
        maxHeap = []
        for followee in self.usersMap[userId]:
            if followee in self.usersPosts:
                index = len(self.usersPosts[followee]) - 1
                counter, postId = self.usersPosts[followee][index]
                maxHeap.append([-counter, postId, followee, index - 1])

        heapq.heapify(maxHeap)

        while maxHeap and len(res) < 10:
            counter, postId, followee, index = heapq.heappop(maxHeap)
            res.append(postId)
            # jeśli dany użytkownik ma jeszcze jakieś posty, to dodajemy je
            if index >= 0:
                # bierzemy posta od użytkownika
                counter, postId = self.usersPosts[followee][index]
                heapq.heappush(maxHeap, [-counter, postId, followee, index - 1])

        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        idea: dodajemy użytkownikowi jakiegoś followera, używamy set, żeby add i remove były w O(1)
        """
        self.usersMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if self.usersMap[followerId]:
            self.usersMap[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)