### Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

[leetcode](https://leetcode.com/problems/permutations-ii/description/)

### Answer 
skip duplicate by sorting

	class Solution {
	public:
	    vector<vector<int>> permuteUnique(vector<int>& nums) {
	        vector<vector<int>> result;
	        sort(nums.begin(), nums.end());
	        recur(result, nums, 0);
	        return result;
	    }
	    
	    void recur(vector<vector<int>> &result, vector<int> nums, int st)
	    {
	        if (st >= nums.size())
	        {
	            result.push_back(nums);
	            return;
	        }
	        
	        recur(result, nums, st + 1);
	        
	        for (int i = st + 1; i < nums.size(); ++i)
	        {
	            if (nums[i] != nums[st])
	            {
	                swap(nums[st], nums[i]);
	                recur(result, nums, st + 1);
	            }
	        }
	    }
	};