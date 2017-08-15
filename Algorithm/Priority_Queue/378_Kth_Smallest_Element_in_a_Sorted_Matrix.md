### Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

[leetcode](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/)

### Answer

	class Solution {
	public:
	    int kthSmallest(vector<vector<int>>& matrix, int k) {
	        int n = matrix.size();
	        priority_queue<int> pq;
	        for (int j = 0; j < n; ++j)
	        {
	            for (int i = 0; i < n; ++i)
	            {
	                pq.push(matrix[j][i]);
	                if (pq.size() > k)
	                {
	                    int top = pq.top();
	                    pq.pop();
	                    if (top == matrix[j][i]) break;
	                }
	            }
	        }
	        return pq.top();
	    }   
