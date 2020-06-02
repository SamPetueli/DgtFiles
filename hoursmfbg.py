# Prints a basic question and asks for user input
hourly_rate = float(input("How much money do you make an hour?"))
hours_worked = float(input("How many hours have you worked this week?"))

# Prints the hourly rate multiplied by the hours worked
weekly_pay = hourly_rate * hours_worked
print("Your weekly pay is {} dollars.".format(weekly_pay))

# Prints annual income by weekly pay multiplied by the number of weeks in a year
annual_income = weekly_pay * 52
print("You make {} each year! (not including tax and provided all weeks have been worked)".format(annual_income))

if annual_income <=34000:
  print("You have a low income.")
elif annual_income <=50000:   
  print("You have a moderate income.")
elif annual_income <=74000:
  print("You have a high income.")
else:
  print("You have even more potential to earn!")
   
internet_hours = int(input("How many hours do you spend on the internet each day?"))

if internet_hours >=0 and internet_hours <=2:
  print("You spend little time on the internet.")
elif internet_hours >=3 and internet_hours <=6:
  print("You spend a moderate amount of time on the internet.")
elif internet_hours >=7 and internet_hours <=12:
  print("You spend much of the day on the internet.")
elif internet_hours >=13 and internet_hours <=24:
  print("You spend the majoirty of the day on the internet!")
elif internet_hours <0: 
  print("Invalid answer! Please provide a value from 0 up to 24.") 
elif internet_hours >=25: 
  print("Invalid answer! Please provide a value from 0 up to 24.")  

current_year = 2020

birth_year = int(input("Please enter your year of birth"))

age = current_year - birth_year

print("You are {} years old".format(age))

retirement_age = 65
if age >= retirement_age: 
 print("You have reached retirement age")


