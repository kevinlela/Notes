### Sparse Matrix Multiplication
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
[leetcode](https://leetcode.com/problems/sparse-matrix-multiplication/description/)

### Answer

	class Solution {
	public:
	    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
	        int hA = A.size(), hB = B.size();
	        if (hA == 0 || hB == 0) return vector<vector<int>> ();
	        int wA = A[0].size(), wB = B[0].size();
	        if (wA != hB) return vector<vector<int>> ();
	        vector<vector<int>> result(hA, vector<int> (wB, 0));
	        
	        unordered_map<int, unordered_set<int>> spA; // row wise
	        unordered_map<int, unordered_set<int>> spB; // col wise
	        
	        for (int j = 0; j < hA; ++j)
	        {
	            for (int i = 0; i < wA; ++i)
	            {
	                if (A[j][i]) spA[j].insert(i);
	            }
	        }
	        
	        for (int j = 0; j < hB; ++j)
	        {
	            for (int i = 0; i < wB; ++i)
	            {
	                if (B[j][i]) spB[j].insert(i);
	            }
	        }
	        
	        // \sum_i A[j][i]*B[i][z] = C[j][z]
	        for (auto rAIt = spA.begin(); rAIt != spA.end(); ++rAIt)
	        {
	            int rA = rAIt->first;
	            for (auto cAIt = rAIt->second.begin(); cAIt != rAIt->second.end(); ++cAIt)
	            {
	                int cA = *cAIt;
	                if (spB.find(cA) != spB.end()) 
	                {
	                    for (auto cBIt = spB[cA].begin(); cBIt != spB[cA].end(); ++cBIt)
	                    {
	                        int cB = *cBIt;
	                        result[rA][cB] += A[rA][cA]*B[cA][cB];
	                    }
	                }
	            }
	        }
	        
	        return result;
	    }
	};
