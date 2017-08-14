### Summary Ranges
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

[leetcode](https://leetcode.com/problems/summary-ranges/description/)

### Answer 

	class Solution {
	public:
	    vector<string> summaryRanges(vector<int>& nums) {
	        vector<string> result;
	        for (int i = 0; i < nums.size();)
	        {
	            string curr;
	            int j = i;
	            int curr_end = nums[j], ori = nums[j];
	            curr += to_string(nums[j++]);
	            
	            for (; j < nums.size(); ++j)
	            {
	                if (nums[j] - nums[j-1] == 1) curr_end = nums[j];
	                else break;
	            }
	            
	            if (curr_end != ori) curr += "->" + to_string(curr_end);
	            result.push_back(curr);
	            i = j;
	        }
	        return result;
	    }
	};