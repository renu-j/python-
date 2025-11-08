# Program to check if a list is a palindrome using copy()
list1= [1,2,1]
list2= [1,2,3]
copy_list1 =list1.copy()#similary we can also check the plaindrome of the list2 .
copy_list1.reverse()

if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")