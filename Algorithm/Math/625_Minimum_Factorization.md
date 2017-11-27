### Minimum Factorization
Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.

If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

Example 1
Input:

48 
Output:
68
Example 2
Input:

15
Output:
35

[leetcode]()

### Answer
factor cannot be 2 digit. 

	class Solution {
	public:
	    int smallestFactorization(int a) {
	        if (a < 10) return a;
	        
	        vector<int> factors(8, 0);
	        int count = 0;
	        while (a != 1)
	        {
	            int i = 9;
	            for (i; i >= 2; --i)
	            {
	                if (a % i == 0) 
	                {
	                    ++factors[i-2];
	                    a /= i;
	                    if (++count > 32) return 0;
	                    break;
	                }
	            }
	            
	            if (i == 1) return 0;
	        }
	        
	        long result = 0;
	        for (int i = 0; i < 8; )
	        {
	            if (factors[i] == 0) ++i;
	            else
	            {
	                result = 10*result + i + 2;
	                --factors[i];
	                if (result > INT_MAX) return 0;
	            }
	        }
	        
	        return result;
	    }
	};