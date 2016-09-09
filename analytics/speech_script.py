from ctypes import *

# Define our error handler type
ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

asound = cdll.LoadLibrary('libasound.so')

# Set error handler

import speech_recognition
import webbrowser
from urllib import quote
import csv
import pandas as pd

BING_API_KEY="b0b8be2625cd44a383c0229c32dd2372"
WIT_API_KEY="C7KCW2EC7YANHHBTWYH5WCY54SPFXGGT"
API_CLIENT_ACESS_TOKEN="2f0e15a44a4a46039ed87cfa479cf507"

recognizer = speech_recognition.Recognizer()

# In[ ]:
chrome_path = '/usr/bin/google-chrome %s'
data={}
# In[ ]:

def speak(text):
    print text
    # speech_engine.say(text)
    # speech_engine.runAndWait()


# In[ ]:

def listen():
    asound.snd_lib_error_set_handler(c_error_handler)
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # return recognizer.recognize_api(audio,client_access_token=API_CLIENT_ACESS_TOKEN)
        # return recognizer.recognize_wit(audio,key=WIT_API_KEY)
        # return recognizer.recognize_sphinx(audio)
        return recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio, Please repeat")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""

def search_google(query):
    new = 2 # not really necessary, may be default on most modern browsers
    base_url = "http://www.google.com/?#q="
    final_url = base_url + quote(query)
    webbrowser.get(chrome_path).open(final_url, new=new)

def load_data(data_path,var_name):
    data[var_name] = pd.read_csv(data_path)
    print "loading data...."
    print "No of rows in file: ",data[var_name].shape[0]
    print "No of columns in file: ",data[var_name].shape[1]
    print "This is how data looks like"
    print data[var_name].head(n=2)


# In[ ]:
def process_cmd(inp):
    print "processing command...\n"
    cmd_list = inp.split(); ## list of commands

    try:
        if(cmd_list[0]=="search"):
            query=str(''.join(cmd_list[1:]))
            search_google(query)

        if(cmd_list[0]=="open" and cmd_list[1]=="presentation"):
            bashCommand="xdg-open Recognition_DIH.pdf"
            import subprocess
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

        # if(cmd_list[0]=="open" and cmd_list[1] and cmd_list[2]=="into"):
        #     file_name = str(''.join(cmd_list[1]))+".csv"
        #     load_data(file_name,cmd_list[3])

        # if(cmd_list[0]=="plot" and cmd_list[1]=="scatter" and cmd_list[2] and cmd_list[3]=="and" and cmd_list[4] and cmd_list[5]=="of" and cmd_list[6]=="data" and cmd_list[7]):
        #     d=data[cmd_list[7]]
        #     import matplotlib.pyplot as plt
        #     x=d[cmd_list[2]]
        #     y=d[cmd_list[4]]
        #     plt.scatter(x, y)

        if(cmd_list[0]=="open" and cmd_list[1] and cmd_list[2]=="into"):
            file_name = str(''.join(cmd_list[1]))+".csv"
            load_data(file_name,cmd_list[3])

        if(cmd_list[0]=="plot" and cmd_list[1]=="scatter" and cmd_list[2] and cmd_list[3]=="and" and cmd_list[4] and cmd_list[5]=="of" and cmd_list[6]=="data" and cmd_list[7]):
            d=data[cmd_list[7]]
            import matplotlib.pyplot as plt
            x=d[cmd_list[2]]
            y=d[cmd_list[4]]
            plt.scatter(x, y)
    except:
        print "Not a possible command"

play=1
while(play):
    speak("Say something!")

    input1=listen()

    # try:
    if input1!='':
        speak("I heard you say " + input1)
        process_cmd(input1)    
    # except:
    #     pass




