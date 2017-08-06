### Add Binary
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

[leetcode](https://leetcode.com/problems/add-binary/description/)

### Answer 
	class Solution {
	public:
	    string addBinary(string a, string b) {
	        int lenA = a.size(), lenB = b.size();
	        if (lenA == 0) return b;
	        if (lenB == 0) return a;
	        
	        int i = lenA-1, j = lenB-1;
	        int carry = 0;
	        string result;
	        while (i >= 0 || j >= 0)
	        {
	            int aDigit = 0, bDigit = 0;
	            if (i >= 0) aDigit = a[i--] - '0';
	            if (j >= 0) bDigit = b[j--] - '0';
	            int curr = aDigit + bDigit + carry;
	            carry = curr/2;
	            curr %= 2;
	            result.append(1, curr + '0');
	        }
	        
	        if (carry) result.append(1, '1');
	        reverse(result.begin(), result.end());
	        return result;
	    }
	};