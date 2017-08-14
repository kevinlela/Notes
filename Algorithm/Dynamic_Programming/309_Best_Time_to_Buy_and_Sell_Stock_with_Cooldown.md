### Best Time to Buy and Sell Stock with Cooldown
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

* You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
* After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]

[leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/)

### Answer 

similar to [188](188_Best_Time_to_Buy_and_Sell_Stock_IV.md). However, we need add one more status cooldown. 

* b[i] = min(b[i], c[i-1] - v[i])
* c[i] = s[i-1]
* s[i] = min(s[i-1], b[i-1]+v[i])

	class Solution {
	public:
	    int maxProfit(vector<int>& prices) {
	        int len = prices.size();
	        vector<int> buy(len+1, INT_MIN);
	        vector<int> sell(len+1, 0);
	        vector<int> cool(len+1, 0);
	        int result = 0;
	        
	        for (int i = 1; i <= len; ++i)
	        {
	            buy[i] = max( buy[i - 1], cool[i - 1] - prices[i - 1]); // buy from not buy and buy
	            sell[i] = max( buy[i - 1] + prices[i - 1], sell[i - 1]); // sell comes from either not sell or sell 
	            cool[i] = sell[i - 1];  // cool down only comes from the sell 
	            
	            result = max(result, sell[i]);
	            result = max(result, cool[i]);
	        }
	        
	        return result;
	    }
	};