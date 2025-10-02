
class BookAppoinments:
    def book_appointment(self,dict_dr):
        self.dict_dr = dict_dr
        name = input("Enter name ::: ")
        c_no=int(input("Enter Mobile no ::: "))
        age = int(input("Enter Age :: "))
        dr_name = input("Enter dr name 'Dr. Shah','Dr. Patel','Dr. Modi' ")
        if dr_name not in dict_dr:
            dr_name = input("Enter dr name 'Dr. Shah','Dr. Patel','Dr. Modi' ")
            
        print(dict_dr[dr_name])
        for i in dict_dr[dr_name]:
            print(i,end="\t")
        book_slot=input("Enter your slot ")
        if book_slot not in dict_dr[dr_name]:
            print("Please enter only avaialable slots only")
        else:
            if self.doctorAvailibity(dr_name,book_slot):
                return c_no,name,age,dr_name,book_slot 

                

        pass
    def viewApprointment(self,data):
        print(data)
    def doctorAvailibity(self,dr_name,slot):       
       
        if self.dict_dr[dr_name][slot]<3:
            self.dict_dr[dr_name][slot]+=1
            print("SLOTS ",self.dict_dr)
            return 1
        else:
            print("Please enter select another slot ") 
        #print("After ",self.dict_dr)

        #return dict

dict={'Dr Shah':{'10 am':0 , '11 am':0 , '12 pm':0},
              'Dr Patel':{'11 am':0 , '12 pm':0}
              }
obj=BookAppoinments()
while True:
    
    data=obj.book_appointment(dict)
    obj.viewApprointment(data)
    ch=input("Do you want to continue ? Yes or No ")
    if ch=='NO':
        break