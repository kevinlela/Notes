### Game of Life
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

[leetcode](https://leetcode.com/problems/game-of-life/description/)

### Answer 
Traditionally, we store the original status and only update the result matrix. In this problem, if we want to do it in place, we need to introduce bits for previous status. 

	class Solution {
	public:
	    void gameOfLife(vector<vector<int>>& board) {
	        // live-live = 11
	        // live-dead = 01
	        // dead-live = 10
	        // dead-dead = 00
	        
	        int mask = 1, stg2 = 2;
	        int h = board.size();
	        if (h == 0) return;
	        int w = board[0].size();
	        
	        for (int j = 0; j < h; ++j)
	        {
	            for (int i = 0; i < w; ++i)
	            {
	                int count_live = 0;
	                for (int n = max(j - 1, 0); n < min( j + 2, h); ++n)
	                {
	                    for (int m = max(i - 1, 0); m < min(i + 2, w); ++m)
	                    {
	                        //cout << n << ", " << m << endl;
	                        if (n == j && m == i) continue;
	                        if (board[n][m] & mask)
	                            ++count_live;
	                    }
	                }
	                //if (count_live < 2) die
	                //cout << count_live << endl;
	                if (board[j][i])
	                {
	                    if (count_live == 2 || count_live == 3) 
	                        board[j][i] |= stg2;
	                }
	                else
	                {
	                    if (count_live == 3) 
	                        board[j][i] |= stg2;
	                }
	                //if (count_live > 3) die
	            }
	        }
	        
	        for (int j = 0; j < h; ++j)
	        {
	            for (int i = 0; i < w; ++i)
	            {
	                ///cout << board[j][i] << endl;
	                board[j][i] >>= 1;
	            }
	        }
	        
	    }
	};