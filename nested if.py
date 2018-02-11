#nested_if_statements
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
#output= if entered number 10, output is "positive number"
    #if entered number 0, output is 0
    #if entered number -10, output is "negative number"
