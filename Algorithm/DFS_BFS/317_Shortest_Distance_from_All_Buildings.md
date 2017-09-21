### Shortest Distance from All Buildings
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

[leetcode](https://leetcode.com/problems/shortest-distance-from-all-buildings/description/)

### Answer
A trick here is to use visited array as count level to track so that we do not need to create an array every time in the bfs.

	class Solution {
	public:
	    int shortestDistance(vector<vector<int>>& grid) {
	        int h = grid.size();
	        if (h == 0) return 0;
	        int w = grid[0].size();
	        if (w == 0) return 0;
	        
	        vector<vector<int>> v(h, vector<int> (w, false));
	        
	        int l = 0;
	        for (int i = 0; i < h; ++i)
	        {
	            for (int j = 0; j < w; ++j)
	            {
	                if (grid[i][j] == 1) bfs(grid, v, l++, i, j);
	            }
	        }
	        
	        int result = INT_MAX;
	        for (int i = 0; i < h; ++i)
	        {
	            for (int j = 0; j < w; ++j)
	            {
	                if (grid[i][j] < 0 && v[i][j] == l) result = min(result, -grid[i][j]);
	            }
	        }
	        
	        return result == INT_MAX ? -1 : result;
	    }
	    
	    void bfs(vector<vector<int>> &grid, vector<vector<int>> &v, int l, 
	             int r, int c)
	    {
	        int h = grid.size(), w = grid[0].size();
	        queue<pair<int, int>> q;
	        q.push({r, c});
	        int dis = -1;
	        while (!q.empty())
	        {
	            int len = q.size();
	            for (int i = 0; i < len; ++i)
	            {
	                int cr = q.front().first;
	                int cc = q.front().second;
	                if (cr - 1 >= 0 && grid[cr-1][cc] <= 0 && v[cr-1][cc] == l)
	                {
	                    grid[cr-1][cc] += dis;
	                    ++v[cr-1][cc];
	                    q.push({cr-1, cc});
	                }
	                if (cr + 1  < h && grid[cr+1][cc] <= 0 && v[cr+1][cc] == l)
	                {
	                    grid[cr+1][cc] += dis;
	                    ++v[cr+1][cc];
	                    q.push({cr+1, cc});
	                }
	                if (cc - 1 >= 0 && grid[cr][cc-1] <= 0 && v[cr][cc-1] == l)
	                {
	                    grid[cr][cc-1] += dis;
	                    ++v[cr][cc-1];
	                    q.push({cr, cc-1});
	                }
	                if (cc + 1  < w && grid[cr][cc+1] <= 0 && v[cr][cc+1] == l)
	                {
	                    grid[cr][cc+1] += dis;
	                    ++v[cr][cc+1];
	                    q.push({cr, cc+1});
	                }
	                q.pop();
	            }
	            --dis;
	        }
	    }
	};