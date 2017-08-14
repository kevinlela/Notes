### Range Sum Query 2D - Immutable
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.

[leetcode](https://leetcode.com/problems/range-sum-query-2d-immutable/description/)

### Answer 

	class NumMatrix {
	public:
	    NumMatrix(vector<vector<int>> matrix) {
	        int h = matrix.size();
	        if (h == 0) return;
	        int w = matrix[0].size();
	        if (w == 0) return;
	        
	        d_sum = matrix;
	        
	        int row_sum = 0;
	        for (int i = 0; i < w; ++i)
	        {
	            row_sum += matrix[0][i];
	            d_sum[0][i] = row_sum;
	        }
	        
	        for (int j = 1; j < h; ++j)
	        {
	            row_sum = 0;
	          	for (int i = 0; i < w; ++i)
	            {
	                row_sum += matrix[j][i];
	                d_sum[j][i] = row_sum + d_sum[j-1][i];
	            }
	        }
	    }
	    
	    int sumRegion(int row1, int col1, int row2, int col2) {
	        int rec1 = row1 == 0 ? 0 : d_sum[row1 - 1][col2];
	        int rec2 = col1 == 0 ? 0 : d_sum[row2][col1 - 1];
	        int rec3 = row1 == 0 || col1 == 0 ? 0 : d_sum[row1 - 1][col1 - 1];
	        return d_sum[row2][col2] - rec1 - rec2 + rec3;
	    }
	private:
	    vector<vector<int>> d_sum;
	};

	/**
	 * Your NumMatrix object will be instantiated and called as such:
	 * NumMatrix obj = new NumMatrix(matrix);
	 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
	 */