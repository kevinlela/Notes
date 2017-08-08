### Triangle
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

[leetcode](https://leetcode.com/problems/triangle/description/)

### Answer 
This problem acually is the same as [62](62_Unique_Paths.md)

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        // dp[j][i] = min(dp[j-1][i], dp[j-1][i-1]) + t[j][i]
        
        int numRows = triangle.size();
        if (numRows <= 0) return 0;
        vector<int> dp(numRows, INT_MAX);
        
        dp[0] = triangle[0][0];
        for (int j = 1; j < numRows; ++j)
        {
            int prev = dp[0];
            dp[0] += triangle[j][0]; // no choice for the first one
            
            for (int i = 1; i <= j; ++i)
            {
                //cout << i << " " << j << endl;
                int tmp = dp[i];
                dp[i] = min(prev, dp[i]) + triangle[j][i];
                prev = tmp;
            }
        }
        
        int result = INT_MAX;
        for (int i = 0; i < numRows; ++i)
        {
            result = min(result, dp[i]);
        }
        
        return result;
    }
};