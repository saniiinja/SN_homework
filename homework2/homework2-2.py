#fizzbuzz

user_number = int(input("Enter a number between 1 and 100: "))

for n in range(user_number + 1):
    if n % 3 == 0 and n % 5 == 0:
        print("fizzbuzz")
        continue
    elif n % 3 == 0:
        print("fizz")
        continue
    elif n % 5 == 0:
        print("buzz")
        continue
    print(n)