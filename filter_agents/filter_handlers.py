import sys
import os

# Add the parent directory of your project to the Python path
project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_directory)

from prompts import *
from llama3_model import get_llm

llm = get_llm()

def handle_resume_parser(resume_txt):
    prompt = prompt_resume_parser.format(resume_txt)
    resume_data = llm.predict(prompt)

    return resume_data

def handle_question(state):
    history = state.get('history', '').strip()
    job_description = state.get('job_description', '').strip()

    prompt = prompt_jd.format(job_description, history)
    question = "JD Bot" + ": " + llm.predict(prompt)
    print("Question:", question)
    if history=='Nothing':
        history = ''

    return {"history": history+"\n"+question, "current_question": question, "total_questions": state.get('total_questions', 0) + 1}

def handle_response(state):
    history = state.get('history', '').strip()
    question = state.get('current_question', '').strip()
    resume = state.get('resume', '').strip()

    prompt = prompt_resume.format(resume, question)
    answer = "Resume Bot" + ": " + llm.predict(prompt)
    print("Response:", answer)
    
    return {"history": history+"\n"+answer, "current_answer": answer}

def handle_evaluate(state):
    question = state.get('current_question', '').strip()
    answer = state.get('current_answer', '').strip()
    history = state.get('history', '').strip()

    prompt = prompt_result.format(question, answer)
    evaluation = llm.predict(prompt)
    print("Evaluation:", evaluation)
    print("**********************DONE***************\n\n")
    return {"history": history+"\n"+evaluation}

def handle_result(state):
    history = state.get('history', '').strip()
    cleaned_up = llm.predict(prompt_cleanup.format(history))
    prompt = prompt_verdict.format(cleaned_up)
    summary = llm.predict(prompt)

    return {"summary": history+"\n"+summary}

def check_conv_length(state):
    return "handle_question" if state.get('total_questions') < 5 else "handle_result"