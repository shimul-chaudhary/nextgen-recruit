prompt_resume_parser= "You're a resume parser bot\
            You have the following resume text:\n{}\n.\
            Parse the data and extract candidate name, email id, location, work experience and project details from the text. For work experience and projects make sure to add all the details.\
            Output the data a json object with the following keys: name, email, location, work_experience, projects.\n\
            I want a true json output and no text crud around it."

prompt_jd = "You're a bot that loads a job description. You need to prescan a candidate based on the job description. This is the job description:\n{}\n This is the interview so far:\n{}\n\
    Check if the skills used in their past experience is somewhat relevant to the job. The answer doesn't have to match exactly with the job description says but the experience should still be relevant. \
    Ask your next question and don't repeat your questions.\
    Keep it less than 20 words and output just the question and no extra text."

prompt_resume = "You're a bot that loads a resume. This is the resume:\n{}\n Answer the questions you are being asked based on the work experience and projects provided in the resume. \
    Don't use your own knowledge but answer extensively using the context from the resume and show why you would be a good fit for the job. \
    Give detailed answers and relevant skills/past experiences. Output just the answer and no extra text. Question: {}"

prompt_result = "Check whether the given asnwers have a good fit with the job description? \
    The answers don't have to be too detailed or have detailed examples but the skills should be relevant. The answers will only come from the information from the resume.\
    Evaluate on a scale of 10 and give a short reason as well. \
        question:{}\nanswer:{}"

prompt_verdict = "Given the interview, should we select the candidate?\
    Give output as Yes or No with a reason. Average score of 6 or above across all questions is a yes candidate. \
        Also generate a summary of the responses so that they can be shared with the hiring team.\
            The interview:{}"


prompt_cleanup = "Remove empty dialogues, repeated sentences and repeated names to convert this input as a conversation:\n{}"
