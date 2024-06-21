**Repository Name: Generative AI Recruitment Copilot**

---

## Introduction
Welcome to the Generative AI Recruitment Copilot Recruiter repository! This repository hosts a conversational AI-based interview screening chatbot. The chatbot interacts with candidates, conducts interviews, and summarizes the conversations for further analysis.

---

## Technologies Used
- **Streamlit**: The chatbot interface is built using Streamlit, allowing for easy interaction and visualization of the interview process.
- **Python Libraries**:
  - **langchain**: Utilized for conversational AI capabilities.
  - **pydub**: For audio manipulation and playback.
  - **whisper**: Provides speech recognition functionality.
  - **numpy**: Required for numerical operations.
  - **os**: For interacting with the operating system.
  - **dotenv**: For loading environment variables.
  - **sounddevice**: Used for audio recording.
  - **openai**: Enables integration with OpenAI's language models.
  - **smtplib**: Facilitates sending emails.
  - **pyaudio**: Required for audio processing.
  - **pyautogui**: Used for automating GUI interactions.
  - **webbrowser**: Allows opening web browser tabs programmatically.
  - **pygame**: Enables audio playback functionalities.

---

## Setup Instructions
To set up and run the chatbot locally, follow these instructions:
1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory and add the following environment variables:
   ```
   OPENAI_API_KEY=<Your_OpenAI_API_Key>
   GROQ_API_KEY=<Your_Groq_API_Key>
   SMTP_PASSWORD=<Your_SMTP_Password>
   ```
4. Replace `<Your_OpenAI_API_Key>`, `<Your_Groq_API_Key>`, and `<Your_SMTP_Password>` with your respective API keys and password.
5. Run the Streamlit app by executing `streamlit run app.py`.
6. Access the chatbot interface in your web browser.

---

## Functionality Overview
The chatbot offers the following functionalities:
- Conducts interview screening with candidates.
- Generates follow-up questions based on the conversation.
- Summarizes the interview conversation.
- Sends an email with the interview summary.

---

## Acknowledgments
- This project utilizes various open-source libraries and APIs, without which it would not be possible.
- Special thanks to the developers and contributors of these tools for their valuable contributions to the open-source community.

---

Thank you for using the Generative AI Recruitement Copilot Recruiter chatbot! We hope it helps streamline your interview screening process effectively.
