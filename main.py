from tkinter import *
from tkinter import ttk
import time
import random
import difflib


class MainWindow:

    def __init__(self, root):
        self.text = ["The first rule of Fight Club is: you do not talk about Fight Club. The second rule of Fight Club is: you DO NOT talk about Fight Club.",
                     "When you play the game of thrones, you win or you die. There is no middle ground.",
                     "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
                     "If life were predictable it would cease to be life, and be without flavor.",
                     "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough.",
                     "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success.",
                     "Life is what happens when you're busy making other plans.",
                     "One day the people that don’t even believe in you will tell everyone how they met you.",
                     "The true meaning of life is to plant trees, under whose shade you do not expect to sit.",
                     "The quick brown fox jumps over the lazy dog."]
        self.speed = 0
        self.accuracy = 0
        self.time_start = 0
        self.time_end = 0
        root.title("MiniProject")
        root.minsize(600, 500)
        for row in range(5):
            root.grid_rowconfigure(row, weight=1)
        for col in range(3):
            root.grid_columnconfigure(col, weight=1)
        self.label_text = Label(
            root, text="WELCOME TO TYPING SPEED CALCULATOR", wraplength=500)
        self.label_text.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.user_text = Text(root)
        self.user_text.grid(column=0, row=1, columnspan=3, sticky="nsew")

        self.btn_start = Button(root, text="START/RESTART", command=self.start)
        self.btn_start.grid(column=0, row=2, columnspan=1, sticky="nsew")
        self.btn_stop = Button(root, text="STOP", command=self.stop)
        self.btn_stop.grid(column=1, row=2, columnspan=1, sticky="nsew")
        self.btn_newtext = Button(root, text="NEW TEXT", command=self.new_text)
        self.btn_newtext.grid(column=2, row=2, columnspan=1, sticky="nsew")

        self.label_speed = Label(
            root, text=f"Your typing speed is {self.speed} WPM")
        self.label_speed.grid(row=3, column=0, columnspan=3, sticky="nsew")

        self.label_accuracy = Label(
            root, text=f"Your typing accuracy is {self.speed} %")
        self.label_accuracy.grid(row=4, column=0, columnspan=3, sticky="nsew")

    def start(self):
        self.time_start = time.time()
    def stop(self):
        self.time_end = time.time()
        words = self.label_text.cget("text").split(' ')
        self.speed = round(len(words)/((self.time_end - self.time_start)/60))
        self.label_speed.config(
            text=f"Your typing Speed is {self.speed} WPM")
        self.accuracy = round(difflib.SequenceMatcher(None, self.label_text.cget(
            "text"), self.user_text.get("1.0", 'end-1c')).ratio()*100)
        self.label_accuracy.config(
            text=f"Your typing accuracy is {self.accuracy} %")
    def new_text(self):
        self.label_text.config(
            text=self.text[random.randint(0, len(self.text)-1)])
        self.user_text.delete('1.0', END)
def main():
    root = Tk()
    myapp = MainWindow(root)
    root.mainloop()
if __name__ == "__main__":
    main()