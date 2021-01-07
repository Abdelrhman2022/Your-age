import datetime
BirthYear = int(input('Enter your birthyear : '))
BirthMonth = int(input('Enter your birthMonth : '))
BirthDay = int(input('Enter your birthDay : '))

BirthYear = (BirthYear - 1) * 12 * 30
BirthMonth = (BirthMonth - 1) * 30
Birth = BirthYear + BirthMonth + BirthDay
curYear = (datetime.datetime.now().year - 1) * 12 * 30
curMonth = (datetime.datetime.now().month - 1) * 30
curDay = datetime.datetime.now().day
date = curYear + curMonth + curDay
age = date - Birth
if(age > (18 * 360)):
    year = age // 360
    month = age % 360 // 30
    day = age % 360 % 30
    print("Your Year is {} and Your Month {} and Your days are {}".format(year, month, day))
else:
    print("Sorry , your age not allowed")