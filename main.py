from inventory import Inventory
from inventory_mngt import Inventory_mngt
from exception1 import Invalidchoice
import sys


if (__name__ == "__main__"):
    obj = Inventory_mngt()
    while True:
        print("1.Login as a ADMIN"+
              "\n"+"2.Login as a User"+
              "\n"+"3.Exit")
        try :
            choice = int(input("Enter the choice :"))
            try :
                if choice<0 or choice>3:
                    raise Invalidchoice(choice)
            except Invalidchoice as e :
                print("----------------------------------------------")
                print(e)
                print("----------------------------------------------")
        except ValueError :
                print("----------------------------------------------")
                print("_______Please enter integer as a choice._______")
                print("----------------------------------------------")
        else:
                if choice ==1:
                    obj.admin_login()
                    while True:
                        print(("1.Add Goods."+
                            "\n"+"2.Display Goods"+
                            "\n"+"3.Search Goods by id"+
                            "\n"+"4.Search Goods by Name"+
                            "\n"+"5.Delete Record"+
                            "\n"+"6.Update Record"+
                            "\n"+"7.Add Emp in Record"+
                            "\n"+"8.Delete Emp in Record"+
                            "\n"+"9.Exit"))
                        try :
                            action=int(input("Enter your choice of admin :"))
                            try :
                                if action<0 or action>9 :
                                    raise Invalidchoice(action)
                            except Invalidchoice as e :
                                print("----------------------------------------------")
                                print(e)
                                print("----------------------------------------------")
                        except ValueError :
                            print("----------------------------------------------")
                            print("_______Please enter integer as a choice._______")
                            print("----------------------------------------------")
                        else:
                            if action==1: #Add Goods
                                try :
                                    gid=int(input("Enter the goods id :"))
                                except ValueError:
                                    print("----------------------------------------------")
                                    print("_______Goods ID MUST be integer._______")
                                    print("----------------------------------------------")
                                else:
                                    gname=input("Enter the name of the goods :")
                                    try:
                                        qty=int(input("Enter the quantity :"))
                                        price=int(input("Enter the price of goods :"))
                                    except ValueError:
                                        print("----------------------------------------------")
                                        print("_______Goods quantity MUST be integer._______")
                                        print("----------------------------------------------")
                                    else:
                                        Cost =price * qty

                                    with open("Goods_record.doc","r") as fp:
                                        for ele in fp:
                                            split_text = ele.split(",")
                                            if split_text[0]==str(gid):
                                                print("***************************************************")
                                                print("Goods with this ID already exist !!! Use another ID")
                                                print("***************************************************")
                                                break
                                            elif split_text[1]==gname:
                                                    print("***************************************************")
                                                    print("Entered goods is already exist in the record...")
                                                    print("***************************************************")
                                                    break
                                        else:
                                            g=Inventory(gid,gname,qty,price,Cost)
                                            obj.addgoods(g)
                                            
                                        
                            elif action==2: #Display Goods
                                obj.Display()
                            elif action==3: #Search by ID
                                try:
                                    id=int(input("Enter the Good's ID :"))
                                except ValueError:
                                    print("----------------------------------------------")
                                    print("_______Enter ID as a integer._______")
                                    print("----------------------------------------------")
                                else:
                                    obj.search_id(id)
                            elif action==4: #Search by name
                                Name=input("Enter the Good's Name :")
                                obj.search_name(Name)
                            elif action==5: #Delete Goods
                                Name1=input("Enter the Good's Name :")
                                obj.Delete_goods(Name1)
                            elif action==6: #Update
                                try :
                                    u_id=int(input("Enter id of record to update :"))
                                except ValueError:
                                    print("----------------------------------------------")
                                    print("_______Enter ID as a integer._______")
                                    print("----------------------------------------------")
                                else:
                                    obj.Update_record(u_id)
                            elif action==7: #Add Emp in Record
                                obj.Add_emp()
                            elif action==8: #Delete Emp in Recor
                                Emp_ID = input("Enter Employee ID to delete :")
                                obj.Delete_Emp(Emp_ID)
                            elif action==9:
                                print("--------------------------------------------------------------------")
                                print("*******************Admin Closed Successfully*********************")
                                print("--------------------------------------------------------------------")
                                break


                            
                if choice==2: #User Login
                    obj.user_login()
                    while True:
                        print(("1.Withdraw Goods."+
                            "\n"+"2.Display Goods"+
                            "\n"+"3.Search Goods by id"+
                            "\n"+"4.Search Goods by Name"+
                            "\n"+"5.Return Goods"+
                            "\n"+"6.Exit"))
                        try :
                            emp_action=int(input("Enter your choice user :"))
                            try:
                                if emp_action<0 or emp_action>6:
                                    raise Invalidchoice(emp_action)
                            except Invalidchoice as e:
                                print("----------------------------------------------")
                                print(e)
                                print("----------------------------------------------")
                        except ValueError:
                            print("----------------------------------------------")
                            print("_______Please enter integer as a choice._______")
                            print("----------------------------------------------")
                        else:
                            if emp_action==1: # Withdraw Goods
                                obj.withdraw()
                            elif emp_action==2: #Display Goods
                                obj.Display()
                            elif emp_action==3: #Search_by_ID
                                try:
                                    id=int(input("Enter the Good's ID :"))
                                except ValueError:
                                    print("----------------------------------------------")
                                    print("_______Please enter integer as a Goods ID._______")
                                    print("----------------------------------------------")
                                else:
                                    obj.search_id(id)
                            elif emp_action==4 : #Search_by_Name
                                Name=input("Enter the Good's Name :")
                                obj.search_name(Name)
                            elif emp_action==5: #Return Goods
                                obj.Return()
                            elif emp_action==6:
                                print("--------------------------------------------------------------------")
                                print("******************--User Closed Successful--********************")
                                print("--------------------------------------------------------------------")
                                break

                elif choice==3:
                    print("--------------------------------------------------------------------")
                    print("************************--Inventory Closed--************************")
                    print("--------------------------------------------------------------------")
                    break
