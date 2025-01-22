import json
import random

class Quiz:
    def __init__(self, question_file):
        self.question_file = question_file
        self.load_questions()
        self.reset_game()

    def load_questions(self):
        try:
            with open(self.question_file, 'r', encoding='utf-8') as file:
                self.questions = json.load(file)
            self.questions_by_difficulty = {
                'easy': [q for q in self.questions if q.get('dificultad') == 'fácil'],
                'medium': [q for q in self.questions if q.get('dificultad') == 'medio'],
                'hard': [q for q in self.questions if q.get('dificultad') == 'difícil']
            }
        except FileNotFoundError:
            print(f"El archivo {self.question_file} no se encontró.")
            self.questions = []
            self.questions_by_difficulty = {'easy': [], 'medium': [], 'hard': []}
        except json.JSONDecodeError:
            print(f"Error al leer el archivo {self.question_file}. Asegúrate de que el formato sea JSON válido.")
            self.questions = []
            self.questions_by_difficulty = {'easy': [], 'medium': [], 'hard': []}

    def reset_game(self):
        self.current_question_index = 0
        self.score = 0
        self.lives = 3
        self.asked_questions = []
        self.all_questions = self.questions_by_difficulty['easy'] + self.questions_by_difficulty['medium'] + self.questions_by_difficulty['hard']
        random.shuffle(self.all_questions)
        self.save_progress()

    def get_question(self):
        if self.current_question_index < len(self.all_questions):
            return self.all_questions[self.current_question_index]
        return None

    def check_answer(self, answer):
        correct = self.all_questions[self.current_question_index]['respuesta']
        if answer == correct:
            self.score += 1
            result = True
        else:
            self.lives = max(0, self.lives - 1)
            result = False
        self.current_question_index += 1
        return result

    def has_more_questions(self):
        return self.current_question_index < len(self.all_questions)

    def is_game_over(self):
        return self.lives == 0 or not self.has_more_questions()

    def save_progress(self):
        progress = {
            'current_question_index': self.current_question_index,
            'score': self.score,
            'lives': self.lives
        }
        with open('progress.json', 'w', encoding='utf-8') as file:
            json.dump(progress, file)

    def load_progress(self):
        try:
            with open('progress.json', 'r', encoding='utf-8') as file:
                progress = json.load(file)
                self.current_question_index = progress['current_question_index']
                self.score = progress['score']
                self.lives = progress['lives']
        except FileNotFoundError:
            pass