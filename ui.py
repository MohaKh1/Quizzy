import tkinter as tk
from quiz_brain import QuizBrain
from playsound import playsound
THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')
FONT2 = ('Arial',16, 'normal')

class UserInterface():

    def __init__(self, quiz: QuizBrain):
        self.quizz = quiz
        self.screen = tk.Tk()
        self.screen.title('Quizzler')
        self.screen.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_lab = tk.Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=FONT2)
        self.score_lab.grid(row=0, column=1)

        self.my_canvas = tk.Canvas(width=300, height=250, bg='white')
        self.my_canvas.grid(row=1,column=0, columnspan=2, pady=50)

        self.question_text = self.my_canvas.create_text(150, 125,text='Placeholder', fill=THEME_COLOR,width=280, font=FONT,justify='center')

        true_img = tk.PhotoImage(file='images/true.png')
        self.true = tk.Button(image=true_img,bd=0,activebackground=THEME_COLOR, highlightthickness=0, command=self.pressed_true)
        self.true.grid(column=1, row=2)

        false_img = tk.PhotoImage(file='images/false.png')
        self.false = tk.Button(image=false_img, bd=0, highlightthickness=0, activebackground=THEME_COLOR, command=self.pressed_false)

        self.false.grid(column=0,row=2)
        self.next_question()
        self.screen.mainloop()

    def next_question(self):
        if self.quizz.still_has_questions():
            self.my_canvas.config(bg='white')

            q_text = self.quizz.next_question()
            self.my_canvas.itemconfig(self.question_text, text=q_text, state='normal')
        else:
            self.game_over(self.quizz.score)

    def pressed_true(self):

        is_right = self.quizz.check_answer('True')
        self.feedback_to_user(is_right)
    def pressed_false(self):
        is_right = self.quizz.check_answer('False')
        self.feedback_to_user(is_right)

    def feedback_to_user(self, is_right):
        self.my_canvas.itemconfig(self.question_text, state='hidden')
        if is_right:
            self.score_lab.config(text=f'Score: {self.quizz.score}')

            playsound('C:/Users/thegr/Desktop/code/100days/Days/day 34/quizzler-app-start/correct.mp3')
            BG='#ADE8AC'

        else:
            self.score_lab.config(text=f'Score: {self.quizz.score}')

            playsound('C:/Users/thegr/Desktop/code/100days/Days/day 34/quizzler-app-start/wrong.mp3')
            BG='#DE6145'
        self.my_canvas.config(bg=BG)
        self.next_question()

    def game_over(self, score):
        self.screen.destroy()






