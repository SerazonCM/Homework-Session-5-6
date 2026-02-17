try: # what we learned in session 5 n 6
    gross = float(input("Enter gross salary: "))
    children = int(input("Enter number of children: "))

# find the base tax rate on income
    if gross < 1000:
        tax = 0.10
    elif gross < 2000:
        tax = 0.12
    elif gross < 4000:
        tax = 0.14
    else:
        tax = 0.18

# find the child tax rate reduction
    if gross < 2000:
        tax -= children * 0.01
    else:
        tax -= children * 0.005

    if tax < 0:
        tax = 0

    net = gross * (1 - tax)
    print("Net salary:", net)

except:
    print("Invalid input, write you salary with digits ex. 3500")