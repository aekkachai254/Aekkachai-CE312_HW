def summation(step):
    if step < 2:
        return 1
    else:
        sum = 1 / step + (summation(step - 1))
        print(f'Limit = {step} Value = {sum}')
        return sum

def main():
    step = int(input('Harmonic step : '))
    print('Limit = 1 Value = 1')
    print(summation(step))

if __name__ == "__main__":
    main()