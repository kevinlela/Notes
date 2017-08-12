### Maximum Gap
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

[leetcode](https://leetcode.com/problems/maximum-gap/description/)

### Answer 
That is the logic, if the element is uniformly lies in every bucket, we can calculate their difference directly, if not, there must be at least one pair of points lies in two buckets with at least one empty bucket in between. 

	class Solution {
	public:
	    int maximumGap(vector<int>& nums) {
	        int len = nums.size();
	        if (len < 2) return 0;
	        
	        // use bucket sort, think in this way
	        // we put len elements in len buckets
	        // the capacity of each bucket is (max - min + 1) / len;
	        // if it is 1, 2, 3, 4, 5 then interval = (5 -1 + 1) / 5;
	        // element is put into the interval n if iv[n] <= x - minVal < iv[n-1]
	        // then, it is the tricky think
	        // if 5 consecutive element, every bucket gets exact one element
	        // if not, at least one bucket will be empty
	        // so, the overall max gap must be larger than an interval
	        // so, we do not need to examine the diff within  a bucket
	        
	        double maxVal = nums[0], minVal = nums[0];
	        for (int k = 1; k < len; ++k)
	        {
	            maxVal = max(maxVal, (double)nums[k]);
	            minVal = min(minVal, (double)nums[k]);
	        }
	        
	        if (maxVal == minVal) return 0;
	        
	        double interval = (maxVal - minVal + 1) / (double)len;
	        vector<bool> occ(len, false);
	        vector<int> maxEle(len, 0);
	        vector<int> minEle(len, 0);
	        
	        for (int k = 0; k < len; ++k)
	        {
	            int index = floor(((double)nums[k] - minVal) / interval);
	            if (index >= len) index = len - 1;
	            //cout << index << endl;
	            if (occ[index])
	            {
	                maxEle[index] = max(maxEle[index], nums[k]);
	                minEle[index] = min(minEle[index], nums[k]);
	            }
	            else
	            {
	                maxEle[index] = nums[k];
	                minEle[index] = nums[k];
	                occ[index] = true;
	            }
	        }
	        
	        int gapRes = 1;
	        int prev = maxEle[0]; // the first bucket is always occupied by min
	        for (int k = 1; k < len; ++k)
	        {
	            if (occ[k])
	            {
	                gapRes = max(gapRes, minEle[k] - prev);
	                prev = maxEle[k];
	            }
	        }
	        
	        return gapRes;
	    }
	};