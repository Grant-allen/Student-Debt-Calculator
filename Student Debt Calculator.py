#PART A, information collection
#In this part of the code we are setting up all the lists we will need for data collection from the user.
#This includes the student type, student loan and interest rates for each year.
#Addtionally, we set lists of loan limits corresponding for the year of school the student is in
#We assumed that a student would not go over 16 years of college so there are 16 max loan amounts for each year according to student type.
#Years is set to zero, which in our case is year 1 of college
typeStud_list = []
loan_list = []
subRate_list = []
unsubRate_list = []
years = 0
subLoanLimit =[3500, 4500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500,5500,5500]
indepLoanLimit = [9500, 10500, 12500, 12500, 12500, 12500, 12500, 12500, 12500, 12500, 12500,12500,12500,12500,12500]
depLoanLimit = [5500, 6500, 7500, 7500, 7500, 7500, 7500, 7500, 7500, 7500, 7500, 7500,7500,7500,7500]
debtDict ={'<7500':10,'7500-10000':12,'10000-20000':15,'20000-40000':20,'40000-60000':25,'>60000':30}
anotherYear = 'Y'
#Creating a custom error so we can display a unique error message when an loan over a limit is entered
class CustomError(Exception):
    pass
#This loop is in range(30) solely for the purpose of running the loop enough times to collect enough user input
#As you can see later, once a user inputs that they are not attending school for another year, the loop breaks
while anotherYear = 'Y':
    #Collecting if the student is Inpependent status or dependent status for a school year, an error is shown if I or D is not entered
    #If entered correctly the student type list is appended
    while True:
        try:
            typeStud = input("Enter I for Independent or D for Dependent student for this school year: ")
            if typeStud not in ['I', 'D']:
                raise ValueError("Invalid input, input 'I' or 'D'.")
            else:
                typeStud_list.append(typeStud)
            break
        except ValueError as e:
            print(e)
    #Collecting the loan amount for each year, an error is displayed if the input isn't numeric
    #If an acceptable value is inputed then the loan list is appended
    while True:
        try:
            loan = input("What is the total loan amount for this school year: ")
            if not loan.isnumeric():
                raise TypeError("Invalid input, please enter a positive, whole number.")
            #Here an error is displayed if the specified loan is over the limit for the student's status and year in college
            elif typeStud == "I" and indepLoanLimit[year] < int(loan): 
                raise CustomError("Invalid input, this loan is over the limit for this year in school.")
            elif typeStud == "D" and depLoanLimit[year] < int(loan):
                raise CustomError("Invalid input, this loan is over the limit for this year in school.")
            else:
                loan_list.append(int(loan))
            break
        except TypeError as ee:
            print(ee)
        except CustomError as x:
            print(x)
    #Collecting the users subsidized interest rate, an error is displayed if anything other than a number is entered
    #If an acceptable value is inputed then the sub. interest rate list is appended
    while True:
        try:
            subRate = input("What is the subsidized loan interest rate: ")
            if not subRate.isnumeric():
                raise TypeError("Invalid input, please enter a positive, whole number.")
            else:
                subRate_list.append(float(subRate))
            break
        except TypeError as eee:
            print(eee)
    #Collecting the user's unsubsidixed interest rate, an error is displayed if anything other than a number is entered
    #If an acceptable value is inputed then the unsub. loan list is appended
    while True:
        try:
            unsubRate = input("What is the unsubsidized loan interest rate: ")
            if not unsubRate.isnumeric():
                raise TypeError("Invalid input, please enter a positive, whole number.")
            else:
                unsubRate_list.append(float(unsubRate)) 
            break
        except TypeError as eeee:
            print(eeee)
    #Asking the user if they are attending school again, if Y then the loop restarts, if N the program moves to part B
    while True:
        try:
            anotherYear = input("Are you attending another year of undergraduate college Y or N: ")
            if anotherYear not in ['Y', 'N']:
                raise ValueError("Invalid input, enter 'Y' or 'N'.")
            break
        except ValueError as eeeee:
            print(eeeee)
    #keeping track of years in college for later calculations
    years += 1

