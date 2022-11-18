# exercise 1
for x in range(5):
    print(" " * (5 - x), "*" * (2 * x + 1))
for x in range(5 - 2, -1, -1):
    print(" " * (5 - x), "*" * (2 * x + 1))
print("")

# exercise 2
def drawDiamond(h):
    for x in range(h):
        print(" " * (h - x), "*" * (2 * x + 1))
    for x in range(h - 2, -1, -1):
        print(" " * (h - x), "*" * (2 * x + 1))

try :
    h = eval(input("Enter diamond's height: "))
    if h < 2 :
        print('Wrong input. (must more than 2).')
        exit(0)
    else :
        drawDiamond(h)
except Exception as err:
    print(f'error : {err}')