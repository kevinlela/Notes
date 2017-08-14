### Search a 2D Matrix II
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

[leetcode](https://leetcode.com/problems/search-a-2d-matrix-ii/description/)

### Answer 
Start from the right upper corner. 

If it is smaller than target, it must belong to lower part, so we move down.

if it is greater than target, it must bekong to lefter part, so we move left.

	class Solution {
	public:
	    bool searchMatrix(vector<vector<int>>& matrix, int target) {
	        int h = matrix.size();
	        if (h == 0) return false;
	        int w = matrix[0].size();
	        if (w == 0) return false;
	        
	        int j = 0, i = w - 1;
	        
	        while ( j < h && i >= 0)
	        {
	            if (matrix[j][i] == target) return true;
	            else if (matrix[j][i] < target) ++j;
	            else --i;
	        }
	        
	        return false;
	    }
	};