Emp_id=input("Enter Emp ID :")
password=input("Enter assigned password :")
record = Emp_id + "," + password

record_present=False
with open("abc.doc","r") as fp:
    for ele in fp:
        split_record = ele.split(",")
        if split_record[0]==Emp_id:
            print("Emp record already exist...")
            record_present==True
            break
if record_present==False:
    with open("abc.doc","a") as fp:
        fp.write(record +","+"\n")
        #fp.write("\n")
        print("Emp record addeed successfully.")