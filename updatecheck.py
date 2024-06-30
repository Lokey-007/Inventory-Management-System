def Add_emp(self):
    Emp_id=input("Enter employee ID :")
    record_present=False
    with open("Emp_record.doc","r") as fp:
        for ele in fp:
            split_record=ele.split(",")
            if Emp_id==split_record[0]:
                record_present=True
                print("***************************************************")
                print("Employee record already exist...")
                print("***************************************************")
                break
            elif record_present==False:
                Emp_password=input("Assign password :")
        if record_present==False:
            with open("Emp_record.doc","a") as fp:
                fp.write(Emp_id+","+Emp_password+"\n")
                print("Emp record added successfully.")