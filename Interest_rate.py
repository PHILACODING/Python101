# Collect the necessary data input ( principal, a_i_r, years)
# Calculate the monthly payment
# Show to the user 

def main ():
    print('This is a monthly payment loan calculator ')
    print("")

    principal = float(input("Inter the loan amount: "))
    a_i_r = float(input("Enter the annual interest rate: "))
    years = int(input( "Enter the number of years : "))

    monthly_interest_rate = a_i_r / 1200
    no_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / ( 1- ( 1+ monthly_interest_rate) **(-no_of_months))

    print( f"Monthly payment is {monthly_payment}")

main()


