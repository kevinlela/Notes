### Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

[leetcode](https://leetcode.com/problems/integer-to-roman/description/)

### Answer:

This problem has no techinical challenge. Just notice there is like IV, IX to record a special status, detect these status first.

	class Solution {
	public:
	    string intToRoman(int num) {
	        string result;
	        // first, M does not have prefix
	        addBynormalCase(num, 1000, 'M', result);
	        
	        if (num >= 900) addByAbnormalCase(num, 900, "CM", result); // check case 900 as CM
	        else addBynormalCase(num, 500, 'D', result); // use D as 500 instead
	        
	        if (num >= 400) addByAbnormalCase(num, 400, "CD", result);  // check case 400 as "CD"
	        else addBynormalCase(num, 100, 'C', result); // use C as 100 instead
	        
	        if (num >= 90) addByAbnormalCase(num, 90, "XC", result); // check case 90 as XC
	        else addBynormalCase(num, 50, 'L', result); // use L as 50 instead
	        
	        if (num >= 40) addByAbnormalCase(num, 40, "XL", result); // check case 40 as XL
	        else addBynormalCase(num, 10, 'X', result); // use X as 10 instead
	        
	        if (num >= 9) addByAbnormalCase(num, 9, "IX", result); // check case 9 as IX
	        else addBynormalCase(num, 5, 'V', result); // use V as 5 instead
	        
	        if (num >= 4) addByAbnormalCase(num, 4, "IV", result); // check case 4 as IV
	        else addBynormalCase(num, 1, 'I', result); // use I as 1 instead
	        
	        return result;
	    }
	    
	    void addByAbnormalCase(int &num, const int amount, const string &symbol, string &result)
	    {
	        result += symbol;
	        num -= amount;
	    }
	    
	    void addBynormalCase(int &num, const int amount, const char &symbol, string &result)
	    {
	        result += string((size_t)(num/amount), symbol);
	        num %= amount;
	    }
	};