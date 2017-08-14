### Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

[leetcode](https://leetcode.com/problems/find-the-duplicate-number/description/)

### Answer 

If we can modify the array, we can use the array itself as a hash map. In this problem, we can use the linkedlist cyple technique to find the duplicate number. For each number, a[i] go to the pos a[i] as  

The duplicate one will form a cycle as

1, 2, 3, 4, 2 becomes

1->2->3->4->2->3, the position 2 is the meeting point and is the result. 

That is because all element will have different position except the duplicate one. That position will be visited twice. 

	class Solution {
	public:
	    int findDuplicate(vector<int>& nums) {
	        // it is a link list intersection problem, 
	        // since there is a duplicate, a same entry will be visited twice
	        // there must be a intersection point, extract that idx
	        
	        int slow = 0, fast = 0;
	        while (1)
	        {
	            slow = nums[slow];
	            fast = nums[fast];
	            fast = nums[fast];
	            if (slow == fast) break;
	        }
	        
	        slow = 0;
	        
	        while (slow != fast)
	        {
	            slow = nums[slow];
	            fast = nums[fast];
	        }
	        
	        return slow;
	    }
	};