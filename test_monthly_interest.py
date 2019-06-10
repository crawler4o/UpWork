# Initial loan
loan_input = float(input("Initial loan = "))

# Monthly interest rate
monthly_interest_rate = float(input("monthly interest rate in % = "))

# monthly payment
monthly_payment = float(input("monthly payment = "))
n = 0

# Calculate result

print("Remaining loan:")
while loan_input > 0:

	n = n + 1
	if monthly_payment > loan_input * (1 + monthly_interest_rate/100):

		loan_input = 0
		print("Month",n,":",loan_input)
	else:
		loan_input = loan_input * ( 1 + monthly_interest_rate/100)

		loan_input = loan_input - monthly_payment
		print("Month",n,":",loan_input)