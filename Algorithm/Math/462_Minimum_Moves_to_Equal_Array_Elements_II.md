### Minimum Moves to Equal Array Elements II
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

[leetcode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/)

### Answer
This is the minimum meeting point problem

* for two point p1 < p2, we meet at either point in between including p1 * and p2
* for three points p1 < p2 < p3, we meet at p2
* for four point p1 < p2 < p3 < p4, we meet at either point between p2 and p3 including p2 and p3. 

SO

* if odd points, meet at the median one
* if even points, meet at either of the median two

	class Solution {
	public:
	    int minMoves2(vector<int>& nums) {
	        //suppose two numse
	        // A and B, any value between A and B will yeild delta = B - A
	        // if A, C, B, the should meet at C because any point left or right to C yeild delta > B - A
	        // so the answer is the median
	        sort(nums.begin(), nums.end());
	        int len = nums.size();
	        if (len == 0) return 0;
	        int median = nums[( len - 1 ) / 2];
	        int result = 0;
	        for (int i = 0; i < len; ++i)
	        {
	            result += abs(nums[i] - median);
	        }
	        return result;
	    }
	};