### Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

[leetcode](https://leetcode.com/problems/majority-element-ii/description/)

### Answer 
Similar to [169](169_Majority_Element.md)

find element in [n/k] times. 
1) construct vector of k elements
2) if n[i] == v[k]; v[k]++;
3) else if v[k] == 0 assign n[i] to v[k]
4) else v[k]-- for all k
5) count v[k] again.

	class Solution {
	public:
	    vector<int> majorityElement(vector<int>& nums) {
	        vector<int> cands(2, 0);
	        cands[1] = 1; // randomly set two number
	        vector<int> counts(2, 0);
	        
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            if (nums[i] == cands[0]) ++counts[0];
	            else if (nums[i] == cands[1]) ++counts[1];
	            else if (counts[0] == 0)
	            {
	                cands[0] = nums[i];
	                counts[0] = 1;
	            }
	            else if (counts[1] == 0)
	            {
	                cands[1] = nums[i];
	                counts[1] = 1;
	            }
	            else
	            {
	                --counts[0];
	                --counts[1];
	            }
	        }
	        
	        counts[0] = 0; counts[1] = 0;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            if (nums[i] == cands[0]) ++counts[0];
	            if (nums[i] == cands[1]) ++counts[1];
	        }
	        
	        int len = nums.size();
	        int thre = len/3;
	        
	        vector<int> result;
	        if (counts[0] > thre) result.push_back(cands[0]);
	        if (counts[1] > thre) result.push_back(cands[1]);
	        
	        return result;
	    }
	};