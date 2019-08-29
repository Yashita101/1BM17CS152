def reverse1(str1):
    l=[]
    l = str1.split(' ')
    l.reverse()
    return ' '.join(l)
    
    
def reverse2(str1):
    l=[]
    l = str1[::-1].split(' ')
    l.reverse()
    return ' '.join(l)

str1 = input("Enter your sentence:")

x = reverse1(str1)
y = reverse2(str1)
print('OUTPUT 1:',x,'\n')
print('OUTPUT 2:',y,'\n')