#PART B, Cost 6 months after leaving college
totalCost_sixMonths = 0
for i in range(0, years):
    #calculating cost for the first year (0) of college, if the loan amount for first year is under the subsidized limit it is simply added
    # if the loan amount is over the subsidized limit then the loan interest is added for each day of the year
    # 90 days is added to account for the extra 6 months we are calculating for
    if i == 0:
        if loan_list[i] <= subLoanLimit[i]:
            totalCost_sixMonths += (loan_list[i])
        else:
            totalCost_sixMonths += subLoanLimit[i]
            totalCost_sixMonths += (loan_list[i] - subLoanLimit[i]) * (1 + (unsubRate_list[i]/100)/365) ** ((years * 365) + 90)
    #calculating cost for the second year (1) of college, if the loan amount for second year is under the subsidized limit it is simply added
    # if the loan amount is over the subsidized limit then the loan interest is added for each day of the year
    # 90 days is added to account for the extra 6 months we are calculating for
    elif i == 1:
        if loan_list[i] <= subLoanLimit[i]:
            totalCost_sixMonths += (loan_list[i])
        else:
            totalCost_sixMonths += subLoanLimit[i]
            totalCost_sixMonths += (loan_list[i] - subLoanLimit[i]) * (1 + (unsubRate_list[i]/100)/365) ** (((years - int(i)) * 365) + 90)
    #calculating cost for all other years past the second year, if the loan amount this year is under the subsidized limit it is simply added
    # if the loan amount is over the subsidized limit then the loan interest is added for each day of the year
    # 90 days is added to account for the extra 6 months we are calculating for
    else:
        if loan_list[i] <= subLoanLimit[i]:
            totalCost_sixMonths += (loan_list[i])
        else:
            totalCost_sixMonths += subLoanLimit[i]
            totalCost_sixMonths += (loan_list[i] - subLoanLimit[i]) * (1 + (unsubRate_list[i]/100)/365) ** (((years - int(i)) * 365) + 90)


#PART C, determining loan factors

#calculating colsolidated interest rate, a weighted average calculation of all loans and their respective interest rates
#setting a variable for the products of numerator calculatotions
numerator = 0
#looping through each year of loans
for i in range(0, years):
    #determining if the student is within the max subsidized loan for the specific year in school
    if loan_list[i] >= subLoanLimit[i]:
        #determining the total unsubidized loan and multipling by its corresponding rate
        numerator += (loan_list[i] - subLoanLimit[i]) * unsubRate_list[i]
        #adding in the subzided loan and rate
        numerator += subLoanLimit[i] * subRate_list[i]
    else:
        #if the loan is not over the subsidized limit then we just apply the subsized interest rate
        numerator += loan_list[i] * subRate_list[i]
#calculating the total debt which will be our denominator
loanTotal = sum(loan_list)
#performing the calculation and rounding to the nearest 1/8th percent
consolidatedIR = round(numerator / loanTotal,2)

#using the debtDict to determine the amount of years the user has to pay off their loan based on total borrowed
#here we use loanTotal from our earlier calculators to compare to our debt dictionary
if loanTotal < 7500:
    payoffYears = debtDict['<7500']
elif loanTotal in range(7500,10000):
    payoffYears = debtDict['7500-10000']
elif loanTotal in range(10000,20000):
    payoffYears = debtDict['10000-20000']
elif loanTotal in range(20000,40000):
    payoffYears = debtDict['20000-40000']
elif loanTotal in range(40000,60000):
    payoffYears = debtDict['40000-60000']
else:
    payoffYears = debtDict['>60000']

#Calculating monthly payment, for this we used Numpy Financial which is a tool to financial make calculations easier
#this is also converted to currency format
import numpy_financial as npf
monthlyPayment = abs(npf.pmt((consolidatedIR/100)/12, 12*int(payoffYears), totalCost_sixMonths))

#Calculating the total paid loans plus interest
grandTotalPaid = monthlyPayment * payoffYears * 12

#Calcultating total interest paid
totalIRPaid = grandTotalPaid - totalCost_sixMonths

#printing all results with blank lines added, values needed to be in currency format are formatted as such
print("\n\n")
print("Total owed after six months of leaving college is $", '${:,.2f}'.format(totalCost_sixMonths), "\n")
print("Consolidated interest rate is: " , consolidatedIR, "%")
print("Monthly payment after consolidation: ", '${:,.2f}'.format(monthlyPayment))
print("Loan payments continue for this many years:", payoffYears)
print("Total interest paid on school loans: ", '${:,.2f}'.format(totalIRPaid))
print("Total paid loans plus interest: ", '${:,.2f}'.format(grandTotalPaid))

#displaying results in the text file results.txt 
with open("results.txt", 'w') as f:
    f.write("Total owed six months after leaving college is: "  + str('${:,.2f}'.format(totalCost_sixMonths)) + '\n')
    f.write("Consolidated interest rate is: " + str(consolidatedIR) + "%\n" )
    f.write("Monthly paynment after consolidation: " + str('${:,.2f}'.format(monthlyPayment)) + '\n')
    f.write("Loan payments continue for this many years: " + str(payoffYears) + '\n')
    f.write("Total interest paid on school loans: " + str('${:,.2f}'.format(totalIRPaid)) + '\n')
    f.write("Total paid loans plus interest: " + str('${:,.2f}'.format(grandTotalPaid)) + '\n')
