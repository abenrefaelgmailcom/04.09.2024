grade: int = int(input('grade:'))

match grade:
    case grade if grade <= 100 and grade > 96:
        print("excellent!!! You're a Star!")
    case grade if grade <= 95 and grade > 81:
        print("!awesome")
    case grade if grade <= 80 and grade > 61:
        print("good pretty")
    case grade if grade <= 60 and grade > 41:
        print("you're getting there, need some more work")
    case grade if grade <= 40 and grade > 0:
        print("try harder next time...")
    case _:
        print("Invalid grade.");
