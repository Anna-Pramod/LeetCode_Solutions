#Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.
#Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible for every character of str1 to every character of str2 while preserving the order.
#Note: All occurrences of every character in ‘str1’ should map to the same character in ‘str2’

#User function Template for python3
from collections import Counter
class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        l1 = list(Counter(str1).values())
        l2 = list(Counter(str2).values())
        l1.sort()
        l2.sort()
        a=[]
        d={}
        i=0
        if l1 == l2:
            while (i<len(str1)):
                a.append([str1[i],str2[i]])
                i+=1
            for j in a:
                if j[0] in d:
                    d[j[0]].append(j[1])
                else:
                    d[j[0]] = [j[1]]
            
            for c in (d.values()):
                if len(c) != 1:
                    if c.count(c[0])==len(c):
                        continue
                    else:
                        return 0
            return 1
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends

# Correct Answer.Correct Answer
# Execution Time:0.27
