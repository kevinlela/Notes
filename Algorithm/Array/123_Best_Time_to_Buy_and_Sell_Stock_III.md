### Best Time to Buy and Sell Stock III
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

[leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/)

### Answer 
We can split the whole array into two part. First part s[0...i] means the first trade and second part s[i+1...N] means the second trade. Similar to [121](121_Best_Time_to_Buy_and_Sell_Stock.md). we already know how to calculate the maximum profit upto the ith day. So the first part has no problem. For the second, part, we need to calculate the maximum profit we can get if we trade on the jth day and last till the end. Also similarily, we traverse the array from the end to the begin, record the maximum value. 

	class Solution {
	public:
	    int maxProfit(vector<int>& prices) {
	        vector<int> l2rMax = leftToRightMax(prices);
	        vector<int> r2lMax = rightToLeftMax(prices);
	        
	        int len = prices.size();
	        
	        int result = 0;
	        for (int i = 0; i < len; ++i)
	        {
	            result = max(result, l2rMax[i] + r2lMax[i]);
	        }
	        
	        return result;
	    }
	    
	    vector<int> leftToRightMax(const vector<int> &prices)
	    {
	        vector<int> result(prices.size(), 0);
	        if (prices.size() <= 1) return result;
	        
	        int minVal = prices[0];
	        for (int i = 1; i < prices.size(); ++i)
	        {
	            result[i] = max(result[i-1], prices[i] - minVal);
	            minVal = min(minVal, prices[i]);
	        }
	        return result;
	    }
	    
	    vector<int> rightToLeftMax(const vector<int> &prices)
	    {
	        vector<int> result(prices.size(), 0);
	        if (prices.size() <= 1) return result;
	        
	        int len = prices.size();
	        int maxVal = prices[len-1];
	        for (int i = len - 2; i >= 0; --i)
	        {
	            result[i] = max(result[i+1], maxVal - prices[i]);
	            maxVal = max(maxVal, prices[i]);
	        }
	        return result;
	    }
	};