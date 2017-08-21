### 4Sum II
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

[leetcode](https://leetcode.com/problems/4sum-ii/description/)

### Answer
O(N^2) for A+B and C+D. Use hash map to calculate 0, so total O(N^2)

	class Solution {
	public:
	    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
	        unordered_map<int, int> myMap;
	        
	        int len = A.size();
	        for (int j = 0; j < len; ++j)
	        {
	            for (int i = 0; i < len; ++i)
	            {
	                ++myMap[A[j] + B[i]];
	            }
	        }
	        
	        int result = 0;
	        for (int j = 0; j < len; ++j)
	        {
	            for (int i = 0; i < len; ++i)
	            {
	                if (myMap.find(-C[j] - D[i]) != myMap.end())
	                    result += myMap[-C[j] - D[i]];
	            }
	        }
	        
	        return result;
	    }
	};
