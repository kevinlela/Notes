### Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

[leetcode](https://leetcode.com/problems/partition-list/description/)

### Answer 

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
	    ListNode* partition(ListNode* head, int x) {
	        ListNode *left = NULL, *leftHead = NULL, *right = NULL, *rightHead = NULL;
	        
	        ListNode *iter = head;
	        
	        while (iter)
	        {
	            if (iter->val < x)
	            {
	                if (left == NULL) leftHead = iter;
	                else left->next = iter;
	                left = iter;
	            }
	            else
	            {
	                if (right == NULL) rightHead = iter;
	                else right->next = iter;
	                right = iter;
	            }
	            
	            iter = iter->next;
	        }
	        
	        if (left == NULL) leftHead = rightHead;
	        else left->next = rightHead;
	        if (right) right->next = NULL;
	        
	        return leftHead;
	    }
	};