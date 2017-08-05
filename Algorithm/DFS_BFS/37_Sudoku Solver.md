### Sudoku Solver
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

[leetcode](https://leetcode.com/problems/sudoku-solver/description/)

### Answer 

	class Solution {
	public:
	    void solveSudoku(vector<vector<char>>& board) {
	        vector<pair<int, int>> needVisit;
	        int width = 9, height = 9;
	        
	        for (int j = 0; j < height; ++j)
	        {
	            for (int i = 0; i < width; ++i)
	            {
	                if (board[j][i] == '.') needVisit.push_back({j, i});
	            }
	        }
	        
	        int iter = 0;
	        while (iter >= 0 && iter < needVisit.size())
	        {
	            int j = needVisit[iter].first, i = needVisit[iter].second;
	            if (board[j][i] == '9') 
	            {
	                board[j][i] = '.';
	                --iter;
	                continue;
	            }
	            else if (board[j][i] == '.') board[j][i] = '1';
	            else board[j][i]++;
	            
	            if (checkRow(board, j) && checkCol(board, i) && checkCell(board, j, i)) ++iter;
	        }
	    }
	    
	    bool checkRow(const vector<vector<char>>& board, int row)
	    {
	        vector<bool> status(9, false);
	        for (int j = 0; j < 9; ++j)
	        {
	            if (board[row][j] == '.') continue;
	            else if (status[board[row][j] - '1'] == true) return false;
	            else status[board[row][j] - '1'] = true;
	        }
	        return true;
	    }
	    
	    bool checkCol(const vector<vector<char>>& board, int col)
	    {
	        vector<bool> status(9, false);
	        for (int i = 0; i < 9; ++i)
	        {
	            if (board[i][col] == '.') continue;
	            else if (status[board[i][col] - '1'] == true) return false;
	            else status[board[i][col] - '1'] = true;
	        }
	        return true;
	    }
	    
	    bool checkCell(const vector<vector<char>>& board, int row, int col)
	    {
	        vector<bool> status(9, false);
	        row = (row/3)*3; col = (col/3)*3;
	        for (int i = 0; i < 3; ++i)
	        {
	            for (int j = 0; j < 3; ++j)
	            {
	                if (board[row + i][col + j] == '.') continue;
	                else if (status[board[row + i][col + j] - '1'] == true) return false;
	                else status[board[row + i][col + j] - '1'] = true;
	            }
	        }
	        return true;
	    }
	};