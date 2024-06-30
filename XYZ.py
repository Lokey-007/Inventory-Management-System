def user_login(self):
    while True:
        emp_name = input("Enter your name: ")
        emp_id = input("Enter your employee ID: ")
        found = False
        
        with open("Emp_record.doc", "r") as fp:
            for element in fp:
                splitit = element.strip().split(",")
                if splitit[0] == emp_id:
                    found = True
                    emp_pass = input("Enter your password: ")
                    if splitit[1] == emp_pass:
                        print("*****************************************************")
                        print("______________Employee login Successful.______________")
                        print("*****************************************************")
                        return  # exit the function after successful login
                    else:
                        print("---------------------------------------------------")
                        print("______________Enter correct password.______________")
                        print("---------------------------------------------------")
                        break  # break the loop if password is incorrect
        
            if not found:
                print("------------------------------------------------------")
                print("______________Enter correct Employee ID______________")
                print("------------------------------------------------------")
