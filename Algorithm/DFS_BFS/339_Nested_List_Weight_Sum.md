### Nested List Weight Sum
Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)

[leetcode](https://leetcode.com/problems/nested-list-weight-sum/description/)

### Answer
	/**
	 * // This is the interface that allows for creating nested lists.
	 * // You should not implement it, or speculate about its implementation
	 * class NestedInteger {
	 *   public:
	 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
	 *     bool isInteger() const;
	 *
	 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
	 *     // The result is undefined if this NestedInteger holds a nested list
	 *     int getInteger() const;
	 *
	 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
	 *     // The result is undefined if this NestedInteger holds a single integer
	 *     const vector<NestedInteger> &getList() const;
	 * };
	 */
	class Solution {
	public:
	    typedef vector<NestedInteger>::const_iterator Vnit;
	    
	    int depthSum(vector<NestedInteger>& nestedList) {
	        stack<Vnit> stStk;
	        stack<Vnit> edStk;
	        stStk.push(nestedList.cbegin());
	        edStk.push(nestedList.cend());
	        int result = 0;
	        
	        while (!stStk.empty())
	        {
	            if (stStk.top() == edStk.top()) 
	            {
	                stStk.pop();
	                edStk.pop();
	            }
	            else
	            {
	                if (stStk.top()->isInteger())
	                {
	                    result += stStk.top()->getInteger() * (int)stStk.size();
	                    ++(stStk.top());
	                }
	                else
	                {
	                    Vnit st_vnit = stStk.top()->getList().cbegin();
	                    Vnit ed_vnit = stStk.top()->getList().cend();
	                    ++(stStk.top());
	                    stStk.push(st_vnit);
	                    edStk.push(ed_vnit);
	                }
	            }
	        }
	        
	        return result;
	    }
	};