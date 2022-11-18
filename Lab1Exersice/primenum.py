# if prime number and even number

def check_print(method_oeb):
    if method_oeb == 'o' or method_oeb == 'O':
        return 0
    elif method_oeb == 'e' or method_oeb == 'E':
        return 1
    elif method_oeb == 'b' or method_oeb == 'B':
        return 2
    else:
        print('wrong input')
        exit(0)

def show_Prime(primeValue):
    if primeValue == 'y' or primeValue == 'Y':
        return False
    elif primeValue == 'n' or primeValue == 'N':
        return True
    else:
        print('wrong input')
        exit(0)

def isPrime_even_odd(num, check, show):
    cnt = num-1
    fil = False
    if check == 2:
        fil = True
    elif check == 1:
        if num % 2 == 0:
            fil = True
    elif check == 0:
        if num % 2 != 0:
            fil = True

    while cnt > 0:
        if num % cnt == 0 and cnt != 1:
            if fil and show:
                print(f'{num}: Not prime divide by {cnt}')
            break
        elif cnt == 1:
            if fil:
                print(f'{num}: Prime')
            break
        cnt -= 1
    if cnt == 0 and fil:
        print('1: Prime')
    if cnt > 0:
        isPrime_even_odd(num-1, check, show)


def main():
    cnt = max_value
    isPrime_even_odd(cnt, check_print(method_oeb), show_Prime(primeValue))


if __name__ == "__main__":
    max_value = int(input("Enter max value : "))
    method_oeb = str(input("Enter O/E/B (Odd or Even or Both) : "))
    primeValue = str(input("Enter Y/N (OnlyPrime?) : "))
    main()