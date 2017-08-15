### Find K Pairs with Smallest Sums
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]

[leetcode](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/)

### Answer
One solution is to use a iterator to the second array for every element in the first array. Advance the minimum one. The complexity is O(k min(M, N)), M, N is the array size. 

The other one is to use a priority queue, encode the second array index, pop the smallest and advance the iterator and insert again. The complexity is O(k log min(M, N))

	class Solution {
	public:
	    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
	        int len1 = nums1.size(), len2 = nums2.size();
	        //if (len2 < len1) return kSmallestPairs(nums2, nums1, k);
	        vector<pair<int, int>> result;
	        if (len1 == 0 || len2 == 0) return result;
	        vector<int> iter(len1, 0);
	        
	        for (int i = 0; i < k; ++i)
	        {
	            int t_idx = -1;
	            int min_sum = INT_MAX;
	            for (int j = 0; j < len1; ++j)
	            {
	                if (iter[j] >= len2) continue;
	                if (nums1[j] + nums2[iter[j]] < min_sum)
	                {
	                    min_sum = nums1[j] + nums2[iter[j]];
	                    t_idx = j;
	                }
	            }
	            
	            if (t_idx == -1) return result;
	            result.push_back({nums1[t_idx], nums2[iter[t_idx]]});
	            ++iter[t_idx];
	        }
	        return result;
	    }
	    
	    
	};
