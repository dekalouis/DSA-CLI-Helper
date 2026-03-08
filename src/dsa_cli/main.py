from pathlib import Path
from loader import load_question, Question
from display import show_question
from rich import print
import questionary

BASE_DIR = Path(__file__).parent
QUESTION_PATH = BASE_DIR / '../../questions/questions.json'

def main():
    questions = load_question(QUESTION_PATH)
    titles = [question.title for question in questions]
    question_dict = {question.title: question for question in questions}

    while True:
        answer = questionary.autocomplete('Search for a question:', choices=titles).ask()

        if answer == 'exit' or answer is None:
            break
        elif answer not in question_dict:
            print('[red]Question not found![/red]')
            continue

        show_question(question_dict[answer])

        choice = questionary.select('What next?', choices=['back', 'exit']).ask()
        if choice == 'exit':
            break


if __name__ == "__main__":
    main()
