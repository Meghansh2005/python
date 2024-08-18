s1=str(input("enter the first string"))
s2=str(input("enter the second string"))
c=s1+" "+s2

char_list = list(s1)
char_list[1] , char_list[0] = char_list[0] , char_list[1]
s1="".join(char_list)
char_list = list(s2)
char_list[1] , char_list[0] = char_list[0] , char_list[1]
s2="".join(char_list)
print("after swapping")
print("first string:",s1)
print("second string:",s2)