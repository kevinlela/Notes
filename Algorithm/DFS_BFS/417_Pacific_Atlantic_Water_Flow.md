### Pacific Atlantic Water Flow
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

[leetcode](https://leetcode.com/problems/pacific-atlantic-water-flow/description/)

### Answer 
You can use dfs for every coordinate, or use bfs, starts from all boundary points

	class Solution {
	public:
	    vector<pair<int, int>> pacificAtlantic(vector<vector<int>>& matrix) {
	        vector<pair<int, int>> result;
	        int h = matrix.size();
	        if (h == 0) return result;
	        int w = matrix[0].size();
	        if (w == 0) return result;
	        
	        queue<pair<int, int>> pacific;
	        vector<vector<bool>> pacific_visited(h, vector<bool> (w, false));
	        for (int i = 0; i < w; ++i)
	        {
	            pacific.push({0, i});
	            pacific_visited[0][i] = true;
	        }
	        
	        for (int j = 1; j < h; ++j)
	        {
	            pacific.push({j, 0});
	            pacific_visited[j][0] = true;
	        }
	        
	        bfs(pacific, pacific_visited, matrix);
	        
	        queue<pair<int, int>> atlantic;
	        vector<vector<bool>> atlantic_visited(h, vector<bool> (w, false));
	        for (int i = 0; i < w; ++i)
	        {
	            atlantic.push({h-1, i});
	            atlantic_visited[h-1][i] = true;
	        }
	        
	        for (int j = 0; j < h-1; ++j)
	        {
	            atlantic.push({j, w-1});
	            atlantic_visited[j][w-1] = true;
	        }
	        
	        bfs(atlantic, atlantic_visited, matrix);
	        
	        for (int j = 0; j < h; ++j)
	        {
	            for (int i = 0; i < w; ++i)
	            {
	                if (atlantic_visited[j][i] && pacific_visited[j][i]) result.push_back({j, i});
	            }
	        }
	        
	        return result;
	    }
	    
	    void bfs(queue<pair<int, int>> &locs, vector<vector<bool>> &visited, vector<vector<int>> &matrix)
	    {
	        int h = visited.size(), w = visited[0].size();
	        vector<pair<int, int>> shift = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	        while(!locs.empty())
	        {
	            int len = locs.size();
	            for (int i = 0; i < len; ++i)
	            {
	                int col = locs.front().second;
	                int row = locs.front().first;
	                for (int j = 0; j < 4; ++j)
	                {
	                    int t_r = row + shift[j].first;
	                    int t_c = col + shift[j].second;
	                    if (t_r >= 0 && t_r < h && t_c >= 0 && t_c < w &&
	                        visited[t_r][t_c] == false && matrix[t_r][t_c] >= matrix[row][col])
	                    {
	                        visited[t_r][t_c] = true;
	                        locs.push({t_r, t_c});
	                    }
	                }
	                locs.pop();
	            }
	        }
	    }
	};