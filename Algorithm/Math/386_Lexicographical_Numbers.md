### Lexicographical Numbers
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

[leetcode](https://leetcode.com/problems/lexicographical-numbers/description/)

### Answer 
The natural way is to use stack to store like 1, 10, 100, 1000 ..., However, a trick here is to avoid using stack by dividing by 10. 

	class Solution {
	public:
	    vector<int> lexicalOrder(int n) {
	        vector<int> result;
	        if (n < 1) return result;
	        int curr = 0;
	        int i = 0;
	        while (i++ < n)
	        {
	            curr += 1;
	            if (curr % 10 == 0) curr = (curr - 1) / 10;
	            else 
	            {
	                while (curr <= n)
	                {
	                    result.push_back(curr);
	                    curr *= 10;
	                }
	            }
	            if (curr > n) curr /= 10;
	        }
	        
	        return result;
	    }
	};