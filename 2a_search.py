def search():
    l=[]
    n = int(input("Enter the number of elements in the list:"))
    print("Enter the numbers from smallest to the largest:")
    for i in range(n):
        x = int(input())
        l.append(x)
    key = int(input("Enter the key element:"))
    if key in l:
        flag=True
    else:
        flag=False
    if flag==True:
        return 'Key element found'
    else:
        return 'Key element not found'

a = search()
print(a)
