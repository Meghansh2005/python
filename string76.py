s1=str(input("enter the string:"))
i=0
j=len(s1)-1
char_list = list(s1)
char_list[j] , char_list[i] = char_list[i] , char_list[j]
s1="".join(char_list)
print("the string:",s1)