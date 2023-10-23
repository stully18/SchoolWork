base_amount = float(input('What is the base amount? '))
interest_rate = float(input('What is the interest rate percentage? ')) / 100
year = int(input('How many years is this investment? '))
count = 0
total_investment = base_amount
for i in range(1, year + 1):
    total_investment = total_investment * (1 + interest_rate)
    count += 1
    print(f'Year {count}: {total_investment:.2f}')