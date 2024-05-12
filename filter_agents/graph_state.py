from typing import TypedDict, Optional 

class GraphState(TypedDict):
    history: str = ''
    result: str = ''
    total_questions: int = 0
    interviewer: str = ''
    candidate: str = ''
    current_question: str = ''
    current_answer: str = ''