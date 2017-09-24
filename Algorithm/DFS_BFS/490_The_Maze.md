### The Maze
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false
Explanation: There is no way for the ball to stop at the destination.

Note:
There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

[leetcode](https://leetcode.com/problems/the-maze/description/)

### Answer

	class Solution {
	public:
	    bool hasPath(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
	        int h = maze.size();
	        if (h == 0) return false;
	        int w = maze[0].size();
	        if (w == 0) return false;
	        
	        vector<vector<pair<int, int>>> lr(h, vector<pair<int, int>>(w, {0, 0}));
	        vector<vector<pair<int, int>>> ud(h, vector<pair<int, int>>(w, {0, 0}));
	        int left = -1, up = -1;
	        for (int i = 0; i < h; ++i)
	        {
	            for (int j = 0; j < w; ++j)
	            {
	                if (maze[i][j] == 1)
	                {
	                    lr[i][j].first = j;
	                    ud[i][j].first = i;
	                    continue;
	                }
	                if (j == 0) lr[i][j].first = -1;
	                else lr[i][j].first = lr[i][j-1].first;
	                if (i == 0) ud[i][j].first = -1;
	                else ud[i][j].first = ud[i-1][j].first;
	            }
	        }
	        
	        for (int i = h - 1; i >= 0; --i)
	        {
	            for (int j = w - 1; j >= 0; --j)
	            {
	                if (maze[i][j] == 1)
	                {
	                    lr[i][j].second = j;
	                    ud[i][j].second = i;
	                    continue;
	                }
	                if (j == w - 1) lr[i][j].second = w;
	                else lr[i][j].second = lr[i][j+1].second;
	                if (i == h - 1) ud[i][j].second = h;
	                else ud[i][j].second = ud[i+1][j].second;
	            }
	        }
	        
	        vector<vector<bool>> visited(h, vector<bool>(w, false));
	        queue<pair<int, int>> q;
	        q.push({start[0], start[1]});
	        visited[q.front().first][q.front().second] = true;
	        while (!q.empty())
	        {
	            int qLen = q.size();
	            for (int i = 0; i < qLen; ++i)
	            {
	                int r = q.front().first, c = q.front().second;
	                if (r == destination[0] && c == destination[1]) return true;
	                //cout << r << " | " << c << endl;
	                int rc = lr[r][c].second - 1;
	                int lc = lr[r][c].first + 1;
	                //cout << lc << " " << rc << endl;
	                if (!visited[r][lc]) 
	                {
	                    visited[r][lc] = true;
	                    q.push({r, lc});
	                }
	                if (!visited[r][rc])
	                {
	                    visited[r][rc] = true;
	                    q.push({r, rc});
	                }
	                int dr = ud[r][c].second - 1;
	                int ur = ud[r][c].first + 1;
	                //cout << ur << " " << dr << endl;
	                if (!visited[ur][c]) 
	                {
	                    visited[ur][c] = true;
	                    q.push({ur, c});
	                }
	                if (!visited[dr][c])
	                {
	                    visited[dr][c] = true;
	                    q.push({dr, c});
	                }
	                q.pop();
	            }
	        }
	        
	        return false;
	    }
	};
