### ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

	P   A   H   N
	A P L S I I G
	Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

{https://leetcode.com/problems/zigzag-conversion/description/}

### Answer:

	class Solution {
	public:
	    string convert(string s, int numRows) {
	        if (numRows <= 1)
	        {
	            return s;
	        }
	        
	        // the period is 2x-2
	        int prd = numRows*2 - 2;
	        int j = 0;
	        string result;
	        
	        // first row
	        while (j < s.size())
	        {
	            result += s[j];
	            j += prd;
	        }
	        
	        // middle rows
	        for (int i = 1; i < numRows - 1; ++i)
	        {
	            j = i;
	            int currPrd = prd - i*2, mid_j = 0;
	            while (j < s.size())
	            {
	                result += s[j];
	                mid_j = j + currPrd;
	                if (mid_j >= s.size())
	                {
	                    break;
	                }
	                result += s[mid_j];
	                j += prd;
	            }
	        }
	        
	        //last row;
	        j = numRows - 1;
	        while (j < s.size())
	        {
	            result += s[j];
	            j += prd;
	        }
	        
	        return result;
	    }
	};