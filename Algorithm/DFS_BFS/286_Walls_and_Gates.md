### Walls and Gates
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

[leetcode](https://leetcode.com/problems/walls-and-gates/description/)

### Answer

	class Solution {
	public:
	    void wallsAndGates(vector<vector<int>>& rooms) {
	        int inf = 2147483647;
	        int h = rooms.size();
	        if (h == 0) return;
	        int w = rooms[0].size();
	        queue<pair<int, int>> q;
	        for (int i = 0; i < h; ++i)
	        {
	            for (int j = 0; j < w; ++j)
	            {
	                if (rooms[i][j] == 0) q.push({i, j});
	            }
	        }
	        
	        int dis = 1;
	        while (!q.empty())
	        {
	            int len = q.size();
	            for (int i = 0; i < len; ++i)
	            {
	                int x = q.front().first;
	                int y = q.front().second;
	                if (x - 1 >= 0 && rooms[x-1][y] == inf)
	                {
	                    rooms[x-1][y] = dis;
	                    q.push({x-1, y});
	                }
	                if (x + 1 <  h && rooms[x+1][y] == inf)
	                {
	                    rooms[x+1][y] = dis;
	                    q.push({x+1, y});
	                }
	                if (y - 1 >= 0 && rooms[x][y-1] == inf)
	                {
	                    rooms[x][y-1] = dis;
	                    q.push({x, y-1});
	                }
	                if (y + 1 >= 0 && rooms[x][y+1] == inf)
	                {
	                    rooms[x][y+1] = dis;
	                    q.push({x, y+1});
	                }
	                q.pop();
	            }
	            ++dis;
	        }
	        
	        return;
	    }
	};