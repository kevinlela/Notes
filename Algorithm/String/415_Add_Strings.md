### Add Strings
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


[leetcode](https://leetcode.com/problems/add-strings/description/)

### Answer 

	class Solution {
	public:
	    string addStrings(string num1, string num2) {
	        int carry = 0;
	        int iter1 = num1.size(), iter2 = num2.size();
	        --iter1;
	        --iter2;
	        string result;
	        while (iter1 >= 0 || iter2 >= 0)
	        {
	            int a = 0, b = 0;
	            if (iter2 >= 0) b = num2[iter2--] - '0';
	            if (iter1 >= 0) a = num1[iter1--] - '0';
	            int curr = a + b + carry;
	            carry = curr / 10;
	            curr = curr % 10;
	            result += to_string(curr);
	        }
	        
	        if (carry != 0) result += to_string(carry);
	        reverse(result.begin(), result.end());
	        return result;
	    }
	    
	};