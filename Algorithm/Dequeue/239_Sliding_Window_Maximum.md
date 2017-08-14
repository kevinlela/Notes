### Sliding Window Maximum
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

[leetcode](https://leetcode.com/problems/sliding-window-maximum/description/)

### Answer 
This is a tricky problem. We need to maitain a window but want to get the maximum one. The brute force method takess O(nk). To use map solution beceomes O(nlogk). 

Use deque optimize to O(2N). when meet a new element n[i], we can pop the front all the elements outside the window, this element will not be include. Then, we pop back all the elements smaller than n[i] because these element will not considered in the later entry. In the other word, we definitely choose n[i] over these elements. 

	class Solution {
	public:
	    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
	        deque<pair<int, int>> win;
	        int len = nums.size();
	        vector<int> result;
	        
	        for (int i = 0; i < len; ++i)
	        {
	            while (!win.empty() && win.front().first <= i - k)
	            {
	                win.pop_front();
	            }
	            
	            while (!win.empty() && win.back().second < nums[i])
	            {
	                win.pop_back();
	            }
	            win.push_back({i, nums[i]});
	            if (i >= k - 1) result.push_back(win.front().second);
	        }
	        return result;
	    }
	};