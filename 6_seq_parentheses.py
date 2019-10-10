class str_parentheses:
    def __init__(self,str1):
        self.sequence_str=str1
    def parentheses(self):
        l=list(self.sequence_str)
        s1=[]
        s2=[]
        s3=[]
        for i in l:
            if i=='(':
                s1.append(i)
            if i==')':
                if s1:
                    s1.pop()
                else:
                    return 0

            if i=='{':
                s2.append(i)
            if i=='}':
                if s2:
                    s2.pop()
                else:
                    return 0

            if i=='[':
                s3.append(i)
            if i==']':
                if s3:
                    s3.pop()
                else:
                    return 0
        if s1 or s2 or s3:
            return 0
        else:
            return 1

seq_str=input("Enter your sequence of string parentheses:\n")
ob1=str_parentheses(seq_str)
if(ob1.parentheses()):
    print("Valid sequence.")
else:
    print("Invalid sequence.")

