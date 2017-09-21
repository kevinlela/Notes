### Factor Combinations
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note: 
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Examples: 
input: 1
output: 
[]
input: 37
output: 
[]
input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]

[leetcode](https://leetcode.com/problems/factor-combinations/description/)

### Answer
One thing need to notive, we need prev to control the order. otherwise duplicate will happen like for 12, it will happen [2, 2, 3] and [3, 2, 2] 

	class Solution {
	public:
	    vector<vector<int>> getFactors(int n) {
	        return recur(n, 2);
	    }
	    
	    vector<vector<int>> recur(int n, int prev)
	    {
	        vector<vector<int>> result;
	        for (int i = prev; i <= sqrt(n); ++i)
	        {
	            if (n % i) continue;
	            int right = n/i;
	            vector<vector<int>> res = recur(right, i);
	            for (int j = 0; j < res.size(); ++j)
	            {
	                vector<int> line = {i};
	                line.insert(line.end(), res[j].begin(), res[j].end());
	                result.push_back(line);
	            }
	            vector<int> line = {i, right};
	            result.push_back(line);
	        }
	        return result;
	    }
	};
