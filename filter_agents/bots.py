from langgraph.graph import StateGraph, END

from graph_state import GraphState
from prompts import *
from filter_handlers import handle_evaluate, handle_question, handle_response, handle_result, check_conv_length

def run_filter_app(job_payload):
    workflow = StateGraph(GraphState)
    print("************************************************JOB********************************************")
    print(job_payload)


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

    conversation = app.invoke({'history': '', 'interviewer': '', 'current_question': '', 'current_answer': '', 'total_questions': 0, 'candidate': ''})

    print(conversation['history'])

def get_filter_app(job_payload):
    return run_filter_app(job_payload)



