def even():
    l=[]
    l1=[]
    n = int(input("Enter the length of the list:"))
    print("Enter the numbers:")
    for i in range(n):
        ele = int(input())
        l.append(ele)
        if(l[i]%2==0):
            l1.append(l[i])
    print(l1)

even()


    
        
