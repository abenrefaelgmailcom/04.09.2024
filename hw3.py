volume: int = int(input('volume:'))

match volume:
    case 0:
        print("mute")
    case 1:
        print("very quiet")
    case 2:
        print("very quiet")
    case 3:
        print("quiet")
    case 4:
        print("moderately quiet")
    case 5:
        print("medium")
    case 6:
        print("moderately loud")
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9:
        print("extremely loud")
    case 10:
        print("extremely loud")
    case _:
        print("Invalid volume.");
