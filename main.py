import time
timer = 2
pword = "043d7f320a5480",


for i in range(1000):
    print("----------------------------------------------")
    print("PLEASE PRESENT CARD:")
    PK = input()

    if PK == pword :
        print("ACCESS CONFIRMED")
        print("(Door opened for: " + str(timer) + " seconds)")
        time.sleep(timer)

    else:
        print("ACCESS DENIED")


