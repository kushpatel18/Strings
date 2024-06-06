str1=input("Enter a string: ")
target=input("Enter a character: ")
start=int(input("Enter a starting index: "))
end=int(input("Enter an end index: "))

def Count(str1,target,start=0,end=len(str1)):
    length=0
    count=0

    for i in str1:
        length+=1

    try:
        for j in range(start,end):
            if str1[j]==target:
                count+=1
    except IndexError:
        if start< (-length):
            start=(-length)
        if end>=length:
            end=length-1
        if end<(-length):
            end=(-length)
        return Count(str1,target,start,end)


    return count

print("Character Count: ",Count(str1,target,start,end))


