### Ugly Number II
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

[leetcode](https://leetcode.com/problems/ugly-number-ii/description/)

### Answer 
2\*1 2\*2 2\*3 2\*5 2\*6 ...

3\*1 3\*2 3\*3 3\*5 3\*6 ...

5\*1 5\*2 5\*3 5\*5 5\*6 ...


The base is the calculated ugly number

	class Solution {
	public:
	    int nthUglyNumber(int n) {
	        // ugly numbers are 
	        // 1x2 2x2 2x3 2x4
	        // 1x3 3x2 3x3 3x4
	        // 1x5 5x2 5x3 5x4
	        
	        vector<int> uglynums(n, 1);
	        int iter2 = 0, iter3 = 0, iter5 = 0;
	        
	        for (int i = 1; i < n; ++i)
	        {
	            int res2 = uglynums[iter2] * 2;
	            int res3 = uglynums[iter3] * 3;
	            int res5 = uglynums[iter5] * 5;
	            int res = min(res2, min(res3, res5));
	            if (res2 == res) ++iter2;
	            if (res3 == res) ++iter3;
	            if (res5 == res) ++iter5;
	            uglynums[i] = res;
	        }
	        
	        return uglynums[n-1];
	    }
	};