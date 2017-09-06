### 01 Matrix
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.

[leetcode](https://leetcode.com/problems/01-matrix/description/)

### Answer

It is a dp problem, we need to go from left-up and right-down so two traversal. but I use bfs, but also another solution 

	class Solution {
	public:
	    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
	        queue<pair<int, int>> myQ;
	        int h = matrix.size();
	        int w = matrix[0].size();
	        vector<vector<int>> result(h, vector<int> (w, 0));
	        for (int j = 0; j < h; ++j)
	        {
	            for (int i = 0; i < w; ++i)
	            {
	                if (matrix[j][i] == 0) myQ.push({j, i});
	                else result[j][i] = -1;
	            }
	        }
	        
	        int dis = 1;
	        while (!myQ.empty())
	        {
	            int len = myQ.size();
	            for (int i = 0; i < len; ++i)
	            {
	                int r = myQ.front().first, c = myQ.front().second;
	                if (r - 1 >= 0 && result[r-1][c] < 0) 
	                {
	                    result[r-1][c] = dis;
	                    myQ.push({r-1, c});
	                }
	                if (r + 1 <  h && result[r+1][c] < 0) 
	                {
	                    result[r+1][c] = dis;
	                    myQ.push({r+1, c});
	                }
	                if (c - 1 >= 0 && result[r][c-1] < 0) 
	                {
	                    result[r][c-1] = dis;
	                    myQ.push({r, c-1});
	                }
	                if (c + 1 <  w && result[r][c+1] < 0) 
	                {
	                    result[r][c+1] = dis;
	                    myQ.push({r, c+1});
	                }
	                myQ.pop();
	            }
	            ++dis;
	        }
	        
	        return result;
	    }
	};
