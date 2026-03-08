from pathlib import Path
from loader import load_question, Question
from display import show_question
import json
import questionary

BASE_DIR = Path(__file__).parent    
QUESTION_PATH = BASE_DIR / '../../questions/questions.json'

def main():
    
    questions = load_question(QUESTION_PATH)
    titles = [question.title for question in questions]
    question_dict = {question.title: question for question in questions} 
    
    is_running = True
    while is_running:

        answer = questionary.autocomplete('Search for a question:', choices=titles).ask()
        
        if answer == 'exit' or answer is None:
            is_running = False
            break
        elif answer not in question_dict:
            print('Question not found!')
            continue

        show_question(question_dict[answer])
        
        option = ['back', 'exit']
        choice = questionary.select('What next?', choices=option).ask()
        if choice == 'exit':
            is_running = False


if __name__ == "__main__":
    main()
