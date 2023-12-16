import speech_recognition as sr
from googletrans import Translator

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,7)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')
        # print('a')
        
    except:
        
        return ""
    
    query = str(query).lower()
    # print('returning query from listen ', query)
    return query

def TranslationHinToEng(Text):
    line = str(Text)

    tkk = "429490.24646915"
    # translate = Translator(service_urls=['translate.googleapis.com'],tkk=tkk)
    translate = Translator()
    result = translate.translate(line,dest='en')
    data = result.text
    print("")
    print(f"You : {data}")
    print("")
    return data

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

MicExecution()