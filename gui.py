import tkinter as tk
from tkinter import messagebox
from quiz import Quiz
from PIL import Image, ImageTk
import pygame

class QuizApp:
    def __init__(self):
        self.quiz = Quiz('questions.json')
        self.window = tk.Tk()
        self.window.title("Juego de Preguntas y Respuestas")
        self.window.geometry("500x350")

        pygame.mixer.init()

        self.bg_image = Image.open(r"asset\closeup-shot-siberian-tiger-jungle.jpg")
        self.bg_image = self.bg_image.resize((500, 350), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.window, width=500, height=350)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        self.question_label = tk.Label(self.window, text="", wraplength=400, font=("Arial", 14), bg="#f0f8ff")
        self.canvas.create_window(250, 50, window=self.question_label)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.window, text="", width=40, height=2, bg="#87ceeb", fg="black", font=("Arial", 12), command=lambda idx=i: self.check_answer(idx))
            self.canvas.create_window(250, 100 + i * 40, window=btn)
            self.buttons.append(btn)

        self.timer_label = tk.Label(self.window, text="Tiempo restante: 10", font=("Arial", 12), bg="#f0f8ff")
        self.canvas.create_window(250, 300, window=self.timer_label)

        self.time_left = 10
        self.timer_running = False
        self.answered = False

        self.load_question()

    def load_question(self):
        self.timer_running = False
        self.time_left = 10
        self.timer_running = True
        self.answered = False

        question = self.quiz.get_question()
        if question:
            self.question_label.config(text=question['pregunta'])
            opciones = question['opciones']
            for i in range(4):
                self.buttons[i].config(text=opciones[i], bg="#87ceeb", state="normal")
            self.update_timer()
        else:
            messagebox.showinfo("Juego terminado", f"Tu puntaje final es {self.quiz.score} de {len(self.quiz.questions)}")
            self.window.quit()

    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            self.timer_label.config(text=f"Tiempo restante: {self.time_left}")
            self.time_left -= 1
            self.window.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.timer_label.config(text="¡Tiempo agotado!")
            self.buttons_disabled()
            self.mark_as_incorrect()

    def mark_as_incorrect(self):
        if not self.answered:
            for btn in self.buttons:
                btn.config(bg="#ff6347")
            correcta = self.quiz.questions[self.quiz.current_question - 1]['respuesta']
            messagebox.showinfo("Incorrecto", f"¡Tiempo agotado! La respuesta correcta era: {correcta}", icon='warning')
            pygame.mixer.music.load("asset/fail-234710.mp3")
            pygame.mixer.music.play()
            self.window.after(1000, self.load_question)

    def check_answer(self, idx):
        if self.answered:
            return

        self.timer_running = False
        self.answered = True
        question = self.quiz.get_question()
        if not question:
            return

        selected_answer = self.buttons[idx]['text']
        correcto = self.quiz.check_answer(selected_answer)
        if correcto:
            self.buttons[idx].config(bg="#32cd32")
            messagebox.showinfo("Correcto", "¡Respuesta correcta!", icon='info')
            pygame.mixer.music.load("asset/correct-156911.mp3")
            pygame.mixer.music.play()
        else:
            self.buttons[idx].config(bg="#ff6347")
            correcta = self.quiz.questions[self.quiz.current_question - 1]['respuesta']
            messagebox.showinfo("Incorrecto", f"Respuesta incorrecta. La correcta era: {correcta}", icon='warning')
            pygame.mixer.music.load("asset/fail-234710.mp3")
            pygame.mixer.music.play()
        self.window.after(1000, self.load_question)

    def buttons_disabled(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = QuizApp()
    app.run()
