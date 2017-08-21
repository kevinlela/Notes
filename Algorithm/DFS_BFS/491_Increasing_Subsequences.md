### Increasing Subsequences
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

[leetcode](https://leetcode.com/problems/increasing-subsequences/description/)

### Answer

	class Solution {
	public:
	    vector<vector<int>> findSubsequences(vector<int>& nums) {
	        vector<vector<int>> result;
	        vector<int> curr;
	        dfs(result, curr, nums, 0);
	        return result;
	    }
	    
	    void dfs(vector<vector<int>> &result, vector<int> &curr, const vector<int> &nums, int idx)
	    {
	        if (curr.size() > 1)
	        {
	            result.push_back(curr);
	        }
	        if (idx == nums.size())  return;
	        
	        unordered_set<int> visited; //avoid duplicate
	        for (int i = idx; i < nums.size(); ++i)
	        {
	            if (curr.empty() || nums[i] >= *(curr.rbegin()))
	            {
	                if (visited.find(nums[i]) != visited.end()) continue;
	                curr.push_back(nums[i]);
	                visited.insert(nums[i]);
	                dfs(result, curr, nums, i+1);
	                curr.pop_back();
	            }
	        }
	    }
	};