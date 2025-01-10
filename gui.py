import tkinter as tk
from tkinter import messagebox
from quiz import Quiz
from PIL import Image, ImageTk  # Importa PIL para trabajar con imágenes
import pygame  # Importar pygame para reproducir sonidos

class QuizApp:
    def __init__(self):
        self.quiz = Quiz('questions.json')
        self.window = tk.Tk()
        self.window.title("Juego de Preguntas y Respuestas")
        self.window.geometry("500x350")  # Aumenté el tamaño para mejor visualización
        
        # Inicializar pygame para manejar los sonidos
        pygame.mixer.init()

        # Cargar la imagen de fondo
        self.bg_image = Image.open(r"asset\closeup-shot-siberian-tiger-jungle.jpg")  # Asegúrate de usar la ruta correcta de la imagen
        self.bg_image = self.bg_image.resize((500, 350), Image.Resampling.LANCZOS)  # Redimensiona la imagen al tamaño de la ventana
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # Crear un Canvas para poner la imagen de fondo
        self.canvas = tk.Canvas(self.window, width=500, height=350)
        self.canvas.pack(fill="both", expand=True)
        
        # Colocar la imagen en el Canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        # Crear los widgets sobre la imagen
        self.question_label = tk.Label(self.window, text="", wraplength=400, font=("Arial", 14), bg="#f0f8ff")
        self.canvas.create_window(250, 50, window=self.question_label)  # Coloca la pregunta sobre el canvas
        
        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.window, text="", width=40, height=2, bg="#87ceeb", fg="black", font=("Arial", 12), command=lambda idx=i: self.check_answer(idx))
            self.canvas.create_window(250, 100 + i * 40, window=btn)  # Coloca los botones sobre el canvas
            self.buttons.append(btn)

        # Etiqueta para el temporizador
        self.timer_label = tk.Label(self.window, text="Tiempo restante: 10", font=("Arial", 12), bg="#f0f8ff")
        self.canvas.create_window(250, 300, window=self.timer_label)  # Coloca el temporizador en la parte inferior

        self.time_left = 10  # Tiempo inicial en segundos
        self.timer_running = False
        self.answered = False  # Para rastrear si la pregunta ha sido respondida

        self.load_question()

    def load_question(self):
        self.time_left = 10  # Restablecer el temporizador a 10 segundos cada vez que se cargue una nueva pregunta
        self.timer_running = True  # Iniciar el temporizador
        self.answered = False  # Restablecer el estado de respuesta

        question = self.quiz.get_question()
        if question:
            self.question_label.config(text=question['pregunta'])
            opciones = question['opciones']
            for i in range(4):
                self.buttons[i].config(text=opciones[i], bg="#87ceeb", state="normal")  # Reiniciar el color y estado de los botones
            # Comenzar el temporizador
            self.update_timer()
        else:
            # Mostrar el puntaje final solo cuando no haya más preguntas
            messagebox.showinfo("Juego terminado", f"Tu puntaje final es {self.quiz.score} de {len(self.quiz.questions)}")
            self.window.quit()

    def update_timer(self):
        if self.timer_running and self.time_left > 0:
            self.timer_label.config(text=f"Tiempo restante: {self.time_left}")
            self.time_left -= 1
            self.window.after(1000, self.update_timer)  # Llamar a la función cada 1000 ms (1 segundo)
        elif self.time_left == 0:
            self.timer_label.config(text="¡Tiempo agotado!")
            self.buttons_disabled()  # Deshabilitar los botones cuando se acaba el tiempo
            self.mark_as_incorrect()  # Marcar la respuesta como incorrecta si no fue respondida
            self.load_question()  # Cargar la siguiente pregunta

    def mark_as_incorrect(self):
        if not self.answered:  # Solo marcar como incorrecta si no ha sido respondida
            for btn in self.buttons:
                btn.config(bg="#ff6347")  # Marcar todos los botones como incorrectos
            correcta = self.quiz.questions[self.quiz.current_question - 1]['respuesta']
            messagebox.showinfo("Incorrecto", f"¡Tiempo agotado! La respuesta correcta era: {correcta}", icon='warning')
            # Reproducir el sonido de respuesta incorrecta
            pygame.mixer.music.load("asset/fail-234710.mp3")  # Cargar el archivo de sonido
            pygame.mixer.music.play()  # Reproducir el sonido

    def check_answer(self, idx):
        if self.answered:  # Evitar que se responda más de una vez
            return

        self.answered = True  # Marcar la pregunta como respondida
        question = self.quiz.get_question()  # Asegurarse de que haya una pregunta cargada
        if not question:
            return  # Evitar el error si no hay preguntas cargadas

        selected_answer = self.buttons[idx]['text']
        correcto = self.quiz.check_answer(selected_answer)
        if correcto:
            self.buttons[idx].config(bg="#32cd32")  # Botón verde si la respuesta es correcta
            messagebox.showinfo("Correcto", "¡Respuesta correcta!", icon='info')
            # Reproducir el sonido de respuesta correcta
            pygame.mixer.music.load("asset/correct-156911.mp3")  # Cargar el archivo de sonido
            pygame.mixer.music.play()  # Reproducir el sonido
        else:
            self.buttons[idx].config(bg="#ff6347")  # Botón rojo si la respuesta es incorrecta
            correcta = self.quiz.questions[self.quiz.current_question - 1]['respuesta']
            messagebox.showinfo("Incorrecto", f"Respuesta incorrecta. La correcta era: {correcta}", icon='warning')
            # Reproducir el sonido de respuesta incorrecta
            pygame.mixer.music.load("asset/fail-234710.mp3")  # Cargar el archivo de sonido
            pygame.mixer.music.play()  # Reproducir el sonido

        self.load_question()

    def buttons_disabled(self):
        for btn in self.buttons:
            btn.config(state="disabled")  # Deshabilitar los botones después de que se acabe el tiempo

    def run(self):
        self.window.mainloop()
