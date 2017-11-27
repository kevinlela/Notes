### Squirrel Simulation
There's a tree, a squirrel, and several nuts. Positions are represented by the cells in a 2D grid. Your goal is to find the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one. The squirrel can only take at most one nut at one time and can move in four directions - up, down, left and right, to the adjacent cell. The distance is represented by the number of moves.

Example 1:
Input: 
Height : 5
Width : 7
Tree position : [2,2]
Squirrel : [4,4]
Nuts : [[3,0], [2,5]]
Output: 12
Explanation:

Note:
All given positions won't overlap.
The squirrel can take at most one nut at one time.
The given positions of nuts have no order.
Height and width are positive integers. 3 <= height * width <= 10,000.
The given positions contain at least one nut, only one tree and one squirrel.

[leetcode](https://leetcode.com/problems/squirrel-simulation/description/)

### Answer
	class Solution {
	public:
	    int minDistance(int height, int width, vector<int>& tree, vector<int>& squirrel, vector<vector<int>>& nuts) {
	        int len = nuts.size();
	        vector<int> n2s(len, 0);
	        vector<int> n2t(len, 0);
	        
	        int sum = 0;
	        for (int i = 0; i < len; ++i)
	        {
	            n2s[i] = abs(nuts[i][0] - squirrel[0]) + abs(nuts[i][1] - squirrel[1]);
	            n2t[i] = abs(nuts[i][0] - tree[0]) + abs(nuts[i][1] - tree[1]);
	            sum += n2t[i];
	        }
	        
	        sum *= 2;
	        int result = INT_MAX;
	        for (int i = 0; i < len; ++i)
	        {
	            result = min(sum - n2t[i] + n2s[i], result);
	        }
	        
	        return result;
	    }
	};