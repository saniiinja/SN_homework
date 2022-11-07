#unit converter

print("Hello there!\n\n" +
    "This is a small and very specific unit conversion program.\n" +
    "Having a problem with understanding miles? This program will help you with that!\n")

check = "Y"

while check.upper() == "Y":

    kilometers = float(input("Enter the number of kilometers: "))

    #conversion factor
    cf = 0.621371

    miles = kilometers * cf

    # '%0.2f' - number of decimal places you want to include
    print("%0.2f kilometer(s) is equal to %0.2f miles." % (kilometers,miles))

    check = input("Do you want to try again? Enter y/n: ")

    if check.upper() != "Y":
        check = input("Are you sure? Enter y/n: ")
        if check.upper() == "Y":
            break
        else:
            check = "Y"

print("\nGoodbye.")
