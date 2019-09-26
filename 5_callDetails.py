class CallDetail:
    def __init__(self,call_from,call_to,call_duration,call_type):
        self.c_from=call_from
        self.c_to=call_to
        self.c_duration=call_duration
        self.c_type=call_type

    print("Call details:\n")
    def details(self):
        print("Call from: ",self.c_from,"\nCall To: ",self.c_to,"\nDuration: ",self.c_duration,"\nType: ",self.c_type,"\n")
        

class Util:
    list_of_call_objects=[]
    def __init_(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        for i in list_of_call_string:
            l=i.split(',')
            self.list_of_call_objects.append(CallDetail(l[0],l[1],l[2],l[3]))

        
    def call_details(self):
        for i in self.list_of_call_objects:
            i.details()
            

call1='9000000001,90000000002,25,STD'
call2='9000000003,90000000004,5,Local'
call3='9000000005,90000000006,25,ISD'

list_of_call_string=[call1,call2,call3]
Util().parse_customer(list_of_call_string)
Util().call_details()
