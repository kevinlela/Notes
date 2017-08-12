### Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

[leetcode](https://leetcode.com/problems/excel-sheet-column-title/description/)

### Answer 
... + 26^2*(x_2 - 'A' + 1) + 26*(x_1 - 'A' + 1) + (x_0 - 'A' + 1) = n 
That is why we need to minus 1 in every iteration

	class Solution {
	public:
	    string convertToTitle(int n) {
	        int base = 26;
	        string result;
	        
	        while (n)
	        {
	            --n;
	            result.append(1, 'A' + n%26);
	            n /= 26;
	        }
	        
	        reverse(result.begin(), result.end());
	        return result;
	    }
	};