from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts  = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#Listens for commands

def myComand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print('I am ready for your next command')
       r.pause_threshold = 1
       r.adjust_for_ambient_noise(source, duration = 1)
       audio = r.listen(source)

    try:
       command = r.reconize_google(audio)
       print('You said: ' + command + '/n')

    #loop back to continue to listen for commands
    except sr.UnknownValueError:
       assistant(myCommand())

    return command

#if statements for executing commnds
def assistant(command):
    if 'open Reddit python' in command:
        chrome_path = 'usr/bin/google-chrome'
        url = 'https://www.reddit.com/r/python'
        webbrowser.get(chrome_path).open(url)
    
    if 'what\'s up' in command:
        talkToMe('Chillin bro')

    if 'email' in command:
        talkToMe('who is the recipient')
        recipient = myCommand()

        if 'Haroon_greyhat' in recipient:
            talkToMe('what should I say')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gamil.com',587)

            #identify to server
            mail.echo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('usrename' , 'password')

            #send message
            mail.sendmail('PERSON NAME' , 'emailaddress@whatever.com' , content)

            #close connection
            mail.close()

            talkToMe('Email sent')

talkToMe('I am ready for your command')

while True:
    assistant(myCommand())
