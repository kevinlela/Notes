### Strobogrammatic Number
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

[leetcode](https://leetcode.com/problems/strobogrammatic-number/description/)

### Answer
	class Solution {
	public:
	    bool isStrobogrammatic(string num) {
	        // what is the letter?
	        // 1, 6, 8, 9, 0
	        if (num.empty()) return true;
	        
	        unordered_map<char, char> m = {{'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};
	        int len = num.size() - 1, mid = len/2;
	        for (int i = 0; i <= mid; ++i)
	        {
	            auto it = m.find(num[i]);
	            if (it == m.end()) return false;
	            if (it->second != num[len - i]) return false;
	        }
	        
	        return true;
	    }
	};