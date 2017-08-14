### Flatten Nested List Iterator
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].

[leetcode](https://leetcode.com/problems/flatten-nested-list-iterator/description/)

### Answer 
We need to record the end iterator to indicate where to stop besides the current iterator. 

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
	class NestedIterator {
	public:
	    typedef vector<NestedInteger> vni;
	    typedef vni::const_iterator niter;
	    
	    
	    NestedIterator(vector<NestedInteger> &nestedList) {
	        niter st = nestedList.begin();
	        niter ed = nestedList.end();
	        d_st.push(st);
	        d_ed.push(ed);
	        
	        while (1)
	        {
	            if (d_st.top() == d_ed.top()) // end or empty
	            {
	                d_st.pop();
	                d_ed.pop();
	                if (d_st.empty()) break;
	                ++(d_st.top());
	            }
	            else
	            {
	                st = d_st.top();
	                if (st->isInteger()) break; //d_st.top() is valid
	                const vni &nextOne = st->getList();
	                d_st.push(nextOne.begin());
	                d_ed.push(nextOne.end());
	            }
	        }
	    }

	    int next() {
	        // print the current one and advance to the next
	        // print the current one, guarantee the current one is always integer
	        int result = d_st.top()->getInteger();
	        
	        // advance to the next;
	        ++d_st.top();
	        
	        while (1)
	        {
	            if (d_st.top() == d_ed.top()) // end or empty
	            {
	                d_st.pop();
	                d_ed.pop();
	                if (d_st.empty()) break;
	                ++(d_st.top());
	            }
	            else
	            {
	                auto st = d_st.top();
	                if (st->isInteger()) break; //d_st.top() is valid
	                const vni &nextOne = st->getList();
	                d_st.push(nextOne.begin());
	                d_ed.push(nextOne.end());
	            }
	        }
	        
	        return result;
	        //return 0;
	    }

	    bool hasNext() {
	        return !d_st.empty();
	    }
	    
	private:
	    stack<niter> d_st;
	    stack<niter> d_ed;
	};

	/**
	 * Your NestedIterator object will be instantiated and called as such:
	 * NestedIterator i(nestedList);
	 * while (i.hasNext()) cout << i.next();
	 */