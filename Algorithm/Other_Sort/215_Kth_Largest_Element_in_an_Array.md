### Kth Largest Element in an Array
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

[leetcode](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

### Answer 
* Merge Sort gives solution O(nlogn). 
* Priority Queue solution gives O(nlogk)
* Quick Sort gives O(n) best and O(n^2) worst

Algorithm
* for each round, randomly choose one to be pivot, say the last element. 
* use two tracker to put elements smaller than pivot to left and elements larger than pivot to right. 
	* if t1 < pivot; ++it
	* else swap t1 and t2
* low is always larger or equal to pivot
* check if the pivot is the kth pos
* go to left and right recursively

	class Solution {
	public:
	    int findKthLargest(vector<int>& nums, int k) {
	        int len = nums.size();
	        return quickSort(nums, k-1, 0, len - 1);
	    }
	    
	    int quickSort(vector<int> &nums, int k, int st, int ed)
	    {
	        int low = st, high = ed - 1;
	        while (low <= high)
	        {
	            if (nums[low] > nums[ed]) ++low;
	            else 
	            {
	                swap(nums[low], nums[high]);
	                --high;
	            }
	        }
	        
	        swap(nums[ed], nums[low]);
	        
	        if (low == k) return nums[low];
	        if (k < low) return quickSort(nums, k, st, low - 1);
	        return quickSort(nums, k, low + 1, ed);
	    }
	};