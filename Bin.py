import os

def options():
    ops = ["op1: Normal", "op2: Repair"]

    showops = input(ops)

    if showops == "op1":
        os.system("python3 Op1.py")

    elif showops == "op2":
        os.system("python3 Op2.py")

    else:
        print("Oops! Try Again")
    

options()
