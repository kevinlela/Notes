### Coin Change 2
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1

[leetcode](https://leetcode.com/problems/coin-change-2/description/)

### Answer
For each coin, we have take or not take. dp[i][j] means the result of 0...i coins with amount of j

dp[i][j] = max( do not include c[i], include c[i] ) = max( dp[i-1][j], dp[i][j-c[i]] )

	class Solution {
	public:
	    int change(int amount, vector<int>& coins) {
	        if (amount == 0 && coins.size() == 0) return 1;
	        if (coins.size() == 0) return 0;
	        
	        vector<vector<int>> dp(coins.size(), vector<int> (amount + 1, 0));
	        
	        for (int j = 0; j < coins.size(); ++j)
	        {
	            dp[j][0] = 1;
	            for (int i = 1; i <= amount; i++)
	            {
	                dp[j][i] = (j - 1 >= 0 ? dp[j-1][i] : 0) + (i - coins[j] >= 0 ? dp[j][i-coins[j]] : 0);
	            }
	        }
	        
	        return dp[coins.size() - 1][amount];
	    }
	};