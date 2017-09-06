### Diagonal Traverse
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.


[leetcode](https://leetcode.com/problems/diagonal-traverse/description/)

### Answer

	class Solution {
	public:
	    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
	        vector<int> result;
	        int h = matrix.size();
	        if (h == 0) return result;
	        int w = matrix[0].size();
	        if (w == 0) return result;
	        
	        int j = 0, i = 0, len = h * w;
	        bool up = true;
	        while (result.size() != len)
	        {
	            while (i >= 0 && i < w && j >= 0 && j < h)
	            {
	                result.push_back(matrix[j][i]);
	                if (up)
	                {
	                    ++i;
	                    --j;
	                }
	                else
	                {
	                    --i;
	                    ++j;
	                }
	            }
	            
	            if (up) // right or down
	            {
	                ++j;
	                if (i >= w)
	                {
	                    --i;
	                    ++j;
	                }
	            }
	            else
	            {
	                ++i;
	                if (j >= h)
	                {
	                    --j;
	                    ++i;
	                }
	            }
	            
	            up = !up;
	        }
	        return result;
	    }
	};
