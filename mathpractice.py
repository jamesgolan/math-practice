import random
import time


def main():
    name = input("Please type your name: ")
    print("Hello " + name + ", Welcome to Jam's math tutor!")

    time.sleep(2)





    num_problems = ""
    while not num_problems.isnumeric():
        num_problems = input("Please enter the number of practice problems you would like to do out of 10: ")

    answer = ""
    while answer not in ["A", "S", "M", "D"]:
        answer = input("What type of math problem would you like to practice today?"
    "[M] for Multiplication, [A] for Addition, [S] for Subtraction`")

    temp_dict = {
        "A": "addition",
        "S": "subtraction",
        "M": "multiplication",
    #        "D": "Division"
    }

    def practice_math(num_problems, answer):
        result = 0
        for _ in range(num_problems):
            if "addition" in answer:
                result += addfunction(random.randrange(1, 10), random.randrange(1, 10))

            elif answer == "multiplication":
                result += multfunction(random.randrange(1, 10), random.randrange(1, 10))

            elif answer == "subtraction":
                result += subfunction(random.randrange(1, 10), random.randrange(1, 10))

    #            elif answer == "division":
    #                result += divfunction(random.randrange(1, 10), random.randrange(1, 10))
        print("You got " + str(result) + " out of " + str(num_problems) + " correct")

    practice_math(int(num_problems), temp_dict[answer])

    def addfunction(a,b):
        print(str(a) + "+" + str(b))
        x = input()
        while not x.isnumeric():
            x = input("Try again: ")
        if int(x) == a + b:
            print("Correct!")
            return 1
        else:
            print("Incorrect")
            return 0

    def subfunction(a,b):
        print(str(a) + "-" + str(b))
        x = input()
        while not x.isnumeric():
            x = input("Try again: ")
        if int(x) == a - b:
            print("Correct!")
            return 1
        else:
            print("Incorrect")
            return 0

    def multfunction(a,b):
        print(str(a) + "*" + str(b))
        x = input()
        while not x.isnumeric():
            x = input("Try again: ")
        if int(x) == a * b:
            print("Correct!")
            return 1
        else:
            print("Incorrect")
            return 0
    
if __name__ == "__main__":
    main()


#def practice_math(num_problems, answer):
    #   result = 0 
    #  for _ in range(num_problems)





