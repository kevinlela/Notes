### Remove K Digits
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.


[leetcode](https://leetcode.com/problems/remove-k-digits/description/)

### Answer 
we can always pop out the previous digit which is larger than current digit and has remaining later. 

	class Solution {
	public:
	    string removeKdigits(string num, int k) {
	        stack<char> stk;
	        int len = num.size();
	        int need = len - k; // the number of digit we need
	        if (need <= 0) return "0";
	        
	        for (int i = 0; i < len; ++i)
	        {
	            int remain = len - i;
	            while (remain > need && !stk.empty())
	            {
	                if (stk.top() > num[i])
	                {
	                    stk.pop();
	                    ++need;
	                }
	                else break;
	            }
	            stk.push(num[i]);
	            --need;
	        }
	        
	        string result;
	        while (!stk.empty())
	        {
	            result += stk.top();
	            stk.pop();
	        }
	        
	        while (!result.empty())
	        {
	            if (*result.rbegin() == '0' && result.size() != 1)
	            {
	                result.pop_back();
	            }
	            else break;
	        }
	        reverse(result.begin(), result.end());
	        return result.substr(0, len - k);
	    }
	};