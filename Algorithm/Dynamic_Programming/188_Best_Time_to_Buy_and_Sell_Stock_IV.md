### Best Time to Buy and Sell Stock IV
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

[leetcode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/)

### Answer 
For stock problem, there are two status, buy and sell. b[.] and s[.]. 
lef s[k][i] denotes the sell status for kth transaction on ith day
lef b[k][i] denotes the sell status for kth transaction on ith day

the s[k][i] comes from
	* b[k][i] + v[i] : sell the current hold
	* s[k][i-1] : keep the current hold
the b[k][i] comes from
	* s[k-1][i-1] - v[i]: after sell at k-1 th transaction
	* b[k][i-1] : keep the current hold

Both of them dp to max.

One trick, when k is larger than number of days, we go back to [122](122_Best_Time_to_Buy_and_Sell_Stock_II).

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int pnum = prices.size();
        
        if (k < 1 || pnum < 1) return 0;
        
        if (k >= pnum) return incremental(prices);
        
        vector<vector<int>> b(k, vector<int> (pnum + 1, 0));
        vector<vector<int>> s(k, vector<int> (pnum + 1, 0));
        
        b[0][0] = INT_MIN;
        
        int result = 0;
        for (int i = 1, j = 0; i <= pnum; ++i)
        {
            b[j][i] = max(b[j][i-1], -prices[i-1]);
            s[j][i] = max(s[j][i-1], b[j][i-1] + prices[i-1]);
            
        }
        
        result = max(s[0][pnum], result);
        
        for (int j = 1; j < k; ++j)
        {
            b[j][0] = INT_MIN;
            for (int i = 1; i <= pnum; ++i)
            {
                b[j][i] = max(b[j][i-1], -prices[i-1] + s[j-1][i-1]);
                s[j][i] = max(s[j][i-1], b[j][i-1] + prices[i-1]);
            }
            result = max(s[j][pnum], result);
        }
        
        return result;
    }
    
    int incremental(vector<int> &prices)
    {
        int result = 0;
        int pnum = prices.size();
        
        for (int k = 1; k < pnum; ++k)
        {
            result += max(prices[k] - prices[k - 1], 0);
        }
        
        return result;
    }
};
