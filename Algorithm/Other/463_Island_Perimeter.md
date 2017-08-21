### Island Perimeter
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:


[leetcode](https://leetcode.com/problems/island-perimeter/description/)

### Answer

The easiest way is to use masks

	class Solution {
	public:
	    int islandPerimeter(vector<vector<int>>& grid) {
	        int h = grid.size();
	        if (h == 0) return 0;
	        int w = grid[0].size();
	        if (w == 0) return 0;
	        
	        int result = 0;
	        for (int j = 0; j < grid.size(); ++j)
	        {
	            for (int i = 0; i < grid[0].size(); ++i)
	            {
	                if (grid[j][i] == 0) continue;
	                int count = 0;
	                if (j-1 >= 0 && grid[j-1][i]) ++count;
	                if (j+1 <  h && grid[j+1][i]) ++count;
	                if (i-1 >= 0 && grid[j][i-1]) ++count;
	                if (i+1 <  w && grid[j][i+1]) ++count;
	                result += 4 - count;
	            }
	        }
	        
	        return result;
	    }
	};
