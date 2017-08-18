### Arithmetic Slices
A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

[leetcode](https://leetcode.com/problems/arithmetic-slices/description/)

### Answer 
for a sequence, we know the number of combination of a consecutive sequence is sum(n-2 .... 1);

	class Solution {
	public:
	    int numberOfArithmeticSlices(vector<int>& A) {
	        if (A.size() < 3) return 0;
	        vector<int> groups;
	        int delta = A[1] - A[0], count = 1;
	        for (int i = 1; i < A.size(); ++i)
	        {
	            if (A[i] - A[i-1] == delta) ++count;
	            else
	            {
	                groups.push_back(count);
	                count = 2;
	                delta = A[i] - A[i-1];
	            }
	        }
	        if (count >= 3) groups.push_back(count);
	        
	        int result = 0;
	        for (int i = 0; i < groups.size(); ++i)
	        {
	            result += (groups[i] - 2) * (groups[i] - 1) / 2;
	        }
	        return result;
	    }
	    
	    
	};