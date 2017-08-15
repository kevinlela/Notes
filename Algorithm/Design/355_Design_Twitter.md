### Design Twitter
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);

[leetcode](https://leetcode.com/problems/design-twitter/description/)

### Answer

class Twitter {
public:
    /** Initialize your data structure here. */
    Twitter() {
        d_time_stamp = 0;
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        d_id_user[userId].push_front({tweetId, d_time_stamp++});
        if (d_id_user[userId].size() > 10)
        {
            d_id_user[userId].pop_back();
        }
    }
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, newer_than> pq;
        list<pair<int, int>> &self = d_id_user[userId];
        for (auto iter = self.begin(); iter != self.end(); ++iter)
        {
            pq.push(*iter);
            if (pq.size() > 10) pq.pop();
        }
        unordered_set<int> &following = d_id_follow[userId];
        for (auto mi = following.begin(); mi != following.end(); ++mi)
        {
            list<pair<int, int>> tl = d_id_user[*mi];
            for (auto iter = tl.begin(); iter != tl.end(); ++iter)
            {
                if (pq.size() == 10 && pq.top().second > iter->second) break;
                pq.push(*iter);
                if (pq.size() > 10) pq.pop();
            }
        }
        
        vector<int> result;
        while (!pq.empty())
        {
            result.push_back(pq.top().first);
            pq.pop();
        }
        
        reverse(result.begin(), result.end());
        return result;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        if (followerId == followeeId) return;
        d_id_follow[followerId].insert(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        if (followerId == followeeId) return;
        d_id_follow[followerId].erase(followeeId);
    }
private:
    struct newer_than{
        inline bool operator () (const pair<int, int> &p1, 
                                 const pair<int, int> &p2)
        {
            return p1.second > p2.second;
        }
    };
    unordered_map<int, list<pair<int, int>> > d_id_user;
    unordered_map<int, unordered_set<int> > d_id_follow; 
    int d_time_stamp;
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * vector<int> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */
