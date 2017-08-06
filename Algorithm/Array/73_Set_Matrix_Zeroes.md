### Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?



[leetcode](https://leetcode.com/problems/set-matrix-zeroes/description/)

### Answer 
It is a tricky problem that uses the first row and column to store the status of each row and column

	class Solution {
	public:
	    void setZeroes(vector<vector<int>>& matrix) {
	        bool setFirstRow = false, setFirstCol = false;
	        int h = matrix.size(); 
	        if (h == 0) return;
	        int w = matrix[0].size();
	        for (int i = 0; i < w; ++i)
	        {
	            if (matrix[0][i] == 0)
	            {
	                setFirstRow = true;
	                break;
	            }
	        }
	        
	        for (int j = 0; j < h; ++j)
	        {
	            if (matrix[j][0] == 0)
	            {
	                setFirstCol = true;
	                break;
	            }
	        }
	        
	        for (int j = 1; j < h; ++j)
	        {
	            for (int i = 1; i < w; ++i)
	            {
	                if (matrix[j][i] == 0)
	                {
	                    matrix[j][0] = 0;
	                    matrix[0][i] = 0;
	                }
	            }
	        }
	        
	        for (int j = 1; j < h; ++j)
	        {
	            if (matrix[j][0] != 0) continue;
	            for (int i = 0; i < w; ++i)
	            {
	                matrix[j][i] = 0;
	            }
	        }
	        
	        for (int i = 1; i < w; ++i)
	        {
	            if (matrix[0][i] != 0) continue;
	            for (int j = 0; j < h; ++j)
	            {
	                matrix[j][i] = 0;
	            }
	        }
	        
	        if (setFirstRow)
	        {
	            for (int i = 0; i < w; ++i)
	            {
	                matrix[0][i] = 0;
	            }
	        }
	        
	        if (setFirstCol)
	        {
	            for (int j = 0; j < h; ++j)
	            {
	                matrix[j][0] = 0;
	            }
	        }
	    }
	};