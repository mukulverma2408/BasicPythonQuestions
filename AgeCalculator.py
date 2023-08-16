# Calculate the complete age of a person in years, months and days

from datetime import datetime

def ValidateDOB():
    dt = input("Enter DOB in DD/MM/YYYY format : ")
    dob = datetime.strptime(dt, "%d/%m/%Y")
    dob = datetime.strftime(dob, "%d-%m-%Y")
    current_date = datetime.now().strftime("%d-%m-%Y")
    print("Current date is {}".format(current_date))
    print("Entered date of birth is {}".format(dob))
    if (current_date >= dob):
        print("Valid Date, Moving Ahead")
        #age = (current_date - dob)
        print(type(current_date))
        print(type(dob))
        #print("Age is : {}".format(age))
    else:
        print("Date is not valid, please enter correct date")
        exit(1)

ValidateDOB()


