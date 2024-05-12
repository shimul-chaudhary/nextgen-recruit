prompt_interviewer = "You're a bot that loads a job description. You need to interview a candidate based on their resume. This is the interview so far:\n{}\n\
    Ask questions to figure out if the candidate is a good fit based on their resume. Ask your next question and don't repeat your questions.\
    Keep it less than 20 words and output just the question and no extra text."

prompt_interviewee = "You're a bot that loads a resume. This is the resume:\n{}\n Answer the questions you are being asked. Output just the answer and no extra text. Question: {}"

prompt_result = "Check whether the answer given for asked question is correct or not?\
    Evaluate on a scale of 10 and give a short reason as well\
        question:{}\nanswer:{}"

prompt_verdict = "Given the interview, should we select the candidate?\
    Give output as Yes or No with a reason. \
        Also generate a summary of the responses so that they can be shared with the hiring team.\
            The interview:{}"


prompt_cleanup = "Remove empty dialogues, repeated sentences and repeated names to convert this input as a conversation:\n{}"