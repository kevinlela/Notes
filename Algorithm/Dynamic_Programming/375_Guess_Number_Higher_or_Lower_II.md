### Guess Number Higher or Lower II
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.


[leetcode](https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/)

### Answer
For every decision, we need to consider its worse case, max(left, right). and min over all decision. 

	class Solution {
	public:
	    int getMoneyAmount(int n) {
	        if (n <= 0) return 0;
	        
	        vector<vector<int>> dp(n, vector<int>(n, 0));
	        
	        for (int k = 1; k < n; ++k)
	        {
	            for (int j = 0, i = k; j < n - k; ++j, ++i)
	            {
	                dp[j][i] = INT_MAX;
	                for (int iter = j; iter <= i; ++iter)
	                {
	                    int maxPay = 0;
	                    if (iter != j) maxPay = max(maxPay, dp[j][iter - 1]);
	                    if (iter != i) maxPay = max(maxPay, dp[iter + 1][i]);
	                    dp[j][i] = min(dp[j][i], iter + 1 + maxPay);
	                }
	            }
	        }
	        
	        return dp[0][n-1];
	    }
	};
