s=input("enter the string:")
i=0
j=len(s)-1
flag=1
while(i<j):
    if(s[i]!=s[j]):
        flag=0
    i=i+1
    j=j-1
if(flag):
    print("the string is palindrome")
else:
    print("the string is not palindrome")