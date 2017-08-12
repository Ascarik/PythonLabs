from Ch06.Lab29 import isValid

if __name__ == '__main__':
    num1 = "4388576018402626"
    if num1.isdigit():
        print("Card number1 " + num1 + " is", end=" ")
        print(isValid(int(num1)))

    num2 = "4388576018410707"
    if num2.isdigit():
        print("Card number2 " + num2 + " is", end=" ")
        print(isValid(int(num2)))
