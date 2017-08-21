### Ones and Zeroes
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

[leetcode]()

### Answer
This is knapsack problem but two variables

kth string can be represent as o[k], and z[k]. The total volume you have is O and Z

we construct a dp array dp[i][j][k]; 0<= i <= O, 0 <= j <= Z

for every dp[i][j][k], we decide whether we take k or not
1) take k
	* dp[i][j][k] = dp[i - o[k]]dp[j - z[k]][k-1] + 1
2) not take k : same as we only use k - 1
	* dp[i][j][k] = dp[i][j][k-1]

	class Solution {
	public:
	    int findMaxForm(vector<string>& strs, int m, int n) {
	        vector<pair<int, int>> counts = count_m_n(strs);
	        int len = strs.size();
	        // m is 0, n is 1
	        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
	        vector<vector<int>> prev(n + 1, vector<int>(m + 1, 0));
	        for (int k = 1; k <= len; k++)
	        {
	            for (int j = 0; j <= n; ++j)
	            {
	                for (int i = 0; i <= m; ++i)
	                {
	                    int c0 = counts[k - 1].first, c1 = counts[k - 1].second;
	                    if (i - c0 < 0 || j - c1 < 0) dp[j][i] = prev[j][i];
	                    else dp[j][i] = max(prev[j - c1][i -  c0] + 1, prev[j][i]);
	                }
	            }
	            
	            for (int j = 0; j <= n; ++j)
	            {
	                for (int i = 0; i <= m; ++i)
	                {
	                    prev[j][i] = dp[j][i];
	                    dp[j][i] = 0;
	                }
	            }
	        }
	        return prev[n][m];
	    }
	    
	    vector<pair<int, int>> count_m_n(const vector<string> &strs)
	    {
	        vector<pair<int, int>> counts;
	        for (int i = 0; i < strs.size(); ++i)
	        {
	            pair<int, int> count = {0, 0};
	            for (int j = 0; j < strs[i].size(); ++j)
	            {
	                if (strs[i][j] == '0') ++count.first;
	                else ++count.second;
	            }
	            counts.push_back(count);
	        }
	        return counts;
	    }
	};

