from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain.chains import ConversationalRetrievalChain
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.vectorstores.faiss import FAISS
from pydub import AudioSegment
from pydub.playback import play
import whisper
import torch
import numpy as np
import os
from dotenv import load_dotenv
import sounddevice as sd
from langchain.memory import ConversationBufferMemory
import time
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
groq_key = os.getenv("GROQ_API_KEY")


initial_summary = """:The candidate is a software engineer with 5 years of experience in web development. They
have worked on projects using JavaScript, React, and Node.js. They are passionate about
creating user-friendly and performant web applications."""


client = OpenAI(api_key=api_key)
model = "base"
english = True
energy = 300
pause = 0.8
dynamic_energy = True
verbose = True

if model != "large" and english:
    model = model + ".en"
audio_model = whisper.load_model(model)

def transcribe(audio_data):
    if english:
        result = audio_model.transcribe(audio_data, language='english')
    else:
        result = audio_model.transcribe(audio_data)
    return result["text"]

def record_audio(duration, sample_rate):
    print("Listening...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()
    audio_data = np.squeeze(audio_data)
    return audio_data

def speak(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="shimmer",
        input=text
    )
    file_name = "reply.mp3"
    client.with_streaming_response.audio.speech.create
    response.stream_to_file(file_name)
    reply_audio = AudioSegment.from_mp3(file_name)
    play(reply_audio)
    os.remove(file_name)

MODEL_NAME = "llama3-8b-8192"
chat = ChatGroq(temperature=0.3, groq_api_key= groq_key, model_name=MODEL_NAME)

def generate_question(conversation_summary):
    system = f"""You are an AI recruiter specializing in analyzing candidate summaries and conducting engaging interviews. remember {initial_summary} You remember the complete conversation and prioritize the last discussed point.
                you will be talking to the canditate directly so be professional and human-like. and responses should contain only communication from the AI recruiter. and the conversation should be completely human-like and should
                be in a way exactly like a human would ask. and dont sound like a robot or a machine."""
    human = conversation_summary
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
    chain = prompt | chat

    response = chain.invoke({"text": "Generate a relevant follow-up question or a new question to continue the interview."})

    try:
        # Accessing the 'content' property directly to retrieve the response text
        content = response.content
    except AttributeError:
        print("Failed to retrieve the content. Check the correct method/property.")
        content = "Sorry, I couldn't generate a question. Let's move on."

    return content


def main():
    print("Welcome to the interview screening chatbot!")
    candidate_summary = "summary of The candidate is a software engineer with 5 years of experience in web development. They have worked on projects using JavaScript, React, and Node.js. They are passionate about creating user-friendly and performant web applications."

    conversation_summary = "As comversation starter introduce yourself and ask the candidate to introduce themselves."
    question_count = 1

    # greeting = "Hey there! How are you doing today? Let"
    # speak(greeting)
    # print(f"Bot: {greeting}")

    while question_count <= 5:
        # if question_count == 1:
        #     question = generate_question(candidate_summary)
        # else:
        question = generate_question(conversation_summary)

        speak(question)
        audio_data = record_audio(duration=10, sample_rate=16000)
        response = transcribe(audio_data)
        time.sleep(5)
        conversation_summary += f"Question {question_count}: {question}\nAnswer: {response}\n\n"
        print(f"Question {question_count}: {question}")
        print(f"Answer: {response}\n")
        question_count += 1

    speak("Thank you for your responses. The interview is now complete.")
    print("Interview summary:")
    print(conversation_summary)

if __name__ == "__main__":
    main()
