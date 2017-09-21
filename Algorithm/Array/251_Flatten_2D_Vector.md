### Flatten 2D Vector
Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

[leetcode](https://leetcode.com/problems/flatten-2d-vector/description/)

### Answer
	class Vector2D {
	public:
	    Vector2D(vector<vector<int>>& vec2d) {
	        row_iter = vec2d.cbegin();
	        row_end = vec2d.cend();
	        if (row_iter != row_end) col_iter = row_iter->cbegin();
	    }

	    int next() {
	        return *(col_iter++);
	    }

	    bool hasNext() {
	        if (row_iter == row_end) return false;
	        while (col_iter == row_iter->cend())
	        {
	            ++row_iter;
	            if (row_iter == row_end) return false;
	            col_iter = row_iter->cbegin();
	        }
	            
	        return true;
	    }
	private:
	    vector<vector<int>>::const_iterator row_iter;
	    vector<vector<int>>::const_iterator row_end;
	    vector<int>::const_iterator col_iter;
	};

	/**
	 * Your Vector2D object will be instantiated and called as such:
	 * Vector2D i(vec2d);
	 * while (i.hasNext()) cout << i.next();
	 */