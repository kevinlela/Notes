### Student Attendance Record I
You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False

[leetcode](https://leetcode.com/problems/student-attendance-record-i/description/)

### Answer
This question is wrong !
should be human understandable:
not rewarded if contain one A and contain two continuous L. 

class Solution {
public:
    bool checkRecord(string s) {
        int a = 0, l = 0, cl = 0;
        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == 'L') cl = max(++l, cl);
            else 
            {
                l = 0;
                if (s[i] == 'A') ++a;
            }
        }
        return !(a > 1 || cl > 2);
    }
};
