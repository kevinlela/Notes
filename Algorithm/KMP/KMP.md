## searching substring

Suppose we have a string S and a string P, we want to find if S contains a substring same as P. Brutal forcely, we need O(PS). 

KMP is designed to optimize this problem

## KMP: Knuth Morris Pratt Pattern Searching

Optimize by finding pattern having same sub-patterns appearing more than once in the pattern. 

For example

	S = "ABABABCABABABCABABABC"
	P = "ABABAC"

When we matched to 

	S = "ABABABCABABABCABABABC"
	          ^
	P = "ABABAC"
              ^

Do we need to start from B (S[1]) and match the string again? NO. Probably what we can do is to set the matching iterators to be 

	S = "ABABABCABABABCABABABC"
	          ^
	P = "ABABAC"
			^
Because we know ABA matches anyway

## Algorithm

1) Auxiliary Array lps[] with sizeof(P)
	* proper prefix: prefix excluding the full string. E.g., "ABC" = {"", "A", "AB"}
	* lps[i] = the longest proper prefix of P[0...i] which is also a suffix of P[0...i]
	* E.g., "AABAA" we have [0, 1, 0, 1, 2]
	* How to construct lps[]

			lps[0] = 0
			pLen = 0 // previous longest prefix suffix
			loop i = 1 ... sizeof(P):
				 if p[i] == p[pLen]:
				 	++pLen
				 	lps[i] = pLen
				 	++i
				 else:
				 	if (pLen != 0):
				 		pLen = lps[pLen - 1] 
				 		//lps[plen-1] contains all solution to substring of matched prefix before p[i] 
				 	else
				 		lps[i] = 0
				 		++i

			For examples:
			
			aabaabaaa
			01012345

			aabaabaaa
			     ^  ^
			     j  i

			i and j mismatched

			aabaabaaa
			  ^     ^
			  j     i
			still mismatch

			aabaabaaa
			^       ^
			j       i
			match

2) Use lps to do matching
	* s[i] == p[j]
		* ++i, ++j
	* s[i] != p[j]
		* p[0...j-1] matches s[i-j...i-1]
		* lps[j-1] is the count of characters of p[0...j-1] that are both proper prefix and suffic
		* So we do not need to match p[0...lps[j-1]-1] with s[i-lps[i-1]...i-1]
