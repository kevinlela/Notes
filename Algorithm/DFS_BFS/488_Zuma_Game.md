### Zuma Game
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 

Note:
You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.

[leetcode](https://leetcode.com/problems/zuma-game/description/)

### Answer

This is a brutal force dfs problem. 

	class Solution {
	public:
	    int findMinStep(string board, string hand) {
	        unordered_map<char, int> handCount;
	        for (int j = 0; j < hand.size(); ++j)
	        {
	            ++handCount[hand[j]];
	        }
	        int num = hand.size();
	        return recur(board, handCount, num, num);
	    }
	    
	    int recur(string board, unordered_map<char, int> &hand, int numBalls, const int& allballs)
	    {
	        board = removeConsecutive(board);
	        if (board.empty()) 
	        {
	            return allballs - numBalls;
	        }
	        if (numBalls == 0) return -1;
	        
	        int result = INT_MAX;
	        int len = board.size();
	        char curr = ' ';
	        for (int i = 0; i < len; ++i)
	        {
	            if (board[i] == curr) continue;
	            
	            curr = board[i];
	            if (hand[curr] == 0) continue;
	            
	            board.insert(board.begin() + i, curr);
	            
	            --hand[curr];
	            int curr_res = recur(board, hand, numBalls - 1, allballs);
	            if (curr_res != -1) result = min(curr_res, result);
	            ++hand[curr];
	            
	            board.erase(i, 1);
	        }
	        
	        return result == INT_MAX ? -1 : result;
	    }
	    
	    string removeConsecutive(const string &board)
	    {
	        string result;
	        if (board.empty()) return result;
	        char curr = board[0];
	        int num = 1;
	        
	        for (int i = 1; i < board.size(); ++i)
	        {
	            if (board[i] != curr)
	            {
	                if (num < 3) result.append(num, curr); 
	                curr = board[i];
	                num = 1;
	            }
	            else ++num;
	        }
	        
	        if (num < 3) result.append(num, curr); 
	        
	        if (result.size() == board.size()) return result;
	        return removeConsecutive(result);
	    }
	};
