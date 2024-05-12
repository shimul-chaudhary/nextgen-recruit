from langgraph.graph import StateGraph, END

from graph_state import GraphState
from prompts import *
import json
from filter_handlers import *

def run_filter_app(job_payload):

    print(job_payload)
    print("**********************START***********************\n\n")

    parsed_resume = handle_resume_parser(job_payload['resume'])

    print(parsed_resume)

    print("**********************PARSE***********************\n\n")

    workflow = StateGraph(GraphState)

    workflow.add_node("handle_question", handle_question)
    workflow.add_node("handle_evaluate", handle_evaluate)
    workflow.add_node("handle_response", handle_response)
    workflow.add_node("handle_result", handle_result)

    workflow.add_conditional_edges(
        "handle_evaluate",
        check_conv_length,
        {
            "handle_question": "handle_question",
            "handle_result": "handle_result"
        }
    )

    workflow.set_entry_point("handle_question")
    workflow.add_edge("handle_question", "handle_response")
    workflow.add_edge("handle_response", "handle_evaluate")
    workflow.add_edge("handle_result", END)

    app = workflow.compile()

    conversation = app.invoke({'history': '', 'job_description': job_payload['description'], 'resume': parsed_resume, 'current_question': '', 'current_answer': '', 'total_questions': 0, 'summary': ''})

    print(conversation['summary'])
    return conversation['summary'], parsed_resume

def get_filter_app(job_payload):
    return run_filter_app(job_payload)
