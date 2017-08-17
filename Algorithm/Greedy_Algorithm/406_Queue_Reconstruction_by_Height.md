### Queue Reconstruction by Height
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

[leetcode](https://leetcode.com/problems/queue-reconstruction-by-height/description/)

### Answer 
This is a greedy algorithm, since the k of large h is not depends on the k of small h, so we put large k first than small k. Suppose k1 > k2, after we put all k1 and come with k2, all the elements in the array are larger than k2. 

class Solution {
public:
    struct greater_than{
        inline bool operator() (const pair<int, int> &p1, const pair<int, int> &p2)
        {
            if (p1.first == p2.first) return p1.second < p2.second;
            return p1.first > p2.first;
        }
    };
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        sort(people.begin(), people.end(), greater_than());
        vector<pair<int, int>> result;
        for (int i = 0; i < people.size(); ++i)
        {
            result.insert(result.begin() + people[i].second, people[i]);
        }
        return result;
    }
};