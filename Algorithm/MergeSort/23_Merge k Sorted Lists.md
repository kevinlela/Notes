### Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

[leetcode](https://leetcode.com/problems/merge-k-sorted-lists/description/)

### Answer:
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

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
	    ListNode* mergeKLists(vector<ListNode*>& lists) {
	        if (lists.empty()) return NULL;
	        return divideConquer(lists, 0, lists.size()-1);
	    }
	    
	    ListNode* divideConquer(vector<ListNode*>& lists, int st, int ed)
	    {
	        if (st == ed) return lists[st];
	        int mid = st + (ed - st)/2;
	        ListNode* left = divideConquer(lists, st, mid);
	        ListNode* right = divideConquer(lists, mid + 1, ed);
	        return mergeTwoLists(left, right);
	    }
	    
	    
	    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
	        ListNode *result = NULL, *head = NULL;
	        while (l1 != NULL || l2 != NULL)
	        {
	            if (l1 == NULL) mergeAndForward(l2, result, head);
	            else if (l2 == NULL) mergeAndForward(l1, result, head);
	            else if (l1->val > l2->val) mergeAndForward(l2, result, head);
	            else mergeAndForward(l1, result, head);
	        }
	        return head;
	    }
	    
	    void mergeAndForward(ListNode* &current, ListNode* &result, ListNode* &head)
	    {
	        if (result == NULL) head = current;
	        else result->next = current;
	        result = current;
	        current = current->next;
	        result->next = NULL;
	    }
	};