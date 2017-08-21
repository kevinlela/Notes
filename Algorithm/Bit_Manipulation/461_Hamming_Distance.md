### Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ?   ?

The above arrows point to positions where the corresponding bits are different.

[leetcode](https://leetcode.com/problems/hamming-distance/description/)

### Answer
Xor and count bit

	class Solution {
	public:
	    int hammingDistance(int x, int y) {
	        int res = x^y, count = 0;
	        while (res)
	        {
	            count += res & 1;
	            res >>= 1;
	        }
	        return count;
	    }
	};
