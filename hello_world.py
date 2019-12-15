resualt = 20
def input_number(resualt):
    number = input('\tguess a number:')
    if (int(number) !=20) and (int(number)>resualt):
        print("\n guess number is bigger")
        return input_number(resualt)
    elif (int(number) !=20) and (int(number)<resualt):
        print("\n guess number is smaller")
        return input_number(resualt)
    else:
        print('\n great! you guess is right.')
input_number(resualt)


