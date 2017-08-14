### Implement Queue using Stacks
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

[leetcode](https://leetcode.com/problems/implement-queue-using-stacks/description/)

### Answer 

	class MyQueue {
	public:
	    /** Initialize your data structure here. */
	    MyQueue() {
	        idx = 0;
	    }
	    
	    /** Push element x to the back of queue. */
	    void push(int x) {
	        myStk.push(x);
	    }
	    
	    /** Removes the element from in front of queue and returns that element. */
	    int pop() {
	        if (this->empty()) return -1;
	        int len = myStk.size();
	        stack<int> tmp;
	        for (int i = 0; i < len - 1; ++i)
	        {
	            tmp.push(myStk.top());
	            myStk.pop();
	        }
	        
	        int result = myStk.top();
	        myStk.pop();
	        
	        for (int i = 0; i < len - 1; ++i)
	        {
	            myStk.push(tmp.top());
	            tmp.pop();
	        }
	        
	        return result;
	    }
	    
	    /** Get the front element. */
	    int peek() {
	        if (this->empty()) return -1;
	        int len = myStk.size();
	        stack<int> tmp;
	        for (int i = 0; i < len - 1; ++i)
	        {
	            tmp.push(myStk.top());
	            myStk.pop();
	        }
	        
	        int result = myStk.top();
	        
	        for (int i = 0; i < len - 1; ++i)
	        {
	            myStk.push(tmp.top());
	            tmp.pop();
	        }
	        
	        return result;
	    }
	    
	    /** Returns whether the queue is empty. */
	    bool empty() {
	        return myStk.empty();
	    }
	private:
	    vector<stack<int>> myStk;
	    int idx;
	};

	/**
	 * Your MyQueue object will be instantiated and called as such:
	 * MyQueue obj = new MyQueue();
	 * obj.push(x);
	 * int param_2 = obj.pop();
	 * int param_3 = obj.peek();
	 * bool param_4 = obj.empty();
	 */