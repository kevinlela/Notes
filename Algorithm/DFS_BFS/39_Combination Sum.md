### Combination Sum
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]

[leetcode](https://leetcode.com/problems/combination-sum/description/)

### Answer 

	class Solution {
	public:
	    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
	        vector<vector<int>> result;
	        vector<int> comb;
	        recur(result, comb, candidates, 0, target, 0);
	        return result;
	    }
	    
	    void recur(vector<vector<int>> &result, vector<int> &comb, 
	               const vector<int> &candidates, int st, int target, int sum)
	    {
	        if (sum == target)
	        {
	            result.push_back(comb);
	            return;
	        }
	        else if (sum > target) return;
	        else if (st >= candidates.size()) return;
	        
	        comb.push_back(candidates[st]);
	        recur(result, comb, candidates, st, target, sum + candidates[st]);
	        comb.pop_back();
	        
	        recur(result, comb, candidates, st + 1, target, sum);
	    }
	};