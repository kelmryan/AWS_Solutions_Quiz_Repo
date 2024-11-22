import tkinter as tk
from tkinter import messagebox
import os
import random
import sys

readme_path = sys.argv[1]

# install requirements
def install_requirements():
    try:
        print("Installing required packages...")
        os.system("pip install -r requirements.txt")
    except OSError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
install_requirements()

# Questions and answers
def load_questions_from_readme(readme_path):
    questions = []
    question_number = 0
    if os.path.exists(readme_path):
        with open(readme_path, "r") as file:
            lines = file.readlines()
            question = None
            options = []
            correct = None
            for line in lines:
                line = line.strip()
                if line.startswith("###"):
                    if question:
                        questions.append({"question": question, "options": options, "correct": correct, "question_number": question_number})
                    question = line[3:].strip()
                    options = []
                    correct = None
                    question_number += 1
                elif line.startswith("- [ ]"):
                    options.append(line[5:].strip())
                elif line.startswith("- [x]"):
                    options.append(line[5:].strip())
                    correct = len(options) - 1
            if question:
                questions.append({"question": question, "options": options, "correct": correct, "question_number": question_number})
    return questions

questions = load_questions_from_readme(readme_path)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.current_question = 0
        self.score_correct = 0
        self.score_incorrect = 0
        self.randomize_question_order()
        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text=questions[self.current_question]["question"], wraplength=400, font=("Helvetica", 12, "bold"))
        self.question_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.var = tk.IntVar()
        self.var.set(-1)

        self.option_buttons = []
        for idx, option in enumerate(questions[self.current_question]["options"]):
            btn = tk.Radiobutton(self.root, text=option, variable=self.var, value=idx, wraplength=400)
            btn.grid(row=1+idx, column=0, columnspan=2, sticky="w", padx=20, pady=5)
            self.option_buttons.append(btn)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1+len(questions[self.current_question]["options"]), column=0, columnspan=2, pady=20)
        # submit button
        self.submit_button = tk.Button(button_frame, text="Submit", command=self.check_answer)
        self.submit_button.grid(row=0, column=0, padx=10, pady=10)
        # next button
        self.next_button = tk.Button(button_frame, text="Next", command=self.next_question)
        self.next_button.grid(row=0, column=2, padx=10, pady=10)
        # sets the back button
        self.back_button = tk.Button(button_frame, text="Back", command=self.previous_question, state="disabled")
        self.back_button.grid(row=0, column=3, padx=10, pady=10)
        # Create the initial frame
        score_frame = tk.Frame(self.root)
        score_frame.grid(row=2+len(questions[self.current_question]["options"]), column=0, columnspan=2, pady=20)
        # Label how many correct in green
        self.correct_label = tk.Label(score_frame, text=f"Correct: {self.score_correct}", fg="green")
        self.correct_label.grid(row=0, column=0, padx=10)

        self.incorrect_label = tk.Label(score_frame, text=f"Incorrect: {self.score_incorrect}", fg="red")
        self.incorrect_label.grid(row=0, column=1, padx=10)

        self.question_counter_label = tk.Label(score_frame, text=f"Question {questions[self.current_question]['question_number']} of {len(questions)}", fg="black")
        self.question_counter_label.grid(row=0, column=2, padx=10)

    def next_question(self):
        self.current_question += 1
        if self.current_question >= len(questions):
            messagebox.showinfo("Quiz Completed", f"Your score is {self.score_correct}/{len(questions)}")
            self.root.quit()
        else:
            self.question_label.config(text=questions[self.current_question]["question"])
            self.var.set(-1)
            for idx, option in enumerate(questions[self.current_question]["options"]):
                self.option_buttons[idx].config(text=option, fg="black")
            self.submit_button.config(state="normal")
        self.back_button.config(state="normal" if self.current_question > 0 else "disabled")
        self.update_question_counter()

    def previous_question(self):
        self.current_question -= 1
        self.question_label.config(text=questions[self.current_question]["question"])
        self.var.set(-1)
        for idx, option in enumerate(questions[self.current_question]["options"]):
            self.option_buttons[idx-1].config(text=option, fg="black")
        self.submit_button.config(state="normal")
        self.back_button.config(state="normal" if self.current_question > 0 else "disabled")
        self.update_question_counter()
        
    def reset_answer(self):
        self.var.set(-1)
        for btn in self.option_buttons:
            btn.config(fg="black")
        self.submit_button.config(state="normal")
        self.next_button.config(state="disabled")

    def randomize_question_order(self):
        random.shuffle(questions)
        self.current_question = 0

    def check_answer(self):
        selected = self.var.get()
        if selected == -1:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        if selected == questions[self.current_question]["correct"]:
            self.option_buttons[selected].config(fg="green")
            self.score_correct += 1
        else:
            self.option_buttons[selected].config(fg="red")
            self.score_incorrect += 1

        self.question_counter_label.config(text=f"Question {questions[self.current_question]['question_number']} of {len(questions)}")
        self.correct_label.config(text=f"Correct: {self.score_correct}")
        self.incorrect_label.config(text=f"Incorrect: {self.score_incorrect}")
        self.next_button.config(state="normal")

    def update_question_counter(self):
        self.question_counter_label.config(text=f"Question {questions[self.current_question]['question_number']} of {len(questions)}")
        self.correct_label.config(text=f"Correct: {self.score_correct}")
        self.incorrect_label.config(text=f"Incorrect: {self.score_incorrect}")

if len(sys.argv) != 2:
    print("Usage: python quizapp.py <path_to_readme>")
    sys.exit(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
