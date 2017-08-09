### Surrounded Regions
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

[leetcode](https://leetcode.com/problems/surrounded-regions/description/)

### Answer 
We can always use dfs and bfs to solve this problem, the complexity is the same. Therefore, either of them will meet extreme case, for dfs, if the connected region like a snake, that will case stak overflow (recur too deep). But, iterative dfs can solve it. For BFS, if it meets flat tree, it consumes more memory. 

	class Solution {
	public:
	    void solve(vector<vector<char>>& board) {
	        int h = board.size();
	        if (h == 0) return;
	        int w = board[0].size();
	        if (w == 0) return;
	        
	        for (int j = 0, i = 0; j < h; ++j)
	        {
	            if (board[j][i] == 'O') BFS(board, j, i, h, w);
	        }
	        
	        for (int j = 0, i = w-1; j < h; ++j)
	        {
	            if (board[j][i] == 'O') BFS(board, j, i, h, w);
	        }
	        
	        for (int j = 0, i = 0; i < w; ++i)
	        {
	            if (board[j][i] == 'O') BFS(board, j, i, h, w);
	        }
	        
	        for (int j = h-1, i = 0; i < w; ++i)
	        {
	            if (board[j][i] == 'O') BFS(board, j, i, h, w);
	        }
	        
	        for (int j = 0; j < h; ++j)
	        {
	            for (int i = 0; i < w; ++i)
	            {
	                if (board[j][i] == 'F') board[j][i] = 'O';
	                else if (board[j][i] == 'O') board[j][i] = 'X';
	            }
	        }
	    }
	    
	    void BFS(vector<vector<char>>& board, int j, int i, int h, int w)
	    {
	        board[j][i] = 'F';
	        queue<pair<int, int>> cands;
	        cands.push({j, i});
	        
	        while (!cands.empty())
	        {
	            int qLen = cands.size();
	            for (int k = 0; k < qLen; ++k)
	            {
	                int row = cands.front().first;
	                int col = cands.front().second;
	                if (row + 1 < h  && board[row+1][col] == 'O') 
	                {
	                    board[row+1][col] = 'F';
	                    cands.push({row+1, col});
	                }
	                if (row - 1 >= 0 && board[row-1][col] == 'O') 
	                {
	                    board[row-1][col] = 'F';
	                    cands.push({row-1, col});
	                }
	                if (col + 1 < w  && board[row][col+1] == 'O') 
	                {
	                    board[row][col+1] = 'F';
	                    cands.push({row, col+1});
	                }
	                if (col - 1 >= 0 && board[row][col-1] == 'O') 
	                {
	                    board[row][col-1] = 'F';
	                    cands.push({row, col-1});
	                }
	                cands.pop();
	            }
	        }
	    }
	};