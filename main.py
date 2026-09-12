import pyttsx3
import random
engine = pyttsx3.init()
smile = "😀😁😂🤣😃😄😎😋😊😉😆😅😍😘🥰😗😙🥲🤔🤩🤗🙂☺️😚🫡🤨😐😑😶🫥😮😥😣😏🙄😶‍🌫️🤐😯😪😫🥱😴🤤😝😜😛😌🫩"
m = random.choice(smile)
# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"
rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)                        # printing current voice rate
engine.setProperty('rate', 230) 
engine.say(m)
engine.runAndWait()
a = input()
if m == a:
    print('Вы победили')
else:
    print('Упс... В следующий раз возможно получится')