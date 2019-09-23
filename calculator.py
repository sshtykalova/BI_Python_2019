a = int(input())
action = input()
b = int(input())
if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "*":
    print(a * b)
elif action == "/":
    if b != 0:
        print(a / b)
    else:
        print("Zero division!")
elif action == "//":
    if b != 0:
        print(a // b)
    else:
        print("Zero division!")
elif action == "^":
    print(a ** b)
else:
    print("I don\'t know this command :(")
