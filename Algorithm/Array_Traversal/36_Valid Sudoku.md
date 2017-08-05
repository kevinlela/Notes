### Valid Sudoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

### Answer 

	class Solution {
	public:
	    bool isValidSudoku(vector<vector<char>>& board) {
	        // check row
	        for (int i = 0; i < 9; ++i)
	        {
	            if (!checkRow(board, i)) return false;
	        }
	        
	        //check column
	        for (int j = 0; j < 9; ++j)
	        {
	            if (!checkCol(board, j)) return false;
	        }
	        
	        //check cell
	        for (int i = 0; i < 9; i = i + 3)
	        {
	            for (int j = 0; j < 9; j = j + 3)
	            {
	                if (!checkCell(board, i, j)) return false;
	            }
	        }
	        
	        return true;
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