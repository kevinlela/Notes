### Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

[leetcode](https://leetcode.com/problems/number-of-islands/description/)

### Answer 

	class Solution {
	public:
	    int numIslands(vector<vector<char>>& grid) {
	        int result = 0;
	        int h = grid.size();
	        if (h == 0) return result;
	        int w = grid[0].size();
	        if (w == 0) return result;
	        
	        for (int j = 0; j < h; ++j)
	        {
	            for (int i = 0; i < w; ++i)
	            {
	                if (grid[j][i] == '1')
	                {
	                    ++result;
	                    bfs(grid, j, i);
	                }
	            }
	        }
	        
	        return result;
	    }
	    
	    void bfs(vector<vector<char>>& grid, int j, int i)
	    {
	        int h = grid.size();
	        int w = grid[0].size();
	        
	        queue<pair<int, int>> myQ;
	        myQ.push({j, i});
	        grid[j][i] = 'x';
	        
	        while (!myQ.empty())
	        {
	            int len = myQ.size();
	            for (int k = 0; k < len; ++k)
	            {
	                j = myQ.front().first;
	                i = myQ.front().second;
	                if ( j + 1 < h && grid[j + 1][i] == '1')
	                {
	                    grid[j + 1][i] = 'x';
	                    myQ.push({j + 1, i});
	                }
	                if ( j - 1 >= 0 && grid[j - 1][i] == '1')
	                {
	                    grid[j - 1][i] = 'x';
	                    myQ.push({j - 1, i});
	                }
	                if ( i + 1 < w && grid[j][i + 1] == '1')
	                {
	                    grid[j][i + 1] = 'x';
	                    myQ.push({j, i + 1});
	                }
	                if ( i - 1 >= 0 && grid[j][i - 1] == '1')
	                {
	                    grid[j][i - 1] = 'x';
	                    myQ.push({j, i - 1});
	                }
	            }
	            myQ.pop();
	        }
	    }
	};