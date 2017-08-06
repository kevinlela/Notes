### Rotate Image
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

[leetcode](https://leetcode.com/problems/rotate-image/description/)

### Answer 
	class Solution {
	public:
	    void rotate(vector<vector<int>>& matrix) {
	        int w1 = matrix.size();
	        if (w1 <= 1) return;
	        
	        int w = w1 - 1;
	        int hw = w / 2;
	        
	        for (int k = 0; k <= hw; ++k)
	        {
	            for (int i = k; i < w - k; ++i)
	            {
	                int tmp = matrix[k][i];
	                matrix[k][i] = matrix[w-i][k];
	                matrix[w-i][k] = matrix[w-k][w-i];
	                matrix[w-k][w-i] = matrix[i][w-k];
	                matrix[i][w-k] = tmp;
	            }
	        }
	    }
	    
	    void print(vector<vector<int>> &m)
	    {
	        for (int i = 0; i < m.size(); ++i)
	        {
	            for (int j = 0; j < m.size(); ++j)
	            {
	                cout << m[i][j] << " ";
	            }
	            cout << endl;
	        }
	        cout << endl;
	    }
	};