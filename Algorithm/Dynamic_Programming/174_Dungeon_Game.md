### Dungeon Game
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

|||
---|---|---
-2 (K)	|-3	 	| 3
-5	    |-10	|  1
10	    | 30	|  -5 (P6

[leetcode](https://leetcode.com/problems/dungeon-game/description/)

### Answer 

	class Solution {
	public:
	    int calculateMinimumHP(vector<vector<int>>& dungeon) {
	        int h = dungeon.size();
	        if (h == 0) return 1;
	        int w = dungeon[0].size();
	        if (w == 0) return 1;
	        
	        vector<vector<int>> dp(h, vector<int> (w, 0));
	        
	        dp[h-1][w-1] = dungeon[h-1][w-1] >= 0 ? 1 : (-dungeon[h-1][w-1] + 1);
	        
	        for (int j = h - 1, i = w - 2; i >= 0; --i)
	        {
	            dp[j][i] = max(dp[j][i + 1] - dungeon[j][i], 1);
	        }
	        
	        for (int j = h - 2, i = w - 1; j >= 0; --j)
	        {
	            dp[j][i] = max(dp[j+1][i] - dungeon[j][i], 1);
	        }
	        
	        
	        for (int j = h - 2; j >= 0; --j)
	        {
	            for (int i = w - 2; i >= 0; --i)
	            {
	                dp[j][i] = min(max(dp[j][i + 1] - dungeon[j][i], 1), 
	                               max(dp[j + 1][i] - dungeon[j][i], 1));
	            }
	        }
	        
	        return dp[0][0];
	    }
	};