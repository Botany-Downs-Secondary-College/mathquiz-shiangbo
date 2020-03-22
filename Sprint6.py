#MathQuiz programme uses GUi with classes, generates questions, responds to user answers and gives a report
#Sprint6.py
#S.Chang March 2020

from tkinter import *
from random import *

class MathQuiz:
    def __init__(self, parent):

        self.frame1 = Frame(parent)
        self.frame1.grid(row=0, column=0)

        self.TitleLabel = Label(self.frame1, bg="black", fg="white", width=30, padx=30, pady=10, text="Welcome to Math Quiz", font=("Times", "16", "bold italic"))
        self.TitleLabel.grid(columnspan=2)

        self.NameLabel = Label(self.frame1, text="Name", width=20, font=("Times", "14", "bold italic"))
        self.NameLabel.grid(row=2, column=0, sticky=W)

        self.name = StringVar()
        self.name.set("")
        self.NameEntry = Entry(self.frame1, textvariable=self.name, width=20)
        self.NameEntry.grid(row=2, column=1, sticky=W)

        self.AgeLabel = Label(self.frame1, text="Age", width=20, font=("Times", "14", "bold italic"))
        self.AgeLabel.grid(row=3, column=0, sticky=W)

        self.age = IntVar()
        self.age.set("")
        self.AgeEntry = Entry(self.frame1, width=20, textvariable=self.age)
        self.AgeEntry.grid(row=3, column=1, sticky=W)

        self.warning = Label(self.frame1, text="")
        self.warning.grid(row=4, column=1, columnspan=3)

        self.SelectLabel = Label(self.frame1, text="Select difficulty", width=20, font=("Times", "14", "bold italic"))
        self.SelectLabel.grid(row=5, column=0, sticky=W)

        self.diff = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.diff)):
            rb = Radiobutton(self.frame1, variable=self.diff_lvl, value=i, text=self.diff[i], anchor=W, padx=50, width="10", height="2")
            self.diff_btns.append(rb)
            rb.grid(row=i+6, column=0, sticky=W)

        self.submit = Button(self.frame1, text="Next", command=self.show_frame2)
        self.submit.grid(row=9, column=1)


        self.index = 0
        self.score = 0
        self.frame2 = Frame(parent, height="450", width="400")

        self.questions = Label(self.frame2, bg="black", fg="white", width=30, padx=30, pady=10, text="Quiz Questions", font=("Times", "14", "bold italic"))
        self.questions.grid(row=0, columnspan=3)

        self.QuestionLabel = Label(self.frame2, text="Click Next", width=15, height=3)
        self.QuestionLabel.grid(row=1, column=0, sticky=W)

        self.AnswerEntry = Entry(self.frame2, width=20)
        self.AnswerEntry.grid(row=1, column=1, sticky=W)

        self.quiz_label = Label(self.frame2, text="Problems", font=("Times", "14", "bold"))
        self.quiz_label.grid(row=1, column=2, columnspan=5, sticky="EW")

        self.feedback = Label(self.frame2, text = "Click Check answer button")
        self.feedback.grid(row=2, column=0, columnspan=4)

        self.home = Button(self.frame2, text="Home", anchor=W, command=self.show_frame1)
        self.home.grid(row=3, column=0)

        self.check = Button(self.frame2, text="Check answer", anchor=W, command=self.check_answer)
        self.check.grid(row=3, column=1)

        self.report_frame = Frame(parent, height="450", width="400")
        self.report_frame.grid_propagate(0)

        report_page = ["Name", "Age", "Score"]
        self.report_labels = []

        for i in range(len(report_page)):
            lb = Label(self.report_frame, text=report_page[i], anchor=W, width="7", height="2", font=("Times", "22", "bold"))
            self.report_labels.append(lb)
            lb.grid(row=1, column=i+1, sticky="EW")

        self.report_name = Label(self.report_frame, textvariable=self.name)
        self.report_name.grid(row=3, column=1, sticky="EW")

        self.report_age = Label(self.report_frame, textvariable=self.age)
        self.report_age.grid(row=3, column=2, sticky="EW")

        self.report_score = Label(self.report_frame, text="")
        self.report_score.grid(row=3, column=3)

        self.reporthome = Button(self.report_frame, text="Home", anchor=W, command=self.show_frame1)
        self.reporthome.grid(row=10, column=0)


    def show_frame1(self):
        self.score = 0
        self.frame2.grid_remove()
        self.report_frame.grid_remove()
        self.frame1.grid()

    def show_frame2(self):
        try:
            if self.name.get() == "":
                self.warning.configure(text="Please enter your name")
                self.NameEntry.focus()
            elif self.name.get().isalpha() == False:
                self.warning.configure(text="Please enter text")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()

            elif self.AgeEntry.get() == "":
                self.warning.configure(text="Please enter a number")
                self.AgeEntry.delete(0, END)
            elif self.age.get() > 12:
                self.warning.configure(text="You are too old to play this game!")
                self.age_entry.delete(0, END)
            elif self.age.get() <= 0:
                self.warning.configure(text="Please enter a number greater than 0")
                self.age_entry.delete(0, END)
            elif self.age.get() <=7:
                self.warning.configure(text="Oh No! You are too young to play this game!")
            else:
                self.frame1.grid_remove()
                self.frame2.grid(row=1, columnspan=4)
                self.next_problem()

        except ValueError:
            self.warning.configure(text="Please enter a number")
            self.AgeEntry.delete(0, END)
            self.AgeEntry.focus()

    def check_answer(self):
        try:
            ans = int(self.AnswerEntry.get())

            if ans == self.answer:
                self.feedback.configure(text = "Correct!")
                self.score += 1
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_problem()
            else:
                self.feedback.configure(text="Unlucky! Try again next time!")
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_problem()
        except ValueError:
            self.feedback.configure(text="This is not a number")
            self.AnswerEntry.delete(0, END)
            self.AnswerEntry.focus()

        if self.score <= 5:
            self.report_score.configure(text=str(self.score))

    def next_problem(self):
        x = randrange(10)
        y = randrange(10)
        self.select = self.diff_lvl.get()

        if self.select == "0":
            easy_text = str(x) + "  +  " + str(y) + "  = "

            self.answer = x + y
            self.index += 1

            self.QuestionLabel.configure(text = easy_text)
            self.quiz_label.configure(text="Question" + str(self.index)+ "/5")

        elif self.select == "1":
            medium_text = str(x) + "  -  " + str(y) + "  = "

            self.answer = x - y
            self.index += 1
            self.QuestionLabel.configure(text=medium_text)
            self.quiz_label.configure(text="Question"+ str(self.index)+ "/5")

        else:
            hard_text = str(x) + "  x  " + str(y) + "  = "

            self.answer = x * y
            self.index += 1

            self.QuestionLabel.configure(text=hard_text)
            self.quiz_label.configure(text="Question" + str(self.index)+ "/5")

        if self.index >= 6:
            self.frame2.grid_remove()
            self.report_frame.grid(row=1, columnspan=4)

if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("MathQuiz")
    root.mainloop()
        
