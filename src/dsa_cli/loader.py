from dataclasses import dataclass
from pathlib import Path
import json

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
        return [Question(**entry) for entry in data]
