### Pascal's Triangle II
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

[leetcode](https://leetcode.com/problems/pascals-triangle-ii/description/)

### Answer 

	class Solution {
	public:
	    vector<int> getRow(int rowIndex) {
	        if (rowIndex < 0) return vector<int>();
	        vector<int> result(rowIndex + 1, 1);
	        if (rowIndex <= 1) return result;
	        
	        for (int i = 2; i <= rowIndex; ++i)
	        {
	            int prev = 1;
	            for (int j = 1; j < i; ++j)
	            {
	                int tmp = result[j];
	                result[j] = prev + result[j];
	                prev = tmp;
	            }
	        }
	        return result;
	    }
	};