### Russian Doll Envelopes
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

[leetcode](https://leetcode.com/problems/russian-doll-envelopes/description/)

### Answer
Sort the array according to the envolop first dimension, so the later one can always include the earlier one. Then, it becomes to be the problem [300](300_Longest_Increasing_Subsequence.md). 

	class Solution {
	public:
	    struct less_than{
	        inline bool operator () (const pair<int, int> &p1, const pair<int, int> &p2)
	        {
	            return p1.first < p2.first;
	        }
	    };
	    
	    int maxEnvelopes(vector<pair<int, int>>& envelopes) {
	        int len = envelopes.size();
	        if (len == 0) return 0;
	        
	        sort(envelopes.begin(), envelopes.end(), less_than());
	        vector<int> dp(len, 0);
	        dp[0] = 1;
	        int res = 1;
	        
	        for (int i = 1; i < len; ++i)
	        {
	            int curr = 0;
	            for (int j = 0; j < i; ++j)
	            {
	                if (envelopes[i].second > envelopes[j].second &&
	                    envelopes[i].first  > envelopes[j].first) 
	                {
	                    curr = max(curr, dp[j]);
	                }
	            }
	            dp[i] = curr + 1;
	            res = max(dp[i], res);
	        }
	        return res;
	    }
	};