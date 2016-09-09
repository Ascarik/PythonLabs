import sys


def getTax(income, status):
    FIRST_PERCENT = 0.10
    SECOND_PERCENT = 0.15
    THIRD_PERCENT = 0.25
    FOURTH_PERCENT = 0.28
    FIFTH_PERCENT = 0.33
    SIXTH_PERCENT = 0.35

    MONEY = [
        [8350, 33950, 82250, 171550, 372950],
        [16700, 67900, 137050, 208850, 372950],
        [8350, 33950, 68525, 104425, 186475],
        [11950, 45500, 117450, 190200, 372950]
    ]

    if income <= MONEY[status][0]:
        tax = income * FIRST_PERCENT
    elif income <= MONEY[status][1]:
        tax = MONEY[status][0] * FIRST_PERCENT + (income - MONEY[status][0]) * SECOND_PERCENT
    elif income <= MONEY[status][2]:
        tax = MONEY[status][0] * FIRST_PERCENT + (MONEY[status][1] - MONEY[status][0]) * SECOND_PERCENT + \
        (income - MONEY[status][1]) * THIRD_PERCENT
    elif income <= MONEY[status][3]:
        tax = MONEY[status][0] * FIRST_PERCENT + (MONEY[status][1] - MONEY[status][0]) * SECOND_PERCENT + \
        (MONEY[status][2] - MONEY[status][1]) * THIRD_PERCENT + (income - MONEY[status][2]) * FOURTH_PERCENT
    elif income <= MONEY[status][4]:
        tax = MONEY[status][0] * FIRST_PERCENT + (MONEY[status][1] - MONEY[status][0]) * SECOND_PERCENT + \
        (MONEY[status][2] - MONEY[status][1]) * THIRD_PERCENT + (MONEY[status][3] - MONEY[status][2]) * FOURTH_PERCENT + \
        (income - MONEY[status][3]) * FIFTH_PERCENT
    else:
        tax = MONEY[status][0] * FIRST_PERCENT + (MONEY[status][1] - MONEY[status][0]) * SECOND_PERCENT + \
        (MONEY[status][2] - MONEY[status][1]) * THIRD_PERCENT + (MONEY[status][3] - MONEY[status][2]) * FOURTH_PERCENT + \
        (MONEY[status][4] - MONEY[status][3]) * FIFTH_PERCENT + (income - MONEY[status][4]) * SIXTH_PERCENT

    return tax


status = eval(input("(0-single filer, 1-married jointly,\n" +
                    "2-married separately, 3-head of household)\n" +
                    "Enter the filing status: "))

income = eval(input("Enter the taxable income: "))

tax = 0

if status == 0:
    tax = getTax(income, status)

elif status == 1:  # Compute tax for married file jointly
    tax = getTax(income, status)
elif status == 2:  # Compute tax for married separately
    tax = getTax(income, status)
elif status == 3:  # Compute tax for head of household
    tax = getTax(income, status)
else:
    print("Error: invalid status")
    sys.exit()

# Display the result
print("Tax is", format(tax, ".2f"))
