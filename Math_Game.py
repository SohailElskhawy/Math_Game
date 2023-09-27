import tkinter as tk
import random
import os


class MathGame:
    def __init__(self,root):
        self.buttons_color = "#222E50" # blue
        self.font_color = "#FCCB06" # yellow
        self.app_color = "#222E50" # blue
        self.root = root
        self.root.geometry("700x400")
        self.root.title("Math Game")
        self.root['background'] = self.app_color
        self.game_title = tk.Label(self.root,text="Math Game",bg=self.buttons_color,font=("Agency FB Bold",33),fg=self.font_color)
        self.game_title.place(x=270,y=0)
        
        self.start_button = tk.Button(self.root,text="Start Game",bg=self.buttons_color,font=("Agency FB Bold",25),width=15,borderwidth=5,command=self.choose_game_mode,fg=self.font_color)
        self.start_button.place(x=250,y=300)
        
        self.exit_button = tk.Button(self.root,text="Exit Game",bg=self.buttons_color,font=("Agency FB Bold",15),width=9,borderwidth=5,command=self.game_over,fg=self.font_color)
        self.high_score_label_home = tk.Label(self.root,font=("Agency FB Bold",25),fg=self.font_color,bg=self.buttons_color)
        self.game_mode = None
        self.difficulty = None
        self.timer = None
        self.points = 0
        self.current_high_score = 0
        self.load_game()
        self.high_score =  self.current_high_score
        if self.high_score > 0 :
            self.high_score_label_home.config(text=f'High Score : {self.high_score}')
            self.high_score_label_home.place(x=280,y=150)

    def choose_game_mode(self):

        self.game_title.destroy()
        self.start_button.destroy()
        if hasattr(self,'high_score_label_home'):
            self.high_score_label_home.destroy()
        self.game_mode_label = tk.Label(root,text="Select Game Mode: ",font=("Agency FB Bold",25),bg=self.buttons_color,fg=self.font_color)
        self.game_mode_label.place(x=50,y=30)
        
        self.add_btn = tk.Button(self.root,text="Addition",font=("Agency FB Bold",25),width=13,borderwidth=3,bg=self.buttons_color,command=lambda: self.select_difficulty("Add"),fg=self.font_color)
        self.add_btn.place(x=130,y=130)
        
        self.sub_btn = tk.Button(self.root,text="Subtraction",font=("Agency FB Bold",25),width=13,borderwidth=3,bg=self.buttons_color,command=lambda: self.select_difficulty("Sub"),fg=self.font_color)
        self.sub_btn.place(x=390,y=130)
        
        self.mul_btn = tk.Button(self.root,text="Multiplication",font=("Agency FB Bold",25),width=13,borderwidth=3,bg=self.buttons_color,command=lambda: self.select_difficulty("Mul"),fg=self.font_color)
        self.mul_btn.place(x=130,y=260)
        
        self.mix_btn = tk.Button(self.root,text="Mix",font=("Agency FB Bold",25),width=13,borderwidth=3,bg=self.buttons_color,command=lambda: self.select_difficulty("Mix"),fg=self.font_color)
        self.mix_btn.place(x=390,y=260)
        


    def select_difficulty(self,game_mode):
        self.game_mode = game_mode
        self.game_mode_label.destroy()
        self.add_btn.destroy()
        self.sub_btn.destroy()
        self.mul_btn.destroy()
        self.mix_btn.destroy()
        
        self.select_difficulty_label = tk.Label(root,text="Select Difficulty: ",font=("Agency FB Bold",25),bg=self.buttons_color,fg=self.font_color)
        self.select_difficulty_label.place(x=50,y=30)
        
        self.easy_btn = tk.Button(self.root,text="Easy",font=("Agency FB Bold",25),width=13,borderwidth=3,bg=self.buttons_color,fg=self.font_color,command=lambda: self.assign_game_diffuculy("Easy"))
        self.easy_btn.place(x=130,y=130)
        
        self.mid_btn = tk.Button(self.root,text="Hard",font=("Agency FB Bold",25),width=13,borderwidth=3,bg=self.buttons_color,fg=self.font_color,command=lambda: self.assign_game_diffuculy("Hard"))
        self.mid_btn.place(x=390,y=130)
        
        self.hard_btn = tk.Button(self.root,text="Very Hard",font=("Agency FB Bold",25),width=13,borderwidth=3,bg=self.buttons_color,fg=self.font_color,command=lambda: self.assign_game_diffuculy("Very Hard"))
        self.hard_btn.place(x=260,y=260)


    def assign_game_diffuculy(self,difficulty):
        self.difficulty = difficulty
        self.select_difficulty_label.destroy()
        self.easy_btn.destroy()
        self.mid_btn.destroy()
        self.hard_btn.destroy()
        self.show_question()

    
    def show_question(self):
        self.question = None
        self.operation = None
        self.answer = None
        
        if hasattr(self,'back'):
            self.back.destroy()
            
        
        
        
        self.question_label = tk.Label(self.root,bg=self.buttons_color,font=("Agency FB Bold",30),fg=self.font_color,width=20)
        if self.game_mode == 'Add':
            self.operation = '+'
            if self.difficulty == 'Easy':
                self.timer = 11 
                x = random.randint(1,50)
                y = random.randint(1,50)
                self.question_label.config(text=f"{x} {self.operation} {y} = ")
                self.answer = eval(f"{x} {self.operation} {y}")
            elif self.difficulty == 'Hard':
                self.timer = 16 
                x = random.randint(1,30)
                y = random.randint(1,100)
                z = random.randint(1,30)
                self.question_label.config(text=f"{x} {self.operation} {y} {self.operation} {z} = ")
                self.answer = eval(f"{x} {self.operation} {y} {self.operation} {z}")
            elif self.difficulty == 'Very Hard':
                self.timer = 21 
                x = random.randint(1,40)
                y = random.randint(1,40)
                z = random.randint(1,60)
                w = random.randint(1,150)
                self.question_label.config(text=f"{x} {self.operation} {y} {self.operation} {z} {self.operation} {w} = ")
                self.answer = eval(f"{x} {self.operation} {y} {self.operation} {z} {self.operation} {w}")
        if self.game_mode == 'Sub':
            self.operation = '-'
            if self.difficulty == 'Easy':
                self.timer = 11 
                x = random.randint(1,40)
                y = random.randint(1,10)
                self.question_label.config(text=f"{x} {self.operation} {y} = ")
                self.answer = eval(f"{x} {self.operation} {y}")
            elif self.difficulty == 'Hard':
                self.timer = 16 
                x = random.randint(1,50)
                y = random.randint(1,30)
                z = random.randint(1,40)
                self.question_label.config(text=f"{x} {self.operation} {y} {self.operation} {z} = ")
                self.answer = eval(f"{x} {self.operation} {y} {self.operation} {z}")
            elif self.difficulty == 'Very Hard':
                self.timer = 21 
                x = random.randint(1,70)
                y = random.randint(1,50)
                z = random.randint(1,30)
                w = random.randint(1,20)
                self.question_label.config(text=f"{x} {self.operation} {y} {self.operation} {z} {self.operation} {w} = ")
                self.answer = eval(f"{x} {self.operation} {y} {self.operation} {z} {self.operation} {w}")
        if self.game_mode == 'Mul':
            self.operation = '*'
            if self.difficulty == 'Easy':
                self.timer = 11 
                x = random.randint(1,12)
                y = random.randint(0,12)
                self.question_label.config(text=f"{x} {self.operation} {y} = ".replace('*','x'))
                self.answer = eval(f"{x} {self.operation} {y}")
            elif self.difficulty == 'Hard':
                self.timer = 16 
                x = random.randint(1,10)
                y = random.randint(1,12)
                z = random.randint(1,10)
                self.question_label.config(text=f"{x} {self.operation} {y} {self.operation} {z} = ".replace('*','x'))
                self.answer = eval(f"{x} {self.operation} {y} {self.operation} {z}")
            elif self.difficulty == 'Very Hard':
                self.timer = 21 
                x = random.randint(1,10)
                y = random.randint(1,12)
                z = random.randint(1,14)
                w = random.randint(1,10)
                self.question_label.config(text=f"{x} {self.operation} {y} {self.operation} {z} {self.operation} {w} = ".replace('*','x'))
                self.answer = eval(f"{x} {self.operation} {y} {self.operation} {z} {self.operation} {w}")
        if self.game_mode == 'Mix':
            # self.operation = random.choice(["+" ,"-" ,"*"])
            if self.difficulty == 'Easy':
                self.timer = 11
                x = random.randint(1,20)
                y = random.randint(1,20)
                self.question_label.config(text=f"{x} {random.choice(['+' ,'-' ,'*'])} {y} = ".replace('*','x'))
                # self.answer = eval(f"{x} {self.operation} {y}")
                self.answer = eval(self.question_label.cget('text').replace('x','*').split("=")[0])
            elif self.difficulty == 'Hard':
                self.timer = 16 
                x = random.randint(1,10)
                y = random.randint(1,12)
                z = random.randint(1,10)
                self.question_label.config(text=f"{x} {random.choice(['+' ,'-' ,'*'])} {y} {random.choice(['+' ,'-' ,'*'])} {z} = ".replace('*','x'))
                # self.answer = eval(f"{x} {self.operation} {y} {self.operation} {z}")
                self.answer = eval(self.question_label.cget('text').replace('x','*').split("=")[0])
            elif self.difficulty == 'Very Hard':
                self.timer = 21 
                x = random.randint(1,10)
                y = random.randint(1,10)
                z = random.randint(1,12)
                w = random.randint(1,10)
                self.question_label.config(text=f"{x} {random.choice(['+' ,'-' ,'*'])} {y} {random.choice(['+' ,'-' ,'*'])} {z} {random.choice(['+' ,'-' ,'*'])} {w} = ".replace('*','x'))
                # self.answer = eval(f"{x} {self.operation} {y} {self.operation} {z} {self.operation} {w}")
                self.answer = eval(self.question_label.cget('text').replace('x','*').split("=")[0])
        
        self.question_label.place(x=200,y=70)

        self.show_choices()
        
        if hasattr(self,'time_label') == False:
            self.display_points_time()
    
    
    def show_choices(self):
        question_ans = self.answer
        choices = [question_ans]
        
        while len(choices) < 4:
            if self.game_mode == 'Sub':
                min_choice = min((-1 * int(self.answer)) - 1000, int(self.answer))
                max_choice = max((-1 * int(self.answer)) - 1000, int(self.answer))
                choice = random.randint(min_choice, max_choice)
            elif self.game_mode == 'Mix':
                min_choice = min((-1 * int(self.answer)) - 1000, int(self.answer))
                max_choice = max((-1 * int(self.answer)) - 1000, int(self.answer))
                choice = random.randint(min_choice, max_choice)
            else :
                min_choice = 0
                max_choice = int(self.answer) + 50
                choice = random.randint(min_choice,max_choice)
            
            if choice != int(question_ans) and choice not in choices:
                choices.append(choice)
        
        random.shuffle(choices)
        
        self.choice_buttons = []
        
        for i,c in enumerate(choices):
            choice_but = tk.Button(self.root, text=f" {c} ",font=("Agency FB Bold",20),width=10,borderwidth=4,fg=self.font_color,bg=self.buttons_color,command=lambda ans = c: self.check_anwers(ans))
            if i %2==0:
                choice_but.place(x=230 ,y= 170 + i * 70)
            else: choice_but.place(x=370,y= 170 + (i - 1) * 70)
            self.choice_buttons.append(choice_but)


    def display_points_time(self):
        self.time_label = tk.Label(self.root,text=f'Time : {self.timer}',font=("Agency FB Bold",20),fg=self.font_color,bg=self.buttons_color)
        self.time_label.place(x=50,y=30)
        self.activate_timer()
        self.points_label = tk.Label(self.root,text=f'Points : {self.points}',font=("Agency FB Bold",20),fg=self.font_color,bg=self.buttons_color)
        self.points_label.place(x=50,y=80)
        self.exit_button.place(x=600,y=30)


    def check_anwers(self,selected_answer):
        

        if selected_answer == self.answer:
            self.points += 1 
            self.clear_question()
            self.show_question()
        else:
            self.points -= 1 
            self.clear_question()
            self.show_question()
        self.points_label.config(text=f'Points : {self.points}')

    def clear_question(self):
        if hasattr(self,'question_label'):
            self.question_label.destroy()
        if hasattr(self,'choice_buttons'):
            for but in self.choice_buttons:
                but.destroy()




    def activate_timer(self):
        self.timer -= 1
        if self.timer > 0 :
            self.time_label.config(text=f'Time : {self.timer}')
            self.root.after(1050,self.activate_timer)
        
        if self.timer == 0 :
            self.game_over()

    
    
    def game_over(self):
        self.timer = 0
        if self.points > self.high_score:
            self.high_score = self.points
        
        self.clear_question()
        self.time_label.destroy()
        self.points_label.destroy()
        self.exit_button.destroy()
        self.save_game()

        self.points_label = tk.Label(self.root,text=f'Points : {self.points}',font=("Agency FB Bold",30),fg=self.font_color,bg=self.buttons_color)
        self.points_label.place(x=300,y=70)
        
        self.high_score_label = tk.Label(self.root,text=f'High Score : {self.high_score}',font=("Agency FB Bold",30),fg=self.font_color,bg=self.buttons_color)
        self.high_score_label.place(x=300,y=150)
        
        note_label = tk.Label(self.root,text=f'To Play Again Run App From its directory',font=("Agency FB Bold",18),fg=self.font_color,bg=self.buttons_color)
        note_label.place(x=250,y=210)
        
        self.play_again_but = tk.Button(self.root,text="Play Again",bg=self.buttons_color,font=("Agency FB Bold",25),width=10,borderwidth=5,fg=self.font_color,command=self.root.destroy)
        self.play_again_but.place(x=290,y=270)

    
    
    def save_game(self):
        self.current_high_score = self.high_score
        
        with open("math_game_data.txt",'w') as data:
            data.truncate(0)
            data.write(str(self.current_high_score))

    
    def load_game(self):
        if os.path.exists("math_game_data.txt"):
            with open('math_game_data.txt','r') as data:
                line = data.readline().strip()
                if line:
                    self.current_high_score = int(line)
                else:
                    self.current_high_score = 0
        else: self.current_high_score = 0
        

    
    def run(self):
        self.root.mainloop()












if __name__ == "__main__":
    
    root = tk.Tk()
    app = MathGame(root)
    app.run()
    app.save_game()
    