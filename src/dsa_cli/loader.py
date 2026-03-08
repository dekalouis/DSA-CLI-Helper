from dataclasses import dataclass
from pathlib import Path
import json

BASE_DIR = Path(__file__).parent
QUESTION_PATH = BASE_DIR / "../../questions/questions.json"

@dataclass
class Question:
    id: str
    title: str
    category: str
    difficulty: str
    steps: list[str]
    time_complexity: str
    space_complexity: str

def load_question(filepath: str) -> list[Question]:
    with open(filepath) as f:
        data = json.load(f)
        
        res = []
        for entry in data:
            new_entry = Question(**entry)
            # new_entry = Question(
            #     entry['id'], 
            #     entry['title'], 
            #     entry['category'], 
            #     entry['difficulty'], 
            #     entry['steps'], 
            #     entry['time_complexity'], 
            #     entry['space_complexity']
            # )
            res.append(new_entry)

        return res

# print(load_question(QUESTION_PATH))
