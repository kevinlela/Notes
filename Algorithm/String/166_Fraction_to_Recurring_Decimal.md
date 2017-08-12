### Fraction to Recurring Decimal
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

* Given numerator = 2, denominator = 1, return "2".
* Given numerator = 2, denominator = 3, return "0.(6)".
* Given numerator = 1, denominator = 2, return "0.5".

[leetcode](https://leetcode.com/problems/fraction-to-recurring-decimal/description/)

### Answer 
cycle recur at occurred remainning, so use a hashmap to store all remaining. remember to deal with corner case like negative number, 0. 

	class Solution {
	public:
	    string fractionToDecimal(int numerator, int denominator) {
	        long num = numerator, den = denominator;
	        bool neg = false;
	        if (num > 0 && den < 0) neg = true;
	        if (num < 0 && den > 0) neg = true;
	        num = abs(num);
	        den = abs(den);
	        
	        string result;
	        long x = num/den;
	        
	        if (neg) result += "-";
	        result += to_string(x);
	        
	        long decimal = num % den;
	        if (decimal == 0) return result;
	        
	        result += ".";
	        string decStr;
	        unordered_map<long, int> visited;
	        
	        int pos = 0;
	        while (decimal)
	        {
	            decimal *= 10;
	            if (visited.find(decimal) != visited.end()) break;
	            visited[decimal] = pos++;
	            decStr += to_string(decimal/den);
	            decimal %= den;
	        }
	        
	        if (decimal)
	        {
	            decStr = decStr.substr(0, visited[decimal]) 
	                    + "(" + decStr.substr(visited[decimal]) + ")";
	        }
	        
	        return result + decStr;
	    }
	};