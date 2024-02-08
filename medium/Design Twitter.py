""" 
    題意:   
        設計一個Twitter interface支援follow/unfollow以及貼文 , 
        同時可以讓特定使用者取回其關注的(他自己的貼文或follow的人的貼文)最新10篇貼文 
        
    思路:
        粗略來說我有兩個想法 , 
        1. maintain所有貼文的list,其順序就是自然的發文時間 , 同時更新每個user的follow list,
            當需要取貼文的時候 , 從list尾部開始找 ,找到10篇滿足條件的貼文
            worse case下每一次查詢都需要O(貼文數) , 因此不可行
        
        2. 每一個user都maintain其發文表 , 順序為這些user貼文的時間軸 , 並且也更新user的follow list
            當需要取貼文的時候 , 從這多組 follow list去找貼文
            worse case下查詢需要的次數為 O(follow者數) , 合理許多
        
"""
from typing import List 
class Twitter:

    def __init__(self):
        
        # record the following relation for every user
        self.record = dict()
        self.timmer = 1 

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        if userId in self.record : 
            self.record[userId]["posts"].append( (tweetId , self.timmer )) 

        else : 
            self.record[userId] = {
                "posts":[(tweetId , self.timmer )] , "follow":set()
            }
        
        self.timmer += 1 
        return 

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId in self.record : 
            self.record[followerId]["follow"].add(followeeId) 
        else : 
            self.record[followerId] = {
                "posts" : [] , "follow": {followeeId}
            }
        return 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followerId in self.record and followeeId in self.record[followerId]['follow']: 
            self.record[followerId]["follow"].remove(followeeId) 
        return             

    # 從userId中取出他所有的follower , 依照時間最早的一一選取
    def getNewsFeed(self, userId: int) -> List[int]:
        
        if not userId in self.record : return []

        stack = list() 
        totalPosts = len( self.record[userId]["posts"] ) 
        for follow in self.record[userId]['follow'] : 

            if not follow in self.record : continue

            totalPosts += len(self.record[follow]["posts"])

        
        # Recent 10 posts 
        while len(stack) <  min( 10 , totalPosts )  :  

            # keep the target  temporary  ( for pop from the record )
            user , time = (userId, self.record[userId]['posts'][-1][1]) if self.record[userId]['posts'] else (None , None )

            for follow in self.record[userId]["follow"] :    

                if not self.record[follow]['posts'] : continue 
                else : 

                    if user is None or self.record[follow]['posts'][-1][1] > time : 
                        user , time = follow , self.record[follow]['posts'][-1][1]

            stack.append(
                (user , self.record[user]['posts'].pop() )
            )                        

        returnPosts = [ post[0] for (user,post) in stack] 

        # 貼回前面取出的貼文 , 注意不是使用for loop , 需要while + pop才能保持原始順序 
        while stack : 
            user , post = stack.pop() 
            self.record[user]["posts"].append(post)


        return returnPosts





# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)