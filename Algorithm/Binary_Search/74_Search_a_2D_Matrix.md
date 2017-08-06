### Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

	*Integers in each row are sorted from left to right.
	*The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

[leetcode](https://leetcode.com/problems/search-a-2d-matrix/description/)

### Answer 

	class Solution {
	public:
	    bool searchMatrix(vector<vector<int>>& matrix, int target) {
	        int h = matrix.size();
	        if (h == 0) return false;
	        int w = matrix[0].size();
	        if (w == 0) return false;
	        
	        int st = 0, ed = h;
	        while (st < ed)
	        {
	            int mid = st + (ed - st)/2;
	            if (matrix[mid][0] == target) return true;
	            else if (matrix[mid][0] > target) ed = mid;
	            else st = mid + 1;
	        }
	        
	        int targetRow = ed - 1;
	        if (targetRow < 0) return false;
	        
	        st = 0; ed = w;
	        
	        while (st < ed)
	        {
	            int mid = st + (ed - st)/2;
	            if (matrix[targetRow][mid] == target) return true;
	            else if (matrix[targetRow][mid] > target) ed = mid;
	            else st = mid + 1;
	        }
	        
	        return false;
	    }
	};