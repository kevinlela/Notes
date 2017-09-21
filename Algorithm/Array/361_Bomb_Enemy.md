### Bomb Enemy
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)

[leetcode](https://leetcode.com/problems/bomb-enemy/description/)

### Answer
	class Solution {
	public:
	    int maxKilledEnemies(vector<vector<char>>& grid) {
	        int h = grid.size();
	        if (h == 0) return 0;
	        int w = grid[0].size();
	        if (w == 0) return 0;
	        
	        vector<vector<int>> kills(h, vector<int>(w, 0));
	        
	        for (int i = 0; i < h; ++i)
	        {
	            int j = 0, st = 0, count = 0;
	            while (j <= w)
	            {
	                if (j == w || grid[i][j] == 'W')
	                {
	                    for (st; st < j; ++st)
	                    {
	                        if (grid[i][st] == '0') kills[i][st] += count; 
	                    }
	                    st = j+1; 
	                    count = 0;
	                }
	                else if (grid[i][j] == 'E') ++count;
	                ++j;
	            }
	        }
	        
	        int result = 0;
	        for (int j = 0; j < w; ++j)
	        {
	            int i = 0, st = 0, count = 0;
	            while (i <= h)
	            {
	                if (i == h || grid[i][j] == 'W')
	                {
	                    for (st; st < i; ++st)
	                    {
	                        if (grid[st][j] == '0') result = max(kills[st][j] + count, result); 
	                    }
	                    st = i+1; 
	                    count = 0;
	                }
	                else if (grid[i][j] == 'E') ++count;
	                ++i;
	            }
	        }
	        
	        return result;
	    }
	};