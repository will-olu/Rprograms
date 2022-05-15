counter = 1

while(counter <= 3):
    principal = int(input("Enter the principal amount"))
    numberofyears = int(input("Enter the number of years:"))
    rateofinterest = float(input("ENter the rate of interest:"))
    simpleinterest = principal * numberofyears * rateofinterest/100
    print("Simple interest = %2f" %simpleinterest)
    #increase the counter by 1
    count = counter + 1
    print("Calculating simple interest 3 times.")
    break

