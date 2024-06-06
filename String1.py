str1=input("Enter a string: ")

def reverse_whole(s):
    i=len(s)-1
    rev=""
    while i>=0:
        rev+=s[i]
        i-=1
    return  rev

def reverse_word(l):
    l2=str1.split()
    rev_wrd=""

    for i in range(len(l2)):
        rev_wrd+=reverse_whole(l2[i])+" "
    return  rev_wrd

def char_list(str1):
    n=len(str1)
    l=[0]*n

    for i in range(n):
        l[i]=str1[i]
    return l

# print(char_list(str1))
l1=char_list(str1)
print(reverse_whole(l1))
print(reverse_word(l1))




