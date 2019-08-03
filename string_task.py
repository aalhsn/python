print ("Mad libs where libs get Mad")
num=input("Enter a number between 1 and 12:   ")
noun=input("Enter a noun:   ")
name=input("What is you name:  ")
sent=input("Enter a random sentence :   ")
vrb=input("Enter a verb:  ")

print(""" MAD LIBS BEGIN!!

    It was {} o'clock when I heard a knock at the door.
    I opened the door and there was a box full of {}s with a note saying "From Mr. {}".
    Just as I closed the door I heard a scream "{}".
    I froze in place and all I could do was {}.""".format(num,noun,name,sent.upper(),vrb))

