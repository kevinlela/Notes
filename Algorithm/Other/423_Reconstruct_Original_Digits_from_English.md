### Reconstruct Original Digits from English
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"

[leetcode](https://leetcode.com/problems/reconstruct-original-digits-from-english/description/)

### Answer 
It is a exclusion or decision tree problem

	class Solution {
	public:
	    string originalDigits(string s) {
	        // write down the english first
	        // zero, one, two, three, four, five, six, seven, eight, nine
	        // two has unique w
	        // four has unique u
	        // eight has unique g
	        // six has unique x
	        // zero has unique z
	        // rest: one, three, five seven, nine
	        // then, f defines five, s defines seven, o defines one, t defines three
	        // rest: nine
	        
	        vector<int> counts(26, 0);
	        vector<int> numCounts(10, 0);
	        
	        for (int k = 0; k < s.size(); ++k)
	        {
	            ++counts[s[k] - 'a'];
	        }
	        
	        numCounts[0] += getNum(counts, "zero",  'z');
	        numCounts[2] += getNum(counts, "two",   'w');
	        numCounts[4] += getNum(counts, "four",  'u');
	        numCounts[6] += getNum(counts, "six",   'x');
	        numCounts[8] += getNum(counts, "eight", 'g');
	        
	        numCounts[1] += getNum(counts, "one",   'o');
	        numCounts[3] += getNum(counts, "three", 't');
	        numCounts[5] += getNum(counts, "five",  'f');
	        numCounts[7] += getNum(counts, "seven", 's');
	        numCounts[9] += getNum(counts, "nine",  'i');
	        
	        string result;
	        for (int k = 0; k < 10; ++k)
	        {
	            result.append(numCounts[k], k + '0');
	        }
	        
	        return result;
	    }
	    
	    int getNum(vector<int> &counts, const string &eng, char uk)
	    {
	        int result = counts[uk - 'a'];
	        if (result == 0) return result;
	        for (int k = 0; k < eng.size(); ++k)
	        {
	            counts[eng[k] - 'a'] -= result;
	        }
	        return result;
	    }
	};