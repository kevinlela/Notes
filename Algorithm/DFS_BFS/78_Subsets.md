### Subsets
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

[leetcode](https://leetcode.com/problems/subsets/description/)

### Answer 
classic backtracking problem uses dfs

	class Solution {
	public:
	    vector<vector<int>> subsets(vector<int>& nums) {
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
	        
	        recur(result, comb, nums, curr + 1);
	        
	        comb.push_back(nums[curr]);
	        recur(result, comb, nums, curr + 1);
	        comb.pop_back();
	    }
	};