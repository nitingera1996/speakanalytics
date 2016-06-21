
# coding: utf-8

# In[ ]:

import speech_recognition
import webbrowser
from urllib import quote
import csv
import pandas as pd

BING_API_KEY="b0b8be2625cd44a383c0229c32dd2372"
WIT_API_KEY="C7KCW2EC7YANHHBTWYH5WCY54SPFXGGT"
API_CLIENT_ACESS_TOKEN="2f0e15a44a4a46039ed87cfa479cf507"

# In[ ]:

def speak(text):
    print text
    # speech_engine.say(text)
    # speech_engine.runAndWait()


# In[ ]:

def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # return recognizer.recognize_api(audio,client_access_token=API_CLIENT_ACESS_TOKEN)
        return recognizer.recognize_wit(audio,key=WIT_API_KEY)
        #return recognizer.recognize_google(audio)
        # or: return recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""



# In[ ]:

recognizer = speech_recognition.Recognizer()
    

# In[ ]:
chrome_path = '/usr/bin/google-chrome %s'
file_loc = '/home/arpit/speech_pro/data/'

# In[ ]:

def search_google(query):
    new = 2 # not really necessary, may be default on most modern browsers
    base_url = "http://www.google.com/?#q="
    final_url = base_url + quote(query)
    webbrowser.get(chrome_path).open(final_url, new=new)

def load_data(data_path):
    data = pd.read_csv(data_path)
    print "loading data...."
    print "No of rows in file: ",data.shape[0]
    print "No of columns in file: ",data.shape[1]
    print "This is how data looks like"
    print data.head(n=2)


# In[ ]:
def process_cmd(inp):
    print "processing command...\n"
    cmd_list = inp.split(); ## list of commands
    if(cmd_list[0]=="open" and cmd_list[1]=="file"):
        file_name = str(''.join(cmd_list[2:]))+".csv"
        file_path  = file_loc+file_name
        load_data(file_path)

    if(cmd_list[0]=="search"):
        query=str(''.join(cmd_list[1:]))
        search_google(query)

play=1
while(play):
    speak("Say something!")

    input1=listen()
    speak("I heard you say " + input1)

    try:
        print input1
        process_cmd(input1);
        # if input1[:4]=="open":
        #     url="http://"+input1[5:]+".com"
        #     print url
        #     webbrowser.get(chrome_path).open(url)
        # elif input1[:6]=="search":
        #     query=input1[7:]
        #     search_google(query)
        # elif input1[:5]=="close":
        #     play=0
            
    except:
        pass




