### Paint Fence
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.


[leetcode](https://leetcode.com/problems/paint-fence/description/)

### Answer
dp[0] = k
dp[1] = k*(k-1) + k = dp1[1] + dp2[1] = non_consecutive + consecutive
dp[2] = [dp1[1]*(k-1) + dp2[1]*(k-1)] + dp1[1] = dp1[2] + dp2[2]

	class Solution {
	public:
	    int numWays(int n, int k) {
	        if (n == 0 || k <= 0) return 0;
	        if (n == 1) return k;
	        if (n == 2) return k*k;
	        int prev1 = k*(k-1), prev2 = k;
	        for (int i = 2; i < n; ++i)
	        {
	            int prev1_tmp = prev1*(k-1) + prev2*(k-1);
	            prev2 = prev1;
	            prev1 = prev1_tmp;
	            //cout << prev1 << " " << prev2 << endl;
	        }
	        return prev1 + prev2;
	    }
	};