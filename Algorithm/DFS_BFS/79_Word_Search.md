### Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.


[leetcode](https://leetcode.com/problems/word-search/description/)

### Answer 

	class Solution {
	public:
	    bool exist(vector<vector<char>>& board, string word) {
	        int h = board.size(), len = word.size();
	        if (len == 0) return true;
	        if (h == 0) return false;
	        int w = board[0].size();
	        if (w == 0) return false;
	        
	        vector<vector<bool>> visited(h, vector<bool> (w, false));
	        for (int j = 0; j < h; ++j)
	        {
	            for (int i = 0; i < w; ++i)
	            {
	                if (dfs(board, word, visited, 0, j, i)) return true;
	            }
	        }
	        
	        return false;
	    }
	    
	    bool dfs(const vector<vector<char>> &board, const string &word, 
	             vector<vector<bool>> &visited, int curr, int row, int col)
	    {
	        int h = board.size(), w = board[0].size(), len = word.size();
	        if (curr == len) return true;
	        if (row >= h || row < 0 || col >= w || col < 0) return false;
	        if (visited[row][col]) return false;
	        if (board[row][col] != word[curr]) return false;
	        
	        bool result = false;
	        
	        visited[row][col] = true;
	        if (dfs(board, word, visited, curr + 1, row + 1, col)) result = true;
	        else if (dfs(board, word, visited, curr + 1, row - 1, col)) result = true;
	        else if (dfs(board, word, visited, curr + 1, row, col + 1)) result = true;
	        else if (dfs(board, word, visited, curr + 1, row, col - 1)) result = true;
	        visited[row][col] = false;
	        
	        return result;
	    }
	};