### Minimum Moves to Equal Array Elements
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
[leetcode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/)

### Answer
It is an interesting problem. 

Say, finally, x move, there are n number
Who needs to engage every time? the shortest one y.

The final bin is x + y

(x + y)*n = (n-1)*x + ori_sum

nx + ny = nx - x + ori_sum
x = ori_sum - ny


	class Solution {
	public:
	    int minMoves(vector<int>& nums) {
	        // if after m moves, every thing becomes equal
	        // (minNum + m) * n = (n-1) * m + sum(nums)
	        // m = sum - n*minNum;
	        
	        int minNum = nums[0], sum = nums[0];
	        for (int i = 1; i < nums.size(); ++i)
	        {
	            minNum = min(minNum, nums[i]);
	            sum += nums[i];
	        }
	        
	        return sum - minNum*(int)nums.size();
	        
	    }
	};


