def overlapping():
    file1=open("/home/bmsce/Yashita/happy_numbers.txt","r")
    file2=open("/home/bmsce/Yashita/prime_numbers.txt","r")
    if file1 and file2:
        str1=file1.read()
        str2=file2.read()
        l1=str1.split(',')
        l2=str2.split(',')
        print("Overlapped Numbers are:")
        for i in l1:
            for j in l2:
                if i==j:
                    print(j)
              
    file1.close()
    file2.close()
overlapping()

