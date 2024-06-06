str1=input("Enter a string: ")

def string1(str1):
    l=list(str1)
    n=len(str1)
    s=0

    for i in range(n):
        if i==n-1 or l[i+1]==' ':
            e=i
            l[s]='@'
            l[e]='#'
            s=i+2

    str2=""
    i=0
    while i<n:
        str2+=l[i]
        i+=1
    return str2

def string2(str1):
    l=list(str1)
    n=len(str1)
    s=0

    for i in range(n):
        if i==n-1 or l[i+1]==' ':
            e=i
            temp1=ord(l[s])
            temp2=ord(l[e])
            if temp1>90:
                l[s]=chr(temp1-32)
            else:
                l[s]=chr(temp1)
            if temp2>90:
                l[e]=chr(temp2-32)
            else:
                l[e]=chr(temp2)
            s=i+2

    str2=""
    i=0
    while i<n:
        str2+=l[i]
        i+=1
    return str2

def string3(str1):
    l=list(str1)
    n=len(str1)
    s=0

    for i in range(n):
        if i==n-1 or l[i+1]==' ':
            e=i
            while s<e:
                l[s],l[s+1]=l[s+1],l[s]
                s+=2
            s=i+2

    str2=""
    i=0
    while i<n:
        str2+=l[i]
        i+=1
    return str2


def string4(str1):
    l=list(str1)
    n=len(str1)
    s=0
    flag=0

    for i in range(n):
        if i==n-1 or l[i+1]==' ':
            e=i
            if not flag:
                while s<e:
                    temp=ord(l[s+1])
                    if temp>90:
                        l[s+1]=chr(temp-32)
                    else:
                        l[s+1]=chr(temp)
                    s+=2
                flag=1
            else:
                while s<e:
                    temp=ord(l[s])
                    if temp>90:
                        l[s]=chr(temp-32)
                    else:
                        l[s]=chr(temp)
                    s+=2
                flag=0
            s=i+2

    str2=""
    i=0
    while i<n:
        str2+=l[i]
        i+=1
    return str2

def string5(str1):
    l=list(str1)
    n=len(str1)
    s=0

    for i in range(n):
        if i==n-1 or l[i+1]==' ':
            e=i
            l[e]=(e+1)-s
            s=i+2

    str2=""
    i=0
    while i<n:
        str2+=str(l[i])
        i+=1
    return str2

# def string_vowel(str1):
#     l=list(str1)
#     n=len(str1)
#     s=0
#     d={'a':1,'e':2,'i':3,'o':4,'u':5}
#
#     for i in range(n):
#         if i==n-1 or l[i+1]==' ':
#             e=i
#             while s<e:
#                 if l[s] in d.keys():
#                     l[s]=d[l[s]]
#                 s+=1
#             s=i+2
#
#     str2=""
#     i=0
#     while i<n:
#         str2+=str(l[i])
#         i+=1
#     return str2

def string6(str1):
    l=list(str1)
    n=len(str1)
    flag=0
    s=0

    for i in range(n):

        if i==n-1 or l[i+1]==' ':
            temp=0
            e=i
            if not flag:
                while s<e:
                    l[s+1]=temp+1
                    temp+=2
                    s+=2
                flag=1
            else:
                while s<e:
                    l[s]=temp
                    temp+=2
                    s+=2
                flag=0
            s=i+2

    str2=""
    i=0
    while i<n:
        str2+=str(l[i])
        i+=1
    return str2

def string7(str1):
    l=list(str1)
    n=len(str1)
    s=0
    d={'a':4,'e':3,'i':1,'o':0,'s':5,'z':2,'b':6,'t':7,'r':8,'q':9}

    for i in range(n):
        if i==n-1 or l[i+1]==' ':
            e=i
            while s<=e:
                if l[s] in d.keys():
                    l[s]=d[l[s]]
                s+=1
            s=i+2

    str2=""
    i=0
    while i<n:
        str2+=str(l[i])
        i+=1
    return str2

def sort(a):
    n=len(a)

    for i in range(n-1):
        f=1
        for j in range(n-1,i,-1):
            if ord(a[j-1])>ord(a[j]):
                a[j],a[j-1]=a[j-1],a[j]
                f=0
        if f:
            break
    return a

def string8(str1):
    l=list(str1)
    n=len(str1)
    s=0

    for i in range(n):
        if i==n-1 or l[i+1]==' ':
            e=i
            l[s:e+1]=sort(l[s:e+1])
            s=i+2

    str2=""
    i=0
    while i<n:
        str2+=l[i]
        i+=1
    return str2

def string9(str1):
    l=list(str1)
    n=len(str1)

    str2=""
    choice=2
    x=0


    while x<choice:
        s=0
        for i in range(n):
            if i==n-1 or l[i+1]==' ':
                e=i
                temp=ord(l[s+x])
                if temp>90:
                    str2+=chr(temp-32)
                else:
                    str2+=chr(temp)
                s=i+2
        str2+=" "
        x+=1
    return str2

def string10(str1):
    l=list(str1)
    n=len(str1)
    s=0
    d={'a':1,'e':2,'i':3,'o':4,'u':5}

    for i in range(n):
        if i==n-1 or l[i+1]==' ':
            e=i
            while s<e:
                if l[s] in d.keys():
                    temp=ord(l[s])
                    if temp>90:
                        l[s]=chr(temp-32)
                    else:
                        l[s]=chr(temp)
                s+=1
            s=i+2

    str2=""
    i=0
    while i<n:
        str2+=str(l[i])
        i+=1
    return str2

def string11(str1):
    l=list(str1)
    n=len(str1)
    s=0
    d={'a':'e','e':'i','i':'o','o':'u','u':'a'}

    for i in range(n):
        if i==n-1 or l[i+1]==' ':
            e=i
            while s<=e:
                if l[s] in d.keys():
                    l[s]=d[l[s]]
                s+=1
            s=i+2

    str2=""
    i=0
    while i<n:
        str2+=str(l[i])
        i+=1
    return str2

def string12(str1):
    l=list(str1)
    n=len(str1)
    s=0

    index=0
    d={'a':'e','e':'i','i':'o','o':'u','u':'a'}
    str2=""
    # print(d.keys())

    for i in range(n):
        if i==n-1 or l[i+1]==' ':
            e=i
            flag=0
            while s<=e:
                if l[s] in d.keys() and not flag:
                    index=s
                    temp=ord(d[l[s]])
                    if temp>90:
                        l[s]=chr(temp-32)
                    else:
                        l[s]=chr(temp)
                    flag=1
                s+=1
            # s=0
            # while s<=e:
            #     if s<index and flag:
            #         temp=ord(l[s])
            #         if temp==65 or temp==97:
            #             l[s]=chr(temp+25)
            #         else:
            #             l[s]=chr(temp-1)
            #
            #
            #     # if  s==index and flag:
            #
            #
            #
            #     if s>index and flag:
            #         temp=ord(l[s])
            #         if temp==90 or temp==122:
            #             l[s]=chr(temp-25)
            #         else:
            #                 l[s]=chr(temp+1)
            #     s+=1
            s=i+2

    str2=""
    i=0
    while i<n:
        str2+=str(l[i])
        i+=1
    return  str2




print(string1(str1))
print(string2(str1))
print(string3(str1))
print(string4(str1))
print(string5(str1))
print(string6(str1))
print(string7(str1))
print(string8(str1))
print(string9(str1))
print(string10(str1))
print(string11(str1))
# print(string12(str1))
