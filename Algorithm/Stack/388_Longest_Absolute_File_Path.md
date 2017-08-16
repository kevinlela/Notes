### Longest Absolute File Path
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.

[leetcode](https://leetcode.com/problems/longest-absolute-file-path/description/)

### Answer 

	class Solution {
	public:
	    int lengthLongestPath(string input) {
	        int curr_len = 0;
	        int max_len = 0;
	        stack<int> stk;
	        int iter = 0;
	        int curr_level = 0;
	        
	        while (iter < input.size())
	        {
	            int next_st = iter;
	            bool is_file = isfileGo(next_st, input);
	            stk.push(next_st - iter + 1);
	            curr_len += next_st - iter + 1;
	            if (is_file) max_len = max(max_len, curr_len - 1);
	            ++next_st;
	            int next_level = getLevel(next_st, input);
	            for (int i = curr_level; i >= next_level && !stk.empty(); --i)
	            {
	                curr_len -= stk.top();
	                stk.pop();
	            }
	            iter = next_st;
	            curr_level = next_level;
	        }
	        
	        return max_len;
	    }
	    
	    bool isfileGo(int &st, const string &input)
	    {
	        int len = input.size();
	        bool flag = false;
	        for (st; st < len; ++st)
	        {
	            if (input[st] == '.') flag = true;
	            else if (input[st] == '\n') return flag;
	        }
	        return flag;
	    }
	    
	    int getLevel(int &st, const string &input)
	    {
	        int level = 0;
	        int len = input.size();
	        for (st; st < len; ++st)
	        {
	            if (input[st] == '\t') level += 4;
	            else return level/4;
	        }
	        return level/4;
	    }
	};