### Combination Sum II
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

[leetcode]()

### Answer 
the difference between non-duplicate [here](39_Combination_Sum.md) is we need skip the duplication, we can leverage the sorting to skip duplicate. But IMPORTANT! we need to consider into next loop, whether this sorting preserved. This is why send vector not reference

	class Solution {
	public:
	    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
	        sort(candidates.begin(), candidates.end());
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
	        recur(result, comb, candidates, st + 1, target, sum + candidates[st]);
	        comb.pop_back();
	        
	        int curr = candidates[st];
	        for (st = st + 1; st < candidates.size(); ++st)
	        {
	            if (candidates[st] != curr) break;
	        }
	        
	        recur(result, comb, candidates, st, target, sum);
	    }
	};