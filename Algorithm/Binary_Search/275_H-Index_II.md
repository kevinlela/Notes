### H-Index II
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

[leetcode](https://leetcode.com/problems/h-index-ii/description/)

### Answer 
This is a binary search problem

h = len - i, if (s[i] < h) must be right, else, mush be left

	class Solution {
	public:
	    int hIndex(vector<int>& citations) {
	        int len = citations.size();;
	        if (len == 0) return 0;
	        int st = 0, ed = len;
	        while (st < ed)
	        {
	            int mid = st + (ed - st)/2;
	            int h = len - 1 - mid;
	            if (citations[mid] > h) ed = mid;
	            else st = mid + 1;
	        }
	        
	        return len - ed;
	    }
	};