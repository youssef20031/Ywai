from datetime import datetime
import time

# defining function


def q(ques,value):
    question = input(ques)
    while question.lower() != value:
            print("try again")
            while True:
                time.sleep(2)
                break
            question = input(ques)
    else:
        print("you guessed it!")



# start of the script
print("hello 😊 :)")
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
    mood = input("how are you today"  ":")
    break
if mood.lower() == "good":
    print("nice")
elif mood.lower() == "bad":
    print("i'am sorry")
elif mood.lower() == "not good":
    print("it is okay")
elif mood.lower() == "nice":
    print("very good")
elif mood.lower() == "fine":
    print("nice")
else:
    print("hmmmm, ok")
# beginning of second question

while True:
    time.sleep(2)
    hobby = input("what are your hobbies?"  ":")
    break
if hobby.lower() == "coding":
    print("good")
elif hobby.lower() == "sports":
    print("nice")
elif hobby.lower() == "nothing":
    print("do something")
elif hobby.lower() == "shouting":
    print("be calm")
else:
    print("ok")
while True:
    time.sleep(2)
    break

color = ("what is my favorite color?"  ":")
val = "blue"
q(color,val)
while True:
    time.sleep(2)
    break

lang = "what is my favorite coding language?"  ":"
val2 = "python"
q(lang,val2)
while True:
    time.sleep(2)
    break
# end of questions

while True:
    time.sleep(2)
    print("Thank you for using this python script 😀👍")
    break

while True:
    time.sleep(2)
    print("Created by Youssef Maged ❄")
    break

while True:
    time.sleep(2)
    print("Good bye ")
    break

while True:
    time.sleep(2)
    print("")
    break
# end of file
# finally! my 100 lines of code
# i am done
