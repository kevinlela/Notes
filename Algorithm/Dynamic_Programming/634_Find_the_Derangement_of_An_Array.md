### Find the Derangement of An Array
In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: 3
Output: 2
Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
Note:
n is in the range of [1, 106].

[leetcode](https://leetcode.com/problems/find-the-derangement-of-an-array/description/)

### Answer
DP part:

let D[N] be the solution for N integers

for position 1 there are (N-1) possibility: switch with ith
for position i there are (N-1) possibility but need decompose
* 1  : when 1 is on that position, so this case has D[N-2]
* N-2: when i is not on ith position, instead, j is on that postion so the it can be decomposed again
	* 1 : when 1 is on j so it has D[N-3]
	* N-3: when 1 is not on j, so decomposed again

D[N] = (N-1)*{D[N-2] + (N-2){D[N-3] + (N-3)...}}
     = (N-1)*{D[N-2] + D[N-1]}

Modular part:

(A+B)%m = (A%m + B%m)%m
(A\*B)%m = (A%m \* B%m)%m

M[N] = D[N]%m
	 = {(N-1)%m \* {(D[N-2]%m + D[N-1]%m)%m}}%m
	 = {(N-1)%m \* {(M[N-2] + M[N-1])%m}}%m
	 = {(N-1)\*(M[N-2] + M[N-1])}%m

	class Solution {
	public:
	    int findDerangement(int n) {
	        if (n <= 1) return 0;
	        long dp1 = 0; // for 1
	        long dp2 = 1; // for 2
	        
	        d_m = 1000000007;
	        for (int i = 3; i <= n; ++i)
	        {
	            int dp1tmp = dp2;
	            dp2 = (i - 1)*(dp1 + dp2) % d_m;
	            dp1 = dp1tmp;
	        }
	        
	        return dp2;
	    }
	private:
	    long d_m;
	};