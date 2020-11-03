def read_int(prompt):
    error = '\033[31m ERROR! Type in a valid option!\033[m'
    while True:
        try:
            v = int(input(prompt))
        except (TypeError, ValueError):
            print(error)
            continue
        except KeyboardInterrupt:
            print('\033[31;1mData input interrupted by the user\033[m')
            exit()
        else:
            return v
