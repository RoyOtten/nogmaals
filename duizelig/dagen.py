day = input ("name a day ") 
if day ==("monday"):
    last_day = 1 
elif day ==("tuesday"):
    last_day = 2
elif day ==("wednesday"):
    last_day = 3
elif day ==("thursday"):
    last_day = 4
elif day == ("friday"):
    last_day = 5
elif day == ("saturday"):
    last_day = 6
elif day == ("sunday"):
    last_day = 7

while last_day <= day:
    if last_day == 1:
        print ('monday')
    elif last_day == 2:
        print('tuesday')
    elif last_day == 3:
        print('wednesday')
    elif last_day == 4:
        print('thursday')
    elif last_day == 5:
        print ('friday')
    elif last_day == 6:
        print ('saturday')
    elif last_day == 7:
        print ("sunday")
    last_day = last_day - 1