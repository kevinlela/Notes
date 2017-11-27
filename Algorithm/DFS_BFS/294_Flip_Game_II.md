### Flip Game II
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.

[leetcode](https://leetcode.com/problems/flip-game-ii/description/)

### Answer

it is a dfs with memorization problem

	class Solution {
	public:
	    bool canWin(string s) {
	        return recur(s);
	    }
	    
	    bool recur(string &s)
	    {
	        if (memo.find(s) != memo.end())
	            return memo[s];
	        
	        int i = 0, len = s.size();
	        for (i = 0; i < len - 1; ++i)
	        {
	            if (s[i] == '+' && s[i+1] == '+')
	            {
	                s[i]   = '-';
	                s[i+1] = '-';
	                bool nextWin = recur(s); 
	                memo[s] = nextWin;
	                s[i]   = '+';
	                s[i+1] = '+';
	                if(nextWin == false) return true;// current player win, when there is a solution make all attempts of the next plan fail
	            }
	        }
	        
	        return false;
	    }
	private:
	    unordered_map<string, bool> memo;
	};