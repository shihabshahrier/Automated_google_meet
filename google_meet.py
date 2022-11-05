import webbrowser
import time
import pyautogui
import schedule
import tkinter as tk


def main():
    def FuckOnlineClass():
        webbrowser.open_new_tab("https://meet.google.com/xkm-jyuk-six?pli=1&authuser=2")

        time.sleep(5)
        pyautogui.hotkey('ctrl', 'd')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'e')
        time.sleep(2)
        for i in range(8):
            pyautogui.hotkey('tab')
            time.sleep(1)
        time.sleep(2)
        pyautogui.hotkey('enter')

    schedule.every().day.at("18:46").do(FuckOnlineClass)

    while True:
        schedule.run_pending()
        time.sleep(1)

def uI():
    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=300, height=300)
    canvas1.pack()


    def click():
        main()

    button1 = tk.Button(text='Click Me', command=click, bg='brown', fg='white')
    canvas1.create_window(150, 150, window=button1)

    root.mainloop()

uI()

#button = driver. find_element_by_id('idofbutton')
#button. click()
