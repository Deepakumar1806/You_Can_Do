  
def reverse(s): 
	return s[::-1] 

def isPalindrome(s): 
 
	rev = reverse(s) 

 
	if (s == rev): 
		return True
	return False


s =str(input())
ans = isPalindrome(s) 
if ans == 1: 
	print("yes") 
else: 
	print("no") 
