year = int(input())
if year % 400 == 0:
    print("Високосный")

elif year % 100 == 0:
    print("Не високосный")

elif year % 4 == 0:
    print("Високосный")

else:
    print("Не високосный")
