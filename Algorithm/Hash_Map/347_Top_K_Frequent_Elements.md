### Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ? k ? number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


[leetcode](https://leetcode.com/problems/top-k-frequent-elements/description/)

### Answer 

	class Solution {
	public:
	    typedef unordered_map<int, int>::iterator umi;
	    struct greater_than{
	        inline bool operator () (const umi &it1, const umi &it2)
	        {
	            return it1->second > it2->second;
	        }
	    };
	    
	    vector<int> topKFrequent(vector<int>& nums, int k) {
	        vector<int> result;
	        if (k == 0) return result;
	        unordered_map<int, int> counts;
	        for (int i = 0; i < nums.size(); ++i)
	        {
	            ++counts[nums[i]];
	        }
	        
	        priority_queue<umi, vector<umi>, greater_than> pq;
	        for (auto iter = counts.begin(); iter != counts.end(); ++iter)
	        {
	            pq.push(iter);
	            if (pq.size() > k) pq.pop();
	        }
	        
	        while (!pq.empty())
	        {
	            result.push_back(pq.top()->first);
	            pq.pop();
	        }
	        
	        return result;
	    }
	};