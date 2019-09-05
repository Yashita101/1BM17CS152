import random
import string
def password():
    pwd=""
    ctr=0
    length=int(input("How many characters would you want in your password?\n"))
    while ctr!=length:
        uppercase = [random.choice(string.ascii_uppercase)]
        print(uppercase)
        lowercase = [random.choice(string.ascii_lowercase)]
        num = [random.choice(string.digits)]
        symbol = [random.choice(string.punctuation)]
        complete_pwd = uppercase+lowercase+num+symbol
        pwd+=random.choice(complete_pwd)
        ctr+=1
        continue
    if ctr==length:
        print(pwd)
password()
