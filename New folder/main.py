from inventory import Inventory
from inventory_mngt import Inventory_mngt

if (__name__ == "__main__"):
    obj = Inventory_mngt()
    while True:
        print("1.Login as a ADMIN"+"\n"+"2.Login as a User"+"\n"+"3.Exit")
        choice = int(input("Enter the choice :"))
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
                
                action=int(input("Enter your choice :"))
                

                if action==1: #Add Goods
                    gid=int(input("Enter the goods id :"))
                    gname=input("Enter the name of the goods :")
                    qty=int(input("Enter the quantity :"))
                    price=int(input("Enter the price of goods :"))
                    Cost =price * qty

                    with open("Goods_record.doc","r") as fp:
                        for ele in fp:
                            split_text = ele.split(",")
                            if split_text[0]==str(gid):
                                print("Goods with this ID already exist !!! Use another ID")
                                break
                            elif split_text[1]==gname:
                                    print("Entered goods is already exist in the record...")
                                    break
                        else:
                                g=Inventory(gid,gname,qty,price,Cost)
                                obj.addgoods(g)
                                
                            
                elif action==2: #Display Goods
                    obj.Display()
                elif action==3: #Search by ID
                    id=int(input("Enter the Good's ID :"))
                    obj.search_id(id)
                elif action==4: #Search by name
                    Name=input("Enter the Good's Name :")
                    obj.search_name(Name)
                elif action==5: #Delete Goods
                    Name1=input("Enter the Good's Name :")
                    obj.Delete_goods(Name1)
                elif action==6: #Update
                    u_id=int(input("Enter id of record to update :"))
                    obj.Update_record(u_id)

                     
                    
        if choice==2:
            obj.user_login()
