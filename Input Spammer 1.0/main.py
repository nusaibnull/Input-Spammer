from pynput.keyboard import Key, Controller
import time

import keyboard

Keyboard = Controller()

print("""
██╗███╗   ██╗██████╗ ██╗   ██╗████████╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██║████╗  ██║██╔══██╗██║   ██║╚══██╔══╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██║██╔██╗ ██║██████╔╝██║   ██║   ██║       ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║██║╚██╗██║██╔═══╝ ██║   ██║   ██║       ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██║██║ ╚████║██║     ╚██████╔╝   ██║       ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝    ╚═╝       ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝                                                                                                     
 """)
print("Enter Esc key to start spamming...\n---------------------------------\n")

while True:
    try:
        spamNum = input("How many messages do you want to send?: ")
        spamNum = int(spamNum)
        break
    except:
        print("Error: try again.. (Enter a Number)")

message = input("Enter the message to spam: ")

while True:
    if keyboard.is_pressed('!'):  # if key 'q' is pressed 
        for i in range(1, spamNum + 1):
            print(str(i) + " Messages Sent.")
            for letter in str(message):
                Keyboard.press(letter)
                Keyboard.release(letter)
            Keyboard.press(Key.enter)
            Keyboard.release(Key.enter)
            time.sleep(0.1)
        break
