### Array Nesting
A zero-indexed array A consisting of N different integers is given. The array contains all integers in the range [0, N - 1].

Sets S[K] for 0 <= K < N are defined as follows:

S[K] = { A[K], A[A[K]], A[A[A[K]]], ... }.

Sets S[K] are finite for each K and should NOT contain duplicates.

Write a function that given an array A consisting of N integers, return the size of the largest set S[K] for this array.

Example 1:
Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
Note:
N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of array A is an integer within the range [0, N-1].

[leetcode](https://leetcode.com/problems/array-nesting/description/)

### Answer
Is it possible that two number go to one entry? no. it is a DFS 

possible is 0->1->2->3->0

	class Solution {
	public:
	    int arrayNesting(vector<int>& nums) {
	        // it is equal to find the longest circle
	        // because 0 <= A[i] <= N-1 and each element, every starting point must end up with a circle
	        // it is not possible two elements goes to a same element
	        int len = nums.size();
	        vector<int> path(len, 0);
	        int result = 0;
	        for (int i = 0; i < len; ++i)
	        {
	            if (path[i] == 0) result = max(result, getPath(nums, i, path));
	        }
	        return result;
	    }
	    
	    int getPath(const vector<int>& nums, int idx, vector<int> &path)
	    {
	        int pLen = nums.size(), iter = idx;
	        while (path[iter] == 0)
	        {
	            path[iter] = ++pLen;
	            iter = nums[iter];
	        }
	        
	        if (path[iter] >= nums.size()) path[idx] = pLen - nums.size();
	        else path[idx] = pLen - nums.size() + path[iter];
	        
	        return path[idx];
	    }
	};