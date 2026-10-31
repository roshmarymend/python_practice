try:
    units = int(input("Enter the units consumed: "))

    if units < 0:
        raise ValueError("Units cannot be negative")

except ValueError as e:
    print("Invalid input:", e)

else:
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    else:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4

    print("Electricity Bill = Rs.", bill)

finally:
    print("Electricity bill calculation completed.")