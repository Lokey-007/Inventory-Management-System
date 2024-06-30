from inventory import Inventory


class Inventory_mngt:
    def addgoods(self,g):
        with open("Goods_record.doc","a") as fp:
            fp.write(str(g))
            print("Goods added successfully...")
            

    def admin_login(self):
        while True:
            username= input("Enter Username :")
            if username == "Lokeshgim":
                password = input("Enter your password :")
                if password == "Lokesh@inventory":
                    print("Login Successful...")
                    break
                else:
                    print("Please Enter correct password...")
            else:
                print("Invalid username...")

    def Display(self):
        with open("Goods_record.doc","r") as fp:
            for ele in fp:
                print(ele)

    def search_id(self,id):
        with open("Goods_record.doc","r") as fp:
            for ele in fp:
                split_text=ele.split(",")
                if split_text[0]==str(id):
                    print(ele)
                    print("Record Found...")
                    break
                else:
                    print("Record not found...")


    def search_name(self,Name):
        with open("Goods_record.doc","r") as fp:
            for ele in fp:
                split_text=ele.split(",")
                if split_text[1]==Name:
                    print(ele)
                    print("Record Found...")
                    break
            else:
                print("Record not found...")
                

    def Delete_goods(self,Name1):
        with open("Goods_record.doc","r") as fp:
            record =[]
            isFound=False
            for ele in fp:
                splited_text=ele.split(",")
                if splited_text[1]==Name1:
                    isFound=True
                    print("Record deleted successfully...")
                    pass
                else:
                    record.append(ele)
        if isFound==True:
            with open("Goods_record.doc","w") as fp:
                for x in record:
                    fp.write(x)
        else:
            print("Record Not Found!!!")

    def Update_record(self,u_id):
        with open("Goods_record.doc","r") as fp:
            update=[]
            isFound=False
            for ele in fp:
                split1=ele.split(",")
                if split1[0]==str(u_id):
                    isFound=True
                    uid=int(input("Enter Good's updated ID :"))
                    uname=input("Enter Good's updated name :")
                    uqty=int(input("Enter Good's updated quantity :"))
                    uprice=int(input("Enter Good's updated price :"))
                    cost=uqty*uprice
                    u=Inventory(uid,uname,uqty,uprice,cost)
                    update.append(str(u))
                    print("Record updates successfully...")
                else:
                    update.append(ele)
        if isFound==True:
            with open("Goods_record.doc","w") as fp:
                for x in update:
                    fp.write(x)
        else:
            print("Record Not Found!!!")


                    
    def user_login(self):
        while True:
            #Emp_name=input("Enter name :")
            empid=input("Enter your Emp ID :")
            with open("Emp_record.doc","r") as fp:
                for ele in fp:
                    splitted_text=ele.split(",")
                    if str(empid)==splitted_text[0]:
                        emp_pass=input("Enter the password :")
                        if (emp_pass)==str(splitted_text[1]):
                            print("Login Successful...")
                            break
                        else:
                            print("Please enter correct password...")
                    else:
                        ("Enter valid empID...")