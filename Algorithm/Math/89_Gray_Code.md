### Gray Code
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

[leetcode](https://leetcode.com/problems/gray-code/description/)

### Answer 
It is very similar to [60](60_Permutation_Sequence) but the period change to be 2^n. flip and append every 2^n

	class Solution {
	public:
	    vector<int> grayCode(int n) {
	        vector<int> result;
	        result.push_back(0);
	        if (n == 0) return result;
	        result.push_back(1);
	        if (n == 1) return result;
	        
	        n -= 1;
	        int basis = 2;
	        while (n-- > 0)
	        {
	            for (int i = result.size() - 1; i >= 0; --i)
	            {
	                result.push_back(result[i] | basis);
	            }
	            basis <<= 1;
	        }
	        
	        return result;
	    }
	};