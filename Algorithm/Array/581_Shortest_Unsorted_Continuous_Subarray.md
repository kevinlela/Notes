### Shortest Unsorted Continuous Subarray
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

[leetcode](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/)

### Answer
we represent the diffent between ajacent elements as - and + like

	+++-+--+--+++

we need to find

	+++(-+--+--)+++
	  ^         ^
	  a         b

This part must be reversed.

if we have four value a, b, c = min(part), d = max(part)

if a <= c <= d <= b, then we just need to sort that part, other wise, we need to extend that part. 

we can firstly check a or check b, it does not matter

a > c extend to left, update d
b < d extend to right

	class Solution {
	public:
	    int findUnsortedSubarray(vector<int>& nums) {
	        int len = nums.size();
	        int st = 0;
	        
	        for (st; st < len - 1; ++st)
	        {
	            if (nums[st + 1] < nums[st]) break;
	        }
	        
	        if (st == len - 1) return 0;
	        
	        int ed = len - 1;
	        for (ed; ed > 0; --ed)
	        {
	            if (nums[ed-1] > nums[ed]) break;
	        }
	        
	        if (st == 0 && ed == len - 1) return len;
	        
	        int minX = nums[ed], maxX = nums[st];
	        for (int i = st + 1; i < ed; ++i)
	        {
	            minX = min(minX, nums[i]);
	            maxX = max(maxX, nums[i]);
	        }
	        
	        for (ed; ed < len; ++ed)
	        {
	            if (nums[ed] >= maxX) break;
	            minX = min(minX, nums[ed]);
	        }
	        
	        for (st; st >= 0; --st)
	        {
	            if (nums[st] <= minX) break;
	        }
	        //cout << st << " " << ed << endl;
	        return ed - st - 1;
	    }
	};

