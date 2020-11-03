def line(tam=48):
    return '-' * tam


def title(msg):
    print(line())
    print(f'{msg}'.center(48))
    print(line())


def read_option(msg, a, b):
    error = '\033[31m ERROR! Type in a valid option!\033[m'
    while True:
        try:
            v = int(input(msg))
        except (TypeError, ValueError):
            print(error)
            continue
        except KeyboardInterrupt:
            print('\033[31;1mData input interrupted by the user\033[m')
            exit()
        else:
            if a <= v < b:
                return v
            else:
                print(error)


def menu(array):
    title('MAIN MENU')
    c = 1
    for item in array:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    return read_option('\033[32m Your option: \033[m', 1, len(array) + 1)
