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
        self.current_question = 0
        self.score = 0
        self.lives = 3
        self.difficulty = 'easy'
        self.save_progress()

    def get_question(self):
        if self.current_question < len(self.questions_by_difficulty[self.difficulty]):
            return self.questions_by_difficulty[self.difficulty][self.current_question]
        return None

    def check_answer(self, answer):
        correct = self.questions_by_difficulty[self.difficulty][self.current_question]['respuesta']
        if answer == correct:
            self.score += 1
            result = True
        else:
            self.lives -= 1
            result = False
        self.current_question += 1
        return result

    def has_more_questions(self):
        return self.current_question < len(self.questions_by_difficulty[self.difficulty])

    def save_progress(self):
        progress = {
            'current_question': self.current_question,
            'score': self.score,
            'lives': self.lives,
            'difficulty': self.difficulty
        }
        with open('progress.json', 'w', encoding='utf-8') as file:
            json.dump(progress, file)

    def load_progress(self):
        try:
            with open('progress.json', 'r', encoding='utf-8') as file:
                progress = json.load(file)
                self.current_question = progress['current_question']
                self.score = progress['score']
                self.lives = progress['lives']
                self.difficulty = progress['difficulty']
        except FileNotFoundError:
            pass