from tkinter import *
import pyautogui

pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.moveTo(1000, 1000, duration=2, tween=pyautogui.easeInCirc)
pyautogui.moveTo(50, 50, duration=2, tween=pyautogui.easeInBounce)
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeOutElastic)

""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Ekran Çözünürlüğü
screenWidth, screenHeight = pyautogui.size()


print("Ekran çözünürlüğü : ", screenWidth, screenHeight)

# Fare Pozisyonu
currentMouseX, currentMouseY = pyautogui.position()
print("Fare Pozisyonu : ", currentMouseX, currentMouseY)

""""""""""""""""""""""""""""""""""""""""""""""""""""""

pyautogui.moveTo(799, 466, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.click()

for i in range(100):
    pyautogui.write("hello world", interval=0.001)
    pyautogui.press("enter")

""""""""""""""""""""""""""""""""""""""""""""""""""""""

# distance = 300
# while distance > 0 :
#     pyautogui.drag(distance, 0, duration=0.5)
#     distance -= 5
#     pyautogui.drag(0 ,distance, duration=0.5)
#     distance -= 5
#     pyautogui.drag(distance, 0, duration=0.5)
#     distance -= 5
#     pyautogui.drag(distance, 0, duration=0.5)
#     distance -= 5

""""""""""""""""""""""""""""""""""""""""""""""""""""""

window = Tk()

window.title("merhaba")
lbl = Label(window, text="Hi!")
lb2 = Label(window, text="Hi!", font=("Arial Bold", 90))

lbl.grid(column=0, row=0)
lb2.grid(column=1, row=0)

window.geometry("500x400")

button = Button(window, text="click")
button.grid(column=1, row=1)


window.mainloop()


def clicked():
    #lbl.configure(text="Clicked button")

    button2 = Button(window, text="colorful click",
                     bg="orange", fg="red", width=20, height=20)
    button2.grid(column=1, row=1)
