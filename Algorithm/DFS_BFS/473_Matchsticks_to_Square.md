### Matchsticks to Square
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.

[leetcode](https://leetcode.com/submissions/detail/108113241/)

### Answer
One criteria is that we know the find side length. Use dfs to try all the possibility. Use sort to optimize, avoid case like 1, 1, 1, 1, 1, ...., 100. Tried many small values but finally find impossible.

	class Solution {
	public:
	    bool makesquare(vector<int>& nums) {
	        int peri = 0;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            peri += nums[i];
	        }
	        
	        if (peri % 4 != 0 || peri == 0) return false;
	        
	        int side  = peri / 4;
	        vector<int> len_4(4, side);
	        sort(nums.begin(), nums.end(), greater<int>()); // optimize case 1, 1, 1, 1, 10000000
	        return recur(len_4, nums, 0);
	    }
	    
	    bool recur(vector<int> &len_4, const vector<int> &nums, int idx)
	    {
	        if (idx >= nums.size()) return true;
	        for (int i = 0; i < 4; ++i)
	        {
	            if (len_4[i] - nums[idx] >= 0)
	            {
	                len_4[i] -= nums[idx];
	                if (recur(len_4, nums, idx + 1)) return true;
	                len_4[i] += nums[idx];
	            }
	        }
	        return false;
	    }
	};
