import random
from datetime import datetime
import time


# defining function


def q(ques, value, arr):
    arr = [arr.capitalize() for arr in arr]
    print(arr)
    question = input(ques)
    while question.lower() != value:
        print("Try again")
        while True:
            time.sleep(2)
            break
        question = input(ques)
    else:
        print("You guessed it!")


# start of the script
print("hello 😊 :)")
while True:
    time.sleep(2)
    break

now = datetime.now()

print("It is:" + " " + str(now.day) + ":" +
      str(now.month) + ":" + str(now.year))

while True:
    time.sleep(2)
    break
name1 = input("What's your name" ":")

while True:
    time.sleep(2)
    print("Hi", name1, "😉")
    break
# beginning of first question

while True:
    time.sleep(2)
    mood = input("How are you today"  ":")
    break
if mood.lower() == "good":
    print("Nice")
elif mood.lower() == "bad":
    print("I am sorry")
elif mood.lower() == "not good":
    print("It is okay")
elif mood.lower() == "nice":
    print("Very good")
elif mood.lower() == "fine":
    print("Nice")
else:
    print("Hmm, ok")
# beginning of second question

while True:
    time.sleep(2)
    hobby = input("what is your hobby?"  ":")
    break
if hobby.lower() == "coding":
    print("Good")
elif hobby.lower() == "sports":
    print("Nice")
elif hobby.lower() == "nothing":
    print("Do something")
elif hobby.lower() == "shouting":
    print("Be calm")
else:
    print("Ok")
while True:
    time.sleep(2)
    break

color = "What is my favorite color in the list above?"  ":"
val = ["blue", "green", "red", "yellow", "white", "pink", "purple"]
val_arr = random.choice(val)
q(color, val_arr, val)
while True:
    time.sleep(2)
    break

lang = "What is my favorite coding language from the list above?"  ":"
val2 = ["python", "ruby", "rust", "c#", "c++", "c", "f", "sql", "matlab"]
val2_arr = random.choice(val2)
q(lang, val2_arr, val2)
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
