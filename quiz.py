import json
import random

class Quiz:
    def __init__(self, question_file):
        try:
            with open(question_file, 'r', encoding='utf-8') as file:
                self.questions = json.load(file)
            random.shuffle(self.questions)
            self.current_question = 0
            self.score = 0
        except FileNotFoundError:
            print(f"El archivo {question_file} no se encontró.")
            self.questions = []
            self.current_question = 0
            self.score = 0
        except json.JSONDecodeError:
            print(f"Error al leer el archivo {question_file}. Asegúrate de que el formato sea JSON válido.")
            self.questions = []
            self.current_question = 0
            self.score = 0

    def get_question(self):
        if self.current_question < len(self.questions):
            return self.questions[self.current_question]
        return None

    def check_answer(self, answer):
        correct = self.questions[self.current_question]['respuesta']
        if answer == correct:
            self.score += 1
            result = True
        else:
            result = False
        self.current_question += 1
        return result

    def has_more_questions(self):
        return self.current_question < len(self.questions)
