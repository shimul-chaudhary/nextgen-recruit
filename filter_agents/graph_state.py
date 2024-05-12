from typing import TypedDict 

class GraphState(TypedDict):
    history: str = ''
    job_description: str = ''
    resume: str = ''
    current_question: str = ''
    current_answer: str = ''
    total_questions: int = 0
    summary: str = ''