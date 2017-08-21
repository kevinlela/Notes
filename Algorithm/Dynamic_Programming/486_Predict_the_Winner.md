### Predict the Winner
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.

[leetcode](https://leetcode.com/problems/predict-the-winner/description/)

### Answer
1) we can use dfs with memorization. we can use the starting index and ending index/length to record the win or lose. 

2) we can use dp to solve this problem. 
	* if len is 1, p1 always wins
	* if len is 2, p1 always wins by choosing the maximum among 2
	* if len is 3, p1 wins if max( n[0] + dp[1...2], n[2] + dp[0...1])
	* if len is k, p1 wins if max( n[0] + dp[1...k-1], n[k-1] + dp[0...k-2])
	* dp[m...n] means the minimum score the player 1 can get if starts with player2. it is equal to sum[0...k-1] - max( n[0] + dp[1...k-1], n[k-1] + dp[0...k-2]) : switch the pos of p1 and p2.

	class Solution {
	public:
	    bool PredictTheWinner(vector<int>& nums) {
	        int len = nums.size();
	        if (len == 1) return true;
	        
	        vector<vector<int>> dp1(len, vector<int>(len, false));
	        vector<int> sum(len, 0);
	        int tmp = 0;
	        for (int i = 0; i < len; ++i)
	        {
	            dp1[i][i] = nums[i];
	            sum[i] = tmp + nums[i];
	            tmp = sum[i];
	        }
	        
	        for (int j = 0, i = 1; j < len - 1; ++j, ++i)
	        {
	            dp1[j][i] = max(nums[j], nums[i]);
	        }
	        
	        for (int k = 2; k < len; ++k)
	        {
	            for (int i = 0, j = k; i < len - k; ++j, ++i)
	            {
	                int l1 = sum[j] - sum[i]; //sum[i+1...j]
	                int l2 = sum[j-1] - (i == 0 ? 0 : sum[i-1]); //sum[i...j-1]
	                dp1[i][j] = max( nums[i] + l1 - dp1[i+1][j], 
	                                 nums[j] + l2 - dp1[i][j-1] );
	            }
	        }
	        
	        return dp1[0][len-1] >= sum[len-1] - dp1[0][len-1];
	    }
	};