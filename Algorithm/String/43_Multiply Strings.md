### Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

[leetcode](https://leetcode.com/problems/multiply-strings/description/)

### Answer 
	class Solution {
	public:
	    string multiply(string num1, string num2) {
	        string result;
	        int len1 = num1.size(), len2 = num2.size();
	        vector<int> carryCol(len2, 0);
	        int carry = 0;
	        for (int k = 0; k < len1 + len2; ++k)
	        {
	            int sum = carry;
	            for (int j = 0; j < len2; ++j)
	            {
	                int i = k - j;
	                if (i < 0 || i >= len1)
	                {
	                    sum += carryCol[j];
	                    carryCol[j] = 0;
	                }
	                else
	                {
	                    int curr = (int)(num1[len1 - i - 1] - '0') * (int)(num2[len2 - j - 1] - '0') + carryCol[j];
	                    carryCol[j] = curr / 10;
	                    sum += curr % 10;
	                }
	            }
	            carry = sum / 10;
	            result.append(1, '0' + sum % 10);
	        }

	        int lenR = result.size();
	        for (int i = 0; i < lenR; i++)
	        {
	            if (*(result.rbegin()) == '0') result.pop_back();
	            else break;
	        }
	        
	        reverse(result.begin(), result.end());
	        return result.empty() ? "0" : result;
	    }
	};