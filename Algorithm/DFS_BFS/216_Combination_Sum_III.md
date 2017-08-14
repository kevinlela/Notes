### Combination Sum III
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

[leetcode](https://leetcode.com/problems/combination-sum-iii/description/)

### Answer 
Backtracking problem

	class Solution {
	public:
	    vector<vector<int>> combinationSum3(int k, int n) {
	        vector<vector<int>> result;
	        vector<int> comb;
	        if (k == 0 && n == 0) return result;
	        if (n > 55) return result;
	        
	        recur(result, comb, 1, k, n);
	        return result;
	    }
	    
	    void recur(vector<vector<int>> &result, vector<int> &comb, 
	               int curr, int k, int n)
	    {
	        if (comb.size() > k || n < 0) return;
	        if (n == 0 && comb.size() == k) 
	        {
	            result.push_back(comb);
	            return;
	        }
	        if (curr > 9) return;
	        
	        comb.push_back(curr);
	        recur(result, comb, curr + 1, k, n - curr);
	        comb.pop_back();
	        
	        recur(result, comb, curr + 1, k, n);
	    }
	};