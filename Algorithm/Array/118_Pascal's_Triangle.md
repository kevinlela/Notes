### Pascal's Triangle
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


[leetcode](https://leetcode.com/problems/pascals-triangle/description/)

### Answer 

	class Solution {
	public:
	    vector<vector<int>> generate(int numRows) {
	        vector<vector<int>> result(numRows, vector<int>(1, 1));
	        if (numRows <= 0) return result;
	        for (int i = 1; i < numRows; ++i)
	        {
	            for (int j = 1; j < i; ++j)
	            {
	                result[i].push_back(result[i-1][j] + result[i-1][j-1]);
	            }
	            result[i].push_back(1);
	        }
	        return result;
	    }
	};