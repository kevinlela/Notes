### Plus One
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

[leetcode](https://leetcode.com/problems/plus-one/description/)

### Answer 

	class Solution {
	public:
	    vector<int> plusOne(vector<int>& digits) {
	        int carry = 1, len = digits.size();
	        if (len == 0) return vector<int> (1, 1);
	        
	        vector<int> result;
	        for (int i = len - 1; i >= 0; --i)
	        {
	            int curr = digits[i] + carry;
	            carry = curr/10;
	            result.push_back(curr%10);
	        }
	        
	        if (carry != 0) result.push_back(carry);
	        reverse(result.begin(), result.end());
	        return result;
	    }
	};