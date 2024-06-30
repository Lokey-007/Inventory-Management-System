from inventory import Inventory
import datetime
import os

class Inventory_mngt:
    def addgoods(self,g):
        with open("Goods_record.doc","a") as fp:
            fp.write(str(g))
            print("***************************************************")
            print("Goods added successfully...")
            print("***************************************************")
            with open("inventory_records.doc","a") as fp:
                date = datetime.datetime.now()
                fp.write("Goods Added"+"-->"+(str(g)).replace("\n"," ")+"on - "+str(date)+"\n")
            

    def admin_login(self):
        while True:
            username= input("Enter Username :")
            if username == "Lokeshgim":
                password = input("Enter your password :")
                if password == "Lokesh@inventory":
                    print("***************************************************")
                    print("Login Successful...")
                    print("***************************************************")
                    break
                else:
                    print("***************************************************")
                    print("Please Enter correct password...")
                    print("***************************************************")
            else:
                print("***************************************************")
                print("Invalid username...")
                print("***************************************************")

    def Display(self):
        with open("Goods_record.doc","r") as fp:
            print("***************************************************")
            for ele in fp:
                print(ele)
                print("----------------------------------------------")
            print("***************************************************")

    def search_id(self,id):
        with open("Goods_record.doc","r") as fp:
            for ele in fp:
                split_text=ele.split(",")
                if split_text[0]==str(id):
                    print("***************************************************")
                    print(ele)
                    print("Record Found...")
                    print("****************************************************")
                    break
            else:
                print("***************************************************")
                print("Record not found...")
                print("***************************************************")


    def search_name(self,Name):
        Name_lowered = Name.lower()
        with open("Goods_record.doc","r") as fp:
            for ele in fp:
                split_text=ele.split(",")
                if split_text[1].lower() == Name_lowered:
                    print("**************************************************")
                    print(ele)
                    print("Record Found...")
                    print("***************************************************")
                    break
            else:
                print("***************************************************")
                print("Record not found...")
                print("***************************************************")
                

    def Delete_goods(self,Name1):
        Name1_lowered = Name1.lower()
        with open("Goods_record.doc","r") as fp:
            record =[]
            isFound=False
            for ele in fp:
                splited_text=ele.split(",")
                if splited_text[1].lower()== Name1_lowered:
                    isFound=True
                    print("***************************************************")
                    print("Record deleted successfully...")
                    print("***************************************************")
                    with open("inventory_records.doc","a") as fp:
                        date = datetime.datetime.now()
                        fp.write("Goods record Deleted"+"-->"+(str(ele)).replace("\n"," ")+"on - "+str(date)+"\n")
                else:
                    record.append(ele)
        if isFound==True:
            with open("Goods_record.doc","w") as fp:
                for x in record:
                    fp.write(x)
        else:
            print("***************************************************")
            print("Record Not Found!!!")
            print("***************************************************")

    def Update_record(self,u_id):
        with open("Goods_record.doc","r") as fp:
            update=[]
            isFound=False
            isupdate= True
            for ele in fp:
                split1=ele.split(",")
                if split1[0]==str(u_id):
                    isFound=True
                    uname=input("Enter Good's updated name :")
                    namelist=[]
                    with open("Goods_record.doc","r") as fp:
                        for ele1 in fp:
                            split2=ele1.split(",")
                            if uname!=split2[1] or uname==split1[1]:
                                try:
                                    uqty=int(input("Enter Good's updated quantity :"))
                                    uprice=int(input("Enter Good's updated price :"))
                                except ValueError:
                                    print("----------------------------------------------")
                                    print("_______Goods quantity MUST be integer._______")
                                    print("----------------------------------------------")
                                else:
                                    cost=uqty*uprice
                                break
                            else:
                                print("***************************************************")
                                print("_______Goods with this name already exist !!!_______")
                                print("***************************************************")
                                isupdate=False
                                break
                    if isupdate==True:
                        u=Inventory(split1[0],uname,uqty,uprice,cost)
                        update.append(str(u))
                        print("***************************************************")
                        print("__________Record updates successfully...__________")
                        print("***************************************************")
                        with open("inventory_records.doc","a") as fp:
                            date = datetime.datetime.now()
                            fp.write("Goods record Updated from"+"-->"+(str(ele)).replace("\n"," ")+"TO  "+str(u).replace("\n"," ")+"on - "+str(date)+"\n")
                    else:
                        break
                else:
                    update.append(ele)
        if isFound==True and isupdate==True:
            with open("Goods_record.doc","w") as fp:
                for x in update:
                    fp.write(x)
        elif isupdate==False:
            pass
        else:
            print("***************************************************")
            print("______________Record Not Found!!!______________")
            print("***************************************************")


    def Add_emp(self):
        Emp_id=input("Enter employee ID :")
        record_present=False
        with open("Emp_record.doc","r") as fp:
            for ele in fp:
                split_record=ele.split(",")
                if split_record[0]==Emp_id:
                    record_present=True
                    print("***************************************************")
                    print("_________Employee record already exist..._________")
                    print("***************************************************")
                    break
            if record_present==False:
                Emp_password=input("Assign password :")
                
            if record_present==False:
                with open("Emp_record.doc","a") as fp:
                    fp.write(Emp_id+","+Emp_password+","+"\n")
                    open(Emp_id + ".doc" ,"w")
                    open(Emp_id + "_cal.doc" ,"w")
                    print("***************************************************")
                    print("__________Emp record added successfully.__________")
                    print("***************************************************")
                
    def Delete_Emp(self,Emp_ID):
        with open("Emp_record.doc","r") as fp:
            record =[]
            isFound=False
            for eled in fp:
                splited_text=eled.split(",")
                if str(Emp_ID)==splited_text[0]:
                    isFound=True
                    print("***************************************************")
                    print("__________Record deleted successfully...__________")
                    print("***************************************************")
                    os.rename(str(Emp_ID)+".doc",str(Emp_ID)+"_deleted.doc")
                    os.rename(str(Emp_ID)+"_cal.doc",str(Emp_ID)+"_deletedcal.doc")
                else:
                    record.append(eled)
            if isFound==True:
                    with open("Emp_record.doc","w") as fp:
                        for x in record:
                            fp.write(x)
            else:
                print("***************************************************")
                print("______________Record Not Found!!!______________")
                print("***************************************************")


                    
    def user_login(self):
        while True:
            login = "Notone"
            emp_name=input("Enter your name :")
            emp_id=input("Enter your employee ID :")
            global storename
            global storeemp
            storeemp = emp_id
            storename = emp_name
            found=False
            with open("Emp_record.doc","r") as fp:
                for element in fp:
                    splitit=element.strip().split(",")
                    if splitit[0]==emp_id:
                        found=True
                        emp_pass=input("Enter your password :")
                        if splitit[1]==emp_pass:
                            print("*****************************************************")
                            print("______________Employee login Successful.______________")
                            print("*****************************************************")
                            login="Done"
                            break
                        else:
                            print("---------------------------------------------------")
                            print("______________Enter corrct password.______________")
                            print("---------------------------------------------------")
                            
                else:
                    print("------------------------------------------------------")
                    print("______________Enter correct Employee ID______________")
                    print("------------------------------------------------------")
            if login=="Done":
                break   
            
                        

    def withdraw(self):
        try:
            wid=int(input("Enter the id of Goods to withdraw :"))
        except ValueError:
            print("----------------------------------------------")
            print("_______Please enter integer as a Goods ID._______")
            print("----------------------------------------------")
        else:
            with open("Goods_record.doc","r") as fp:
                withdraw=[]
                found=False
                found1=False
                for goods in fp:
                    split_good=goods.split(",")
                    if split_good[0]==str(wid):
                        found=True
                        try:
                            wqty=int(input("Enter the quantity :"))
                        except ValueError:
                            print("----------------------------------------------")
                            print("_______Please enter integer as a quantity._______")
                            print("----------------------------------------------")
                        else:
                            if wqty < int(split_good[2]):
                                found1=True
                                w=Inventory( split_good[0] , split_good[1] , (int(split_good[2])-wqty) , split_good[3], (int(split_good[2])- wqty)  * int(split_good[3] ))
                                withdraw.append(str(w))

                                print("***************************************************")
                                print("Goods Withdrawed Successfully...")
                                print("***************************************************")
                                with open("inventory_records.doc","a") as fp:
                                    date = datetime.datetime.now()
                                    fp.write("Goods Withdraw "+"-->"+(str(split_good[0]))+" - "+(str(split_good[1]))+" - "+str(wqty)+" - "+str(split_good[3])+" - "+str(wqty*int(split_good[3]))+" - "+"on - "+str(date)+ "-->" + storeemp+"-"+storename +"\n")
                                with open(storeemp+".doc" ,"a" )as fp:
                                    fp.write("Goods Withdraw "+" - "+(str(split_good[0]))+" - "+(str(split_good[1]))+" - "+str(wqty)+" - "+str(split_good[3])+" - "+str(wqty*int(split_good[3]))+" - "+"on - "+str(date)+ "-->"+"\n")
                                with open(storeemp+"_cal.doc","a")as fp:
                                    fp.write((str(split_good[0]))+" - "+(str(split_good[1]))+" - "+str(wqty)+" - "+"\n")
                            else:
                                print("***************************************************")
                                print("Inventory does not have sufficient goods...")
                                print("For now you can only withdraw =",split_good[2])
                                print("***************************************************")
                    else:
                        withdraw.append(goods)
            if found==True and found1==True:
                with open("Goods_record.doc","w")as fp: 
                    for x in withdraw:
                        fp.write(x)
            elif found==False:
                print("***************************************************")
                print("Record with entered ID not exists")
                print("***************************************************")

    def Return(self):
        greturn = False
        returned = False
        try:
            rid=int(input("Enter the id of Goods want to return :"))
        except ValueError:
            print("----------------------------------------------")
            print("_______Please enter integer as a Goods ID._______")
            print("----------------------------------------------")
        else:
            with open("Goods_record.doc","r") as fp:
                Return_good=[]
                found_good=False
                for good in fp:
                    split_goods=good.split(",")
                    if split_goods[0]==str(rid):
                        found_good=True


                        with open(storeemp + "_cal.doc" , "r") as fp:
                            withdrawed_found = False
                            for withd in fp:
                                split_withd = withd.split("-")
                                if split_withd[0].strip() == str(rid):
                                    withdrawed_found = True
                                    try:
                                        rqty=int(input("Enter the quantity to return :"))
                                    except ValueError:
                                        print("----------------------------------------------")
                                        print("_______Please enter integer as a Quantity._______")
                                        print("----------------------------------------------")
                                    else:
                                        if int((split_withd[2].strip())) >= rqty:
                                            r=Inventory( split_goods[0] , split_goods[1] , (int(split_goods[2]) + rqty) , split_goods[3] , (int(split_goods[2]) + rqty) * int(split_goods[3]))
                                            Return_good.append(str(r))
                                            returned = True
                                            
                                            print("********************************************************************")
                                            print("Goods returned successful...")
                                            greturn = True
                                            print("********************************************************************")
                                            with open("inventory_records.doc","a") as fp:
                                                date = datetime.datetime.now()
                                                fp.write("Goods Returned "+"-->"+(str(split_goods[0]))+" - "+(str(split_goods[1]))+" - "+str(rqty)+" - "+str(split_goods[3])+" - "+str(rqty*int(split_goods[3]))+" - "+"on - "+str(date) + str(storeemp)+"-"+storename +"\n")
                                            with open(storeemp + ".doc","a") as fp:
                                                fp.write("Goods Returned "+"-->"+(str(split_goods[0]))+" - "+(str(split_goods[1]))+" - "+str(rqty)+" - "+str(split_goods[3])+" - "+str(rqty*int(split_goods[3]))+" - "+"on - "+str(date)+"\n")
                                        else:
                                            print("******************************************************************************")
                                            print("The quantity of goods that you want to return is greater than quantity of goods that you withdrawed...-->Return Quantity should be less than or equal to Withdrawed...")
                                            print("******************************************************************************")
                                            return False
                            else :
                                if greturn == False:
                                    print("******************************************************************************")
                                    print("_____",rid," is not withdrawed by ",storeemp," so you can not return it..._____")
                                    print("******************************************************************************")
                    
                    else:
                        Return_good.append(good)
            if found_good==True and withdrawed_found==True and returned==True:
                with open("Goods_record.doc","w") as fp:
                    for x in Return_good:
                        fp.write(x)
            else:
                print("***************************************************")
                print("Record with entered ID not exists")
                print("***************************************************")


        with open(storeemp + "_cal.doc","r") as fp1:
                cal_updated = False
                returncal=[]
                for withd_good in fp1:
                    split_withd_good = withd_good.split("-")
                    if split_withd_good[0].strip() == str(rid):
                        wid = split_withd_good[0]
                        wname = split_withd_good[1]
                        wqty = int(split_withd_good[2].strip())- rqty
                        wrecord = (wid + " - " + wname + " - "+str(wqty)+"\n")
                        returncal.append(wrecord)
                        cal_updated =True
                    else:
                        returncal.append(withd_good)
        if cal_updated == True:
                with open(storeemp + "_cal.doc","w") as fp:
                    for x in returncal:
                        fp.write(x)