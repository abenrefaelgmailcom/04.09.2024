# קלוט מהמשתמש ציון מבחן ) int )והדפס פידבק באופן הבא:
grade: int = int(input('students grade:'))

if grade <= 100 and grade > 96:
    print("excellent!!! You're a Star!")
elif grade <= 95 and grade > 81:
    print("!awesome")
elif grade <= 80 and grade > 61:
    print("good pretty")
elif grade <= 60 and grade > 41:
    print("you're getting there, need some more work")
elif grade <= 40 and grade > 0:
    print("try harder next time...")
else: print("grade illegal")