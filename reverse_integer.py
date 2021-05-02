#Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-2 ^ 31, 2 ^ 31 - 1], then return 0.

def reve(n):
    rev = 0
    while n>0:
        rev = (rev*10) + (n%10)
        n//=10
    return (rev)
class Solution:
    
    def reverse(self, x: int) -> int:
                                            
        if x<0:
            x = x * (-1)
            r = (-reve(x))
        elif x==0:
            return(0)
        else:
            r = (reve(x))
            
        if  -2147483648<r<2147483647:               #(r<=((2**31)-1)) or (r>=(-2**31)):
            return (r)
        else:
            return (0)
        
        
