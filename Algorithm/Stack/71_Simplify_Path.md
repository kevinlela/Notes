### Simplify Path
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
* Did you consider the case where path = "/../"?
In this case, you should return "/".
* Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

[leetcode](https://leetcode.com/problems/simplify-path/description/)

### Answer
the only operation we need to do is to pop the current folder when meeting ".."
I use dequeue instead of stack only because the last step - stringfy. 

	class Solution {
	public:
	    string simplifyPath(string path) {
	        deque<string> stk;
	        
	        for (int i = 0; i < path.size(); ++i)
	        {
	            if (path[i] == '/') continue;
	            string currFolder;
	            for (; i < path.size(); ++i)
	            {
	                if (path[i] == '/') break;
	                currFolder.append(1, path[i]);
	            }
	            //cout << currFolder << endl;
	            if (currFolder == ".") continue;
	            else if (currFolder == "..")
	            {
	                if (!stk.empty()) stk.pop_back();
	            }
	            else stk.push_back(currFolder);
	        }
	        
	        string result;
	        while (!stk.empty())
	        {
	            result += "/" + stk.front();
	            stk.pop_front();
	        }
	        
	        return result.empty() ? "/" : result;
	    }
	}; 