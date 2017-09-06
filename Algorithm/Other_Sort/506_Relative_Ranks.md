### Relative Ranks
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.

[leetcode](https://leetcode.com/problems/relative-ranks/description/)

### Answer

	class Solution {
	public:
	    struct greater_than{
	        inline bool operator () (const pair<int, int> &p1, const pair<int, int> &p2)
	        {
	            return p1.first > p2.first;
	        }
	    };
	    vector<string> findRelativeRanks(vector<int>& nums) {
	        vector<pair<int, int>> num_idx;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            num_idx.push_back({nums[i], i});
	        }
	        sort(num_idx.begin(), num_idx.end(), greater_than());
	        vector<string> result(nums.size(), "");
	        for (int i = 0; i < num_idx.size(); ++i)
	        {
	            if (i == 0) result[num_idx[i].second] = "Gold Medal";
	            else if (i == 1) result[num_idx[i].second] = "Silver Medal";
	            else if (i == 2) result[num_idx[i].second] = "Bronze Medal";
	            else result[num_idx[i].second] = to_string(i+1);
	        }
	        
	        return result;
	    }
	};
