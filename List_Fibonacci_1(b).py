def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

num=int(input("Enter the number of fibonacci numbers you need:"))
l=[]
if num<=0:
    print("Incorrect input.Enter a positive integer.")
for i in range(num):
    x=fibonacci(i)
    l.append(fibonacci(i))

print(l)

        
