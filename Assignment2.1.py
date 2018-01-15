while True:
    try:
        sequence = input("Enter Sequence as comma-separated numbers: ")
        my_list = list(map(int, sequence.split(',')))
        print (my_list)
    except ValueError:
        print("You've given an invalid input")
        continue
    else:
        break
