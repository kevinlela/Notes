### Subsets II
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

[leetcode](https://leetcode.com/problems/subsets-ii/description/)

### Answer 
use sort to avoid duplicate

	class Solution {
	public:
	    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
	        sort(nums.begin(), nums.end());
	        vector<vector<int>> result;
	        vector<int> comb;
	        recur(result, comb, nums, 0);
	        return result;
	    }
	    
	    void recur(vector<vector<int>> &result, vector<int> &comb, const vector<int> &nums, int curr)
	    {
	        if (curr >= nums.size())
	        {
	            result.push_back(comb);
	            return;
	        }
	        
	        comb.push_back(nums[curr]);
	        recur(result, comb, nums, curr + 1);
	        comb.pop_back();
	        
	        int currVal = nums[curr];
	        for (; curr < nums.size(); ++curr)
	        {
	            if (nums[curr] != currVal) break;
	        }
	        recur(result, comb, nums, curr);
	    }
	};