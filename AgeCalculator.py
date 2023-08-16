# Calculate the complete age of a person in years, months and days

from datetime import datetime

def ValidateDOB():
    dt = input("Enter DOB in DD/MM/YYYY format : ")
    #day, month, year = map(int, dt.split('/'))
    #print(day, month, year)
    #dob = datetime(day, month, year)
    dob = datetime.strptime(dt, "%d/%m/%Y")
    dob = datetime.strftime(dob, "%d-%m-%Y")
    current_date = datetime.now().strftime("%d-%m-%Y")
    print(current_date)
    print(dob)

ValidateDOB()


