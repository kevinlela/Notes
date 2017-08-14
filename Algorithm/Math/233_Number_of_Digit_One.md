### Number of Digit One
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

[leetcode](https://leetcode.com/problems/number-of-digit-one/description/)

### Answer
let s[i] be the 1s in [0..10^i] 
* s[1] = 1 = 1
* s[2] = 10...19 21, 31, ... 91 = 10 * s[1] + 10
* s[3] = 100...199, ...999 = 10*s[2] + 100

	class Solution {
	public:
	    int countDigitOne(int n) {
	        if (n < 0) return 0;
	        vector<int> record;
	        record.push_back(0);
	        long tmp = n, base = 1;
	        while (tmp)
	        {
	            tmp /= 10;
	            record.push_back(base + 10 * (*record.rbegin()));
	            base *= 10;
	        }
	        
	        tmp = n;
	        long result = 0, remain = 0, k = record.size() - 1;
	        base /= 10;
	        while (base)
	        {
	            long digit = tmp/base;
	            tmp %= base;
	            --k;
	            if (digit == 1) result += record[k] + tmp + 1;
	            else if (digit > 1) 
	            {
	                result += digit * record[k] + base;
	            }
	            base /= 10;
	        }
	        
	        return result;
	    }
	};