### Design Phone Directory
Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
Example:

// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);

[leetcode](https://leetcode.com/problems/design-phone-directory/description/)

### Answer
	class PhoneDirectory {
	public:
	    /** Initialize your data structure here
	        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
	    PhoneDirectory(int maxNumbers) {
	        maxNum = 0;
	        this->maxNumber = maxNumbers;
	    }
	    
	    /** Provide a number which is not assigned to anyone.
	        @return - Return an available number. Return -1 if none is available. */
	    int get() {
	        if (recycled.empty()) 
	        {
	            if (maxNum >= maxNumber) return -1;
	            else return maxNum++;
	        }
	        int result = *recycled.begin();
	        recycled.erase(recycled.begin());
	        return result;
	    }
	    
	    /** Check if a number is available or not. */
	    bool check(int number) {
	        if (number >= maxNumber) return false;
	        if (number >= maxNum) return true;
	        if (recycled.find(number) != recycled.end()) return true;
	        return false;
	    }
	    
	    /** Recycle or release a number. */
	    void release(int number) {
	        if (number >= maxNum) return;
	        recycled.insert(number);
	    }
	private:
	    unordered_set<int> recycled;
	    int maxNum;
	    int maxNumber;
	};

	/**
	 * Your PhoneDirectory object will be instantiated and called as such:
	 * PhoneDirectory obj = new PhoneDirectory(maxNumbers);
	 * int param_1 = obj.get();
	 * bool param_2 = obj.check(number);
	 * obj.release(number);
	 */