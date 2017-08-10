### Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

[leetcode](https://leetcode.com/problems/linked-list-cycle-ii/description/)

### Answer 
proof, suppose the cycle perimeter is r, and the length before cycle is l. L_s means the distance slow iterator has been through and L_f is for fast iterator. 

L_s = l + x
L_f = l + mr + x
2xL_s = L_f
x = l + mr - 2l = mr - l

x is the meeting point, means if we let x go l further, it gonna be the cycle beginning point. so we send a iterator from the beginning of list again. 


	/**
	 * Definition for singly-linked list.
	 * struct ListNode {
	 *     int val;
	 *     ListNode *next;
	 *     ListNode(int x) : val(x), next(NULL) {}
	 * };
	 */
	class Solution {
	public:
	    ListNode *detectCycle(ListNode *head) {
	        ListNode *slow = head, *fast = head, *intersect = NULL;
	        while (fast)
	        {
	            slow = slow->next;
	            fast = fast->next;
	            if (fast) fast = fast->next;
	            else return NULL;
	            if (slow == fast)
	            {
	                intersect = slow;
	                break;
	            }
	        }
	        
	        if (intersect == NULL) return NULL;
	        
	        slow = head;
	        
	        while (slow != fast)
	        {
	            slow = slow->next;
	            fast = fast->next;
	        }
	        
	        return slow;
	    }
	};