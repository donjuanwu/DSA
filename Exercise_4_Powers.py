"""
Date: 4/13/2021
Source: O'reilly
Presenter: Reuven Lerner
#Excercise: Powers of 10

Requirements:
1. Ask the user to enter a number.
2. Print the number in the formt I showed below, with the power of 10 * the digit

Example:
Enter a number: 1234
1000 * 1
100 * 2
10 * 3
1 * 4

Hints:
1. In Python, you can perform exponentiation with the "**" operator. So "3**2" = 9,
because that's 3 squared

2. You might need to do some calculations with "len" to get the exponent right.

"""

def main():
    print_power_10()

def print_power_10():
    print()
   
    while True:
        number = input("Enter an integer number: ")
        if (number == ""):
            break
        else:
            if not(number.isdigit):
                continue
            else:
                exp = len(number) -1
                for index in range(len(number)):
                    print(f"{10 ** exp} * {number[index]}")
                    exp -= 1


print("Exercise 4 - Print Power Of 10.")
if __name__ == "__main__":
    main()

