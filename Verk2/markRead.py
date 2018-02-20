import pyautogui as auto
from time import sleep
mails = int(input("Number of emails\n"))

for x in range((mails // 50)+((mails % 50) != 0)):
    auto.click(310, 185)
    auto.click(310, 230)
    auto.click(957, 185)
    auto.click(957, 230)
    sleep(1)


'''import tkinter as tk
def keypress(event):
    if event.keysym == 'Escape':
        root.destroy()
    x = event.char
    print(x)
root = tk.Tk()
print("Press a key (Escape key to exit):")
root.bind_all('<Key>', keypress)
# don't show the tk window
root.withdraw()
root.mainloop()'''