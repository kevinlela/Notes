### Missing Ranges
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

[leetcode](https://leetcode.com/problems/missing-ranges/description/)

### Answer
	class Solution {
	public:
	    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
	        vector<string> result;
	        if (lower > upper) return result;
	        // use binary search to locate two pointer
	        auto lb = lower_bound(nums.begin(), nums.end(), lower);
	        auto rb = lower_bound(nums.begin(), nums.end(), upper);
	        
	        int st = lower;
	        for (auto iter = lb; iter != rb; ++iter)
	        {
	            if (st < *iter) result.push_back(genInterval(st, *iter - 1));
	            st = *iter + 1;
	        }
	        
	        if (rb != nums.end() && *rb == upper) upper -= 1;
	        if (st <= upper) result.push_back(genInterval(st, upper));
	        return result;
	    }
	    
	    string genInterval(int st, int ed)
	    {
	        return ed == st ? to_string(st) : (to_string(st) + "->" + to_string(ed));
	    }
	};