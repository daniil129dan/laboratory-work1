days = ["31", "28(в високосном)", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
month = ["январе", "феврале", "марте", "апреле", "мае", "июне", "июле", "августе", "сентябре", "октябре", "ноябре", "декабре"]
print("1.Январь\n2.Февраль\n3.Март\n4.Апрель\n5.Май\n6.Июнь\n7.Июль\n8.Август\n9.Сентябрь\n10.Октябрь\n11.Ноябрь\n12.Декабрь\nВыберите номер месяца.")
a = int(input())
if(a < 1):
    a = 1
if(a > 12):
    a = 12
print("В", month[a-1], days[a-1], "день" )
