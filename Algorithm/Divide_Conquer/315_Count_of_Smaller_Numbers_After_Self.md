### Count of Smaller Numbers After Self
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

[leetcode](https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/)

### Answer 
Merge sort indicates the relationship between left and right, the right elements must come after the lest ones. 

	class Solution {
	public:
	    vector<int> countSmaller(vector<int>& nums) {
	        int len = nums.size();
	        if (len == 0) return vector<int> ();
	        vector<pair<int, int>> idx_count = mergeSort(nums, 0, len - 1);
	        vector<int> result(len, 0);
	        for (auto iter = idx_count.begin(); iter != idx_count.end(); ++iter)
	        {
	            result[iter->first] = iter->second;
	        }
	        return result;
	    }
	    
	    vector<pair<int, int>> mergeSort(const vector<int> &nums, int st, int ed)
	    {
	        if (st == ed) return vector<pair<int, int>>(1, {st, 0});
	        int mid = st + (ed - st) / 2;
	        vector<pair<int, int>> l = mergeSort(nums, st, mid);
	        vector<pair<int, int>> r = mergeSort(nums, mid + 1, ed);
	        return merge(l, r, nums);
	    }
	    
	    vector<pair<int, int>> merge(const vector<pair<int, int>> &left, 
	                                 const vector<pair<int, int>> &right,
	                                 const vector<int> &nums)
	    {
	        vector<pair<int, int>> result;
	        int iter1 = 0, iter2 = 0, lenL = left.size(), lenR = right.size();
	        
	        while (iter1 != lenL || iter2 != lenR)
	        {
	            if (iter2 == lenR) result.push_back(left[iter1++]);
	            else if (iter1 == lenL) result.push_back(right[iter2++]);
	            else
	            {
	                int numL = nums[left[iter1].first];
	                int numR = nums[right[iter2].first];
	                if (numL > numR)
	                {
	                    result.push_back({left[iter1].first, left[iter1].second + lenR - iter2});
	                    ++iter1;
	                }
	                else result.push_back(right[iter2++]);
	            }
	            
	        }
	        return result;
	    }
	};