### Complex Number Multiplication
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.

[leetcode](https://leetcode.com/problems/complex-number-multiplication/description/)

### Answer

	class Solution {
	public:
	    string complexNumberMultiply(string a, string b) {
	        int aRe = 0, aIm = 0, bRe = 0, bIm = 0;
	        decomp(a, aRe, aIm);
	        decomp(b, bRe, bIm);
	        int cRe = aRe*bRe - aIm*bIm;
	        int cIm = aRe*bIm + aIm*bRe;
	        return to_string(cRe) + "+" + to_string(cIm) + "i";
	    }
	    
	    void decomp(const string &s, int &re, int &im)
	    {
	        re = 0; 
	        im = 0;
	        int sp = s.find_first_of('+');
	        if (sp != -1) re = atoi(s.substr(0, sp).c_str());
	        int si = s.find_first_of('i', sp);
	        if (si != -1) im = atoi(s.substr(sp+1, si).c_str());
	    }
	};