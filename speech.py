import speech_recognition as sr
from pocketsphinx import LiveSpeech
import pyttsx3
import time
import browser
from word2number import w2n

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150) 
    engine.say(text) 
    engine.runAndWait()

def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("SPEAK")
        #say("waiting for command")
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio, )
        if (response["transcription"] is None):
            response["success"] = False
            response["error"] = "No speech"
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["success"] = False
        response["error"] = "Unable to recognize speech"

    return response

#speech = LiveSpeech(lm=False, keyphrase='computer', kws_threshold=1e-50)
#for phrase in speech:
    #print("keyword said")

def toLowerCase(string):
    return string.lower()

while True:
    result = recognize_speech_from_mic(r,mic)
    print("Got result")
    print(result)
    if(result["success"]):
        try:
            parts = result["transcription"].split()
            parts = map(toLowerCase, parts)
            command, *parameters = parts
            print("Command", command)
            print("Parameters", parameters)
            if("quit" in command):
                print("quit")
                break
            elif("search" in command):
                print("search")
                browser.search(parameters)
            elif("select" in command):
                print("select")
                selectedNumber = parameters[1]
                try:
                    selectedNumber = int(selectedNumber)
                except ValueError:
                    selectedNumber = w2n.word_to_num(selectedNumber)
                if("poster" in parameters[0] or "show" in parameters[0]):
                    browser.selectPoster(selectedNumber)
                if("epi" in parameters[0]):
                    browser.selectEpisode(selectedNumber)
            elif("search" in command):
                print("search")
            else:
                print("Couldn't understand command")
        except:
            print("Error occured, say command again...")
            
    time.sleep(5)

