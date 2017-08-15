### Max Sum of Rectangle No Larger Than K
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?

[leetcode](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/)

### Answer
The brute force way is calculating the sum matrix O(N^2) and traverse all possible rectangular O(N^4). 

if we keep the left boundary i, and right boundary j, vertically, we can traverse from 0 to h, the rec = sum[i][n] - sum[i][m] this becomes the problem [327](327_Count_of_Range_Sum.md)

	class Solution {
	public:
	    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
	        // you can store the rec area regarding with the left top corner in N^2
	        // for every corner, you need N^2 to find all possible rec -> N^4
	        // so brutal force way generate O(N^4) complexity
	        // fuck, it is the third time I cannot figure out this problem, it is just so strange to iterate
	        int h = matrix.size();
	        if (h == 0) return 0;
	        int w = matrix[0].size();
	        
	        vector<vector<int>> sum(h, vector<int>(w, 0));
	        int prev = 0;
	        for (int i = 0; i < w; ++i)
	        {
	            sum[0][i] = prev + matrix[0][i];
	            prev += matrix[0][i];
	        }
	        for (int j = 1; j < h; ++j)
	        {
	            prev = 0;
	            for (int i = 0; i < w; ++i)
	            {
	                sum[j][i] = sum[j-1][i] + prev + matrix[j][i];
	                prev += matrix[j][i];
	            }
	        }
	        
	        int result = INT_MIN;
	        for (int i = 0; i < w; ++i)
	        {
	            for (int m = 0; m <= i; ++m)
	            {
	                set<int> sumSoFar;
	                sumSoFar.insert(0);
	                for (int j = 0; j < h; ++j)
	                {
	                    int left = m == 0 ? 0 : sum[j][m-1];
	                    int curr = sum[j][i] - left;
	                    auto iter = sumSoFar.lower_bound(curr-k);
	                    if (iter != sumSoFar.end()) 
	                        result = max(result, curr - *iter);
	                    sumSoFar.insert(curr);
	                }
	            }
	        }
	        return result;
	    }
	};

