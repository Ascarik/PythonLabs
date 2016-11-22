import time

seconds = eval(input("Enter the number of seconds: "))

for i in range(seconds, 0, -1):
    time.sleep(1)
    if i > 1:
        print(i, "seconds remaining")
    else:
        print(i, "second remaining")
print("Stopped")
