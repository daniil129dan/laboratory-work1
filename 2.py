dog = float(input())
if(dog < 0):
    print("слишком молодой")
else:
    if(dog >= 2):
        olddog = (dog - 2) * 4 + 10.5 * 2
    else:
        olddog = dog * 10.5
    print(olddog)
