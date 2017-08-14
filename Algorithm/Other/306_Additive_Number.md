### Additive Number
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?

[leetcode](https://leetcode.com/problems/additive-number/description/)

### Answer 
* use string add to handle very large input
* the initial starting points and check

	class Solution {
	public:
	    bool isAdditiveNumber(string num) {
	        int len = num.size();
	        string s1;
	        for (int i = 0; i < len - 2; ++i)
	        {
	            s1 += num[i];
	            string s2;
	            for (int j = i + 1; j < len - 1; ++j)
	            {
	                s2 += num[j];
	                if (recur(s1, s2, num, j + 1)) return true;
	                if (s2 == "0") break;
	            }
	            if (s1 == "0") break;
	        }
	        
	        return false;
	    }
	    
	    bool recur(string s1, string s2, const string &num, int currIdx)
	    {
	        for (currIdx; currIdx < num.size(); )
	        {
	            string result = addStr(s1, s2);
	            string curr = num.substr(currIdx, result.size());
	            if (result != curr) return false;
	            currIdx += result.size();
	            s1 = s2;
	            s2 = result;
	        }
	        return true;
	    }
	    
	    string addStr(const string &s1, const string &s2)
	    {
	        int len1 = s1.size(), len2 = s2.size();
	        int iter1 = len1 - 1, iter2 = len2 - 1;
	        int carry = 0;
	        string result;
	        while (iter1 >= 0 || iter2 >= 0)
	        {
	            int digit1 = 0, digit2 = 0;
	            if (iter1 >= 0) digit1 = s1[iter1--] - '0';
	            if (iter2 >= 0) digit2 = s2[iter2--] - '0';
	            int sum = digit1 + digit2 + carry;
	            result += to_string(sum%10);
	            carry = sum / 10;
	        }
	        
	        if (carry > 0) result += to_string(carry);
	        reverse(result.begin(), result.end());
	        return result;
	    }
	};