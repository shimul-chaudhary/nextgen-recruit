from langchain.chains import ConversationalRetrievalChain
from pydub import AudioSegment
from pydub.playback import play
import whisper
import numpy as np
import os
from dotenv import load_dotenv
import sounddevice as sd
import time
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from openai import OpenAI
import smtplib
from email.message import EmailMessage

import pyaudio
import pyautogui as auto
import webbrowser
from pygame import mixer, _sdl2 as devicer

import pygame.sndarray

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

p = pyaudio.PyAudio()

def transcribe(audio_data):
    if english:
        result = audio_model.transcribe(audio_data, language='english')
    else:
        result = audio_model.transcribe(audio_data)
    return result["text"]

def record_audio(duration, sample_rate):
    print("Listening...")
    
    # sd.default.device = (1, 3)

    # vb_cable_device = 'CABLE Input (VB-Audio Virtual C'
    # pygame.mixer.set_output(vb_cable_device)
    # device = 'Speakers (Realtek(R) Audio)'
    # output = devicer.audio.get_audio_device_names(False)
    # print(input)
    # if vb_cable_device in output:
        # device = vb_cable_device
    # print(f"device-{device}")
    vb_cable_output_name = 'CABLE Output (VB-Audio Virtual Cable)'
    device_index = None

    # print()
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        # print(device_info)
        if device_info['name'] == vb_cable_output_name and device_info['maxInputChannels'] > 0:
            # print(device_info['name'])
            device_index = i
            break
    # device = 'CABLE Output (VB-Audio Virtual Cable)'

    audio_data = sd.rec(int(duration * sample_rate), device=device_index, samplerate=sample_rate, channels=1, dtype='float32')
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
    
    mixer.music.load(file_name)
    mixer.music.play()

    while mixer.music.get_busy():
        time.sleep(1)
    
    mixer.music.unload()
    
    # play(reply_audio)
    os.remove(file_name)
    # return reply_audio, file_name
    

MODEL_NAME = "llama3-8b-8192"
chat = ChatGroq(temperature=0.3, groq_api_key= groq_key, model_name=MODEL_NAME)

def generate_question(conversation_summary):
    system = f"""You are an AI recruiter specializing in analyzing candidate summaries referred as resume and conducting engaging interviews. remember {initial_summary} You remember the complete conversation and prioritize the last discussed point.
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

def join_meet(meet_link):
    webbrowser.open_new_tab(meet_link)
    time.sleep(7)
    # auto.hotkey('ctrl', 'd')
    auto.hotkey('ctrl', 'e')
    auto.click(1240.578125, 600.55859375)



# Function to send mail with conversation summary
def send_mail(conversation_summary):
    subject = "Interview Summary"
    body = f"Here is the summary of the interview conversation:\n\n{conversation_summary}"
    to_email = "nithingovindugari@gmail.com"  # Replace with the recipient's email address
    sender = "Next Gen Recruiter <nextgenrecruiter@gmail.com>"
    
    message = EmailMessage()
    message.set_content(body)
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = to_email
    
    # Send the message via SMTP server (replace with your SMTP server details)
    smtp_host = "smtp.mailtrap.io"
    smtp_port = 2525
    smtp_username = "8064bd9cae3b81"  # Replace with your SMTP username
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.send_message(message)
    
    return "Email sent successfully"


def main():
    print("Welcome to the interview screening chatbot!")
    # candidate_summary = "summary of The candidate is a software engineer with 5 years of experience in web development. They have worked on projects using JavaScript, React, and Node.js. They are passionate about creating user-friendly and performant web applications."

    conversation_summary = "As conversation starter introduce yourself and ask the candidate to introduce themselves."
    question_count = 1
    meet_link = "https://meet.google.com/iqk-zfwn-iyc"
    join_meet(meet_link)

    mixer.init(devicename = 'CABLE Input (VB-Audio Virtual Cable)') 
    # Initialize it with the correct device

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
    mixer.quit()    
    # Call the send_mail function to send the email
    send_mail(conversation_summary)

if __name__ == '__main__':
    main()
