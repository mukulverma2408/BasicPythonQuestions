# Calculate the complete age of a person in years, months and days
from datetime import datetime

def validateDOB():
    dob = input("Enter date of birth in DD/MM/YYYY format : ")
    dobFormatted = datetime.strptime(dob, "%d/%m/%Y").date()
    currdate = datetime.now().date()
    if dobFormatted <= currdate:
        print("DOB is valid, Moving Ahead!!!")
        diff = currdate - dobFormatted
        print("Age is : {}".format(diff))
    elif dobFormatted > currdate:
        print("Invalid DOB entered, please enter correct date")
        exit(1)

validateDOB()
