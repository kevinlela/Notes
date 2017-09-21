### Zigzag Iterator
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].

[leetcode](https://leetcode.com/problems/zigzag-iterator/description/)

### Answer
use queue if it is k vectors

	class ZigzagIterator {
	public:
	    ZigzagIterator(vector<int>& v1, vector<int>& v2) : odd(true) {
	        d_cit1 = v1.cbegin();
	        d_ced1 = v1.cend();
	        d_cit2 = v2.cbegin();
	        d_ced2 = v2.cend();
	    }

	    int next() {
	        int result = 0;
	        if (odd)
	        {
	            if (d_cit1 != d_ced1) result = *(d_cit1++);
	            else result = *(d_cit2++);
	        }
	        else
	        {
	            if (d_cit2 != d_ced2) result = *(d_cit2++);
	            else result = *(d_cit1++);
	        }
	        odd = !odd;
	        return result;
	    }

	    bool hasNext() {
	        return d_cit1 != d_ced1 || d_cit2 != d_ced2;        
	    }
	    
	private:
	    vector<int>::const_iterator d_cit1;
	    vector<int>::const_iterator d_ced1;
	    vector<int>::const_iterator d_cit2;
	    vector<int>::const_iterator d_ced2;
	    bool odd;
	};

	/**
	 * Your ZigzagIterator object will be instantiated and called as such:
	 * ZigzagIterator i(v1, v2);
	 * while (i.hasNext()) cout << i.next();
	 */