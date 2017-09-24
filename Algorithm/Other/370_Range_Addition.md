### Range Addition
Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Given:

    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]

Output:

    [-2, 0, 3, 5, 3]
Explanation:

Initial state:
[ 0, 0, 0, 0, 0 ]

After applying operation [1, 3, 2]:
[ 0, 2, 2, 2, 0 ]

After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ]

After applying operation [0, 2, -2]:
[-2, 0, 3, 5, 3 ]

[leetcode](https://leetcode.com/problems/range-addition/description/)

### Answer
	class Solution {
	public:
	    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
	        vector<int> result(length + 1, 0);
	        for (int i = 0; i < updates.size(); ++i)
	        {
	            result[updates[i][0]]   += updates[i][2];
	            result[updates[i][1]+1] -= updates[i][2];
	        }
	        
	        int inc = 0;
	        for (int i = 0; i < result.size(); ++i)
	        {
	            inc += result[i];
	            result[i] = inc;
	        }
	        
	        result.pop_back();
	        return result;
	    }
	};