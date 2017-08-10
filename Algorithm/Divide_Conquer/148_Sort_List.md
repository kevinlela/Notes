### Sort List
Sort a linked list in O(n log n) time using constant space complexity.

[leetcode](https://leetcode.com/problems/sort-list/description/)

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
	    ListNode* sortList(ListNode* head) {
	        int listLen = getLen(head);
	        if (listLen == 0) return head;
	        return mergeSort(head, 0, listLen - 1);
	    }
	    
	    ListNode* mergeSort(ListNode* &iter, int st, int ed)
	    {
	        if (st == ed) 
	        {
	            ListNode *curr = iter;
	            iter = iter->next;
	            curr->next = NULL;
	            return curr;
	        }
	        
	        int mid = st + (ed - st)/2;
	        ListNode* left  = mergeSort(iter, st, mid);
	        ListNode* right = mergeSort(iter, mid + 1, ed);
	        
	        return merge(left, right);
	    }
	    
	    ListNode* merge(ListNode* left, ListNode* right)
	    {
	        ListNode* head = NULL, *iter = NULL, *iterL = left, *iterR = right;
	        while (iterL || iterR)
	        {
	            ListNode* selected = NULL;
	            if (iterL == NULL)
	            {
	                selected = iterR;
	                iterR = iterR->next;
	            }
	            else if (iterR == NULL)
	            {
	                selected = iterL;
	                iterL = iterL->next;
	            }
	            else if (iterL->val < iterR->val)
	            {
	                selected = iterL;
	                iterL = iterL->next;
	            }
	            else
	            {
	                selected = iterR;
	                iterR = iterR->next;
	            }
	            
	            selected->next = NULL;
	            if (head == NULL) head = selected;
	            else iter->next = selected;
	            iter = selected;
	        }
	        return head;
	    }
	    
	    int getLen(ListNode* head)
	    {
	        int len = 0;
	        while (head)
	        {
	            head = head->next;
	            ++len;
	        }
	        return len;
	    }
	};