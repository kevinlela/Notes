### Counting Bits
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

[leetcode](https://leetcode.com/problems/counting-bits/description/)

### Answer 

0000
0001
0010
0011
0100
0101
0110
0111

Period *= period * 2

	class Solution {
	public:
	    vector<int> countBits(int num) {
	        // 00000000 0
	        // 00000001 1
	        // 00000010 2
	        // 00000011 3
	        // 00000100 4
	        // 00000101 5
	        // 00000110 6
	        // 00000111 7
	        
	        vector<int> result(1, 0);
	        if (num == 0) return result;
	        result.push_back(1);
	        if (num == 1) return result;
	        
	        int period = 2;
	        while (1)
	        {
	            for (int i = 0; i < period; ++i)
	            {
	                result.push_back(result[i] + 1);
	                if (result.size() == num + 1) return result;
	            }
	            period *= 2;
	        }
	        
	        return result;
	    }
	};