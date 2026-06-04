math = int(input("enter the marks: "))
physics = int(input("enter the subject marks: "))
chemestry = int(input("enter the subject marks: "))
computer = int(input("enter the subject marks: "))
english = int(input("enter the subject marks: "))
total = math + physics + chemestry + computer + english
percentage = total / 500 * 100
print ("The total marks is: ", total) 
print("The percentage is:", percentage, "%")

paisa = int(input("Enter the amount of paisa you want to convert: "))
rupees = paisa / 100 
print(rupees)

dollarRupees = int(input("enter the amount of rupees: "))
dollar = dollarRupees /150 
print("$" + str(dollar))

principle = int(input("Enter the principal: "))
time = int(input("Enter the amount of time: "))
rate = int(input("Enter the rate: "))
simpleIntrest = ((principle*time*rate)/100)
print("The Simple Intrest is: " + str(simpleIntrest))