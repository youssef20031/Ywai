from datetime import datetime
import time

# defining function


def q1():
    color = input("what is my favorite color?"  ":")
    while q1 != "color":
        print
        if color != "blue":
            print("try again")
            while True:
                time.sleep(2)
                break
            color = input("what is my favorite color?"  ":")
        else:
            print("you guessed it!")
            break


def q2():
    lang = input("what is my favorite coding language?"  ":")
    while q2 != "name4":
        print
        if lang != "python":
            print("try again")
            while True:
                time.sleep(2)
                break
            lang = input("what is my favorite coding language?"  ":")
        else:
            print("you guessed it!")
            break


# start of the script
print("hello")
while True:
    time.sleep(2)
    break

now = datetime.now()

print("it is:" + " " + str(now.day) + ":" +
      str(now.month) + ":" + str(now.year))


while True:
    time.sleep(2)
    break
name1 = input("what's your name" ":")

while True:
    time.sleep(2)
    print("hi", name1, "😉")
    break
# beginning of first question

while True:
    time.sleep(2)
    name2 = input("how are you"  ":")
    break
if name2 == "good":
    print("nice")
elif name2 == "bad":
    print("i'am sorry")
elif name2 == "not good":
    print("it is okay")
elif name2 == "nice":
    print("very good")
elif name2 == "fine":
    print("nice")
else:
    print("hmmm, ok")
# beginning of second question

while True:
    time.sleep(2)
    name3 = input("what are your hobbies?"  ":")
    break
if name3 == "coding":
    print("good")
elif name3 == "sports":
    print("nice")
elif name3 == "nothing":
    print("do something")
elif name3 == "shouting":
    print("be calm")
else:
    print("ok")
while True:
    time.sleep(2)
    break
q1()
while True:
    time.sleep(2)
    break
q2()
# end of questions

while True:
    time.sleep(2)
    print("Thank you for using this python script")
    break

while True:
    time.sleep(2)
    print("Created by Youssef Maged")
    break

while True:
    time.sleep(2)
    print("Good bye")
    break

while True:
    time.sleep(2)
    print("")
    break
# end of file
# finally! my 100 lines of code
# i am done
