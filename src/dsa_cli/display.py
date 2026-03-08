from loader import Question
from rich import print
from rich.console import Console
from rich.panel import Panel

console = Console()

DIFFICULTY_COLORS = {
    "easy": "green",
    "medium": "yellow",
    "hard": "red",
}

def show_question(question: Question) -> None:
    difficulty_color = DIFFICULTY_COLORS.get(question.difficulty.lower(), "white")
    subtitle = f"[{difficulty_color}]{question.difficulty.capitalize()}[/{difficulty_color}]  •  {question.category}"
    print(Panel(question.title, title="Question", subtitle=subtitle))

    for i, step in enumerate(question.steps):
        print(f'[bold green]{i+1}. {step}[/bold green]')
        console.input("[dim]-> Press Enter for next step...[/dim]")

    print(Panel(
        f"Time Complexity: {question.time_complexity}\nSpace Complexity: {question.space_complexity}",
        title="Summary"
    ))
