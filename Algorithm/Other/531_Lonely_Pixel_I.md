### Lonely Pixel I
Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
Note:
The range of width and height of the input 2D array is [1,500].

[leetcode](https://leetcode.com/problems/lonely-pixel-i/description/)

### Answer
	class Solution {
	public:
	    int findLonelyPixel(vector<vector<char>>& picture) {
	        int h = picture.size();
	        if (h == 0) return 0;
	        int w = picture[0].size();
	        if (w == 0) return 0;
	        
	        vector<int> row(h, -2);
	        vector<int> col(w, -2);
	        
	        for (int i = 0; i < h; ++i)
	        {
	            for (int j = 0; j < w; ++j)
	            {
	                if (picture[i][j] == 'B')
	                {
	                    if (row[i] == -2) row[i] = j;
	                    else row[i] = -1;
	                    if (col[j] == -2) col[j] = i;
	                    else col[j] = -1;
	                }
	            }
	        }
	        
	        int result = 0;
	        for (int i = 0; i < h; ++i)
	        {
	            if (row[i] >= 0)
	            {
	                if (col[row[i]] >= 0)
	                {
	                    ++result;
	                }
	            }
	        }
	        
	        return result;
	    }
	};