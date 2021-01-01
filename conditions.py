is_hot_day = True
is_cold_day = False
if is_hot_day:
    print("It's a hot day")
elif is_cold_day:
    print("It's a cold day.")
    print("Wear warm cloths")
else:
    print("It's a lovely day")
print("Enjoy your day")

#### Exercise
actual_price = 1000000
is_buyer_credit_good = True
discount_percentage = 20

if is_buyer_credit_good:
    discount_percentage = 10

offer_price = actual_price - (actual_price * discount_percentage // 100)
print(f"Downpayment is: ${offer_price}")

has_good_credit = False
has_high_income = True
has_criminal_record = False

# Logical AND
if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# Logical OR

if has_high_income or has_good_credit:
    print("OR OPERATOR - Eligible for loan")
else:
    print("OR OPERATOR - Not eligible for loan")

# Logical NOT

if has_high_income and not has_criminal_record:
    print("NOT Operator - Eligible for Loan")

