### Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

[leetcode](https://leetcode.com/problems/combinations/description/)

### Answer 
classic backtracking problem using dfs

	class Solution {
	public:
	    vector<vector<int>> combine(int n, int k) {
	        vector<vector<int>> result;
	        vector<int> comb;
	        recur(result, comb, 1, n, k);
	        return result;
	    }
	    
	    void recur(vector<vector<int>> &result, vector<int> &comb, int curr, int n, int k)
	    {
	        if (comb.size() == k) 
	        {
	            result.push_back(comb);
	            return;
	        }
	        if (comb.size() > k || curr > n) return;
	        
	        recur(result, comb, curr + 1, n, k);
	        
	        comb.push_back(curr);
	        recur(result, comb, curr + 1, n, k);
	        comb.pop_back();
	    }
	};