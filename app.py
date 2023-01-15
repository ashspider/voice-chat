from flask import Flask, request, render_template
import openai
import speech_recognition as sr

app = Flask(__name__)

def takeCommand(audio):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        return query
    except Exception as e:
        print("Say that again please...")  
        return "None"

def send_to_api(query):
    openai.api_key = "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"
    prompt = (f"User: {query}\n")
    response = openai.Completion.create(engine="text-davinci-002",prompt=prompt,max_tokens=1024)
    return response.choices[0].text

@app.route('/')
def home():
    return render_template('home.html', response='')

@app.route('/', methods=['POST'])
def get_audio():
    audio = request.form.get("audio")
    query = takeCommand(audio)
    response = send_to_api(query)
    return render_template('home.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
