### The Maze II
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

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

Output: 12
Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1
Explanation: There is no way for the ball to stop at the destination.

Note:
There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

[leetcode](https://leetcode.com/problems/the-maze-ii/description/)

### Answer

	class Solution {
	public:
	    int shortestDistance(vector<vector<int>>& maze, vector<int>& start, vector<int>& destination) {
	        int h = maze.size();
	        if (h == 0) return false;
	        int w = maze[0].size();
	        if (w == 0) return false;
	        
	        vector<vector<int>> visited(h, vector<int>(w, 0));
	        queue<pair<pair<int, int>, char>> q;
	        q.push({{start[0], start[1]}, 'b'});
	        visited[q.front().first.first][q.front().first.second] = 15;
	        int dis = 0;
	        while (!q.empty())
	        {
	            int qLen = q.size();
	            for (int i = 0; i < qLen; ++i)
	            {
	                int r = q.front().first.first, c = q.front().first.second;
	                //cout << r << " " << c << endl;
	                int op = q.front().second;
	                if (is_des(r, c, destination[0], destination[1], op, maze, w, h)) return dis;
	                push_direction(q, op, maze, visited, r, c, w, h);
	                q.pop();
	            }
	            //cout << endl;
	            ++dis;
	        } 
	        return -1;
	    }
	    
	    bool is_des(int r, int c, int t_r, int t_c, char op, vector<vector<int>> &maze, int w, int h)
	    {
	        if (r != t_r || c != t_c) return false;
	        if (op == 'b') return true;
	        if (op == 'u')
	        {
	            if (r - 1 < 0) return true;
	            if (maze[r-1][c] == 1) return true;
	        }
	        if (op == 'd')
	        {
	            if (r + 1 >= h) return true;
	            if (maze[r+1][c] == 1) return true;
	        }
	        if (op == 'l')
	        {
	            if (c - 1 < 0) return true;
	            if (maze[r][c-1] == 1) return true;
	        }
	        if (op == 'r')
	        {
	            if (c + 1 >= w) return true;
	            if (maze[r][c+1] == 1) return true;
	        }
	        return false;
	    }
	            
	    void push_direction(queue<pair<pair<int, int>, char>> &q, char op, vector<vector<int>> &maze, 
	                        vector<vector<int>> &visited, int r, int c, int w, int h)
	    {
	        if (op == 'b')
	        {
	            push_four(q, maze, visited, r, c, w, h);
	        }
	        
	        if (op == 'u')
	        {
	            if (r - 1 >= 0)
	            {
	                if (maze[r-1][c] == 0)
	                {
	                    if (!(visited[r-1][c] & 1))
	                    {
	                        q.push({{r-1, c}, 'u'});
	                        visited[r-1][c] |= 1;
	                    }
	                }
	                else push_four(q, maze, visited, r, c, w, h);
	            }  
	            else push_four(q, maze, visited, r, c, w, h);
	        }
	        
	        if (op == 'd')
	        {
	            if (r + 1 <  h)
	            {
	                if (maze[r+1][c] == 0)
	                {
	                    if (!(visited[r+1][c] & 2))
	                    {
	                        q.push({{r+1, c}, 'd'});
	                        visited[r+1][c] |= 2;
	                    }
	                }
	                else push_four(q, maze, visited, r, c, w, h);
	            }  
	            else push_four(q, maze, visited, r, c, w, h);
	        }
	        
	        if (op == 'l')
	        {
	            if (c - 1 >= 0)
	            {
	                if (maze[r][c-1] == 0)
	                {
	                    if (!(visited[r][c-1] & 4))
	                    {
	                        q.push({{r, c-1}, 'l'});
	                        visited[r][c-1] |= 4;
	                    }
	                }
	                else push_four(q, maze, visited, r, c, w, h);
	            }  
	            else push_four(q, maze, visited, r, c, w, h);
	        }
	        
	        if (op == 'r')
	        {
	            if (c + 1 <  w)
	            {
	                if (maze[r][c+1] == 0)
	                {
	                    if (!(visited[r][c+1] & 8))
	                    {
	                        q.push({{r, c+1}, 'r'});
	                        visited[r][c+1] |= 8;
	                    }
	                }
	                else push_four(q, maze, visited, r, c, w, h);
	            }  
	            else push_four(q, maze, visited, r, c, w, h);
	        }
	    }
	    
	    void push_four(queue<pair<pair<int, int>, char>> &q, vector<vector<int>> &maze, 
	                        vector<vector<int>> &visited, int r, int c, int w, int h)
	    {
	        visited[r][c] = 15;
	        if (r - 1 >= 0 && !(visited[r-1][c] & 1) && maze[r-1][c] == 0)
	        {
	            q.push({{r-1, c}, 'u'});
	            visited[r-1][c] |= 1;
	        }
	        if (r + 1 <  h && !(visited[r+1][c] & 2) && maze[r+1][c] == 0)
	        {
	            q.push({{r+1, c}, 'd'});
	            visited[r+1][c] |= 2;
	        }
	        if (c - 1 >= 0 && !(visited[r][c-1] & 4) && maze[r][c-1] == 0)
	        {
	            q.push({{r, c-1}, 'l'});
	            visited[r][c-1] |= 4;
	        }
	        if (c + 1 <  w && !(visited[r][c+1] & 8) && maze[r][c+1] == 0)
	        {
	            q.push({{r, c+1}, 'r'});
	            visited[r][c+1] |= 8;
	        }
	    }    
	};
