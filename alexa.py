import webbrowser
from time import ctime, localtime,sleep
import os
import playsound
from gtts import gTTS
import speech_recognition as sr
import threading
import random
import pyautogui
from bs4 import BeautifulSoup
import requests
from plyer import notification
import psutil
import subprocess
import re
import cv2
from datetime import datetime
import calendar
import csv

class VoiceAssistant:
    lang = ""
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.lang= "ar"
        self.mylang= "ar-EG"
    def record_audio(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            return audio

    def recognize_speech(self, audio):
        
        try:
            text = self.recognizer.recognize_google(audio, language=self.mylang)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an error processing your request.")
            return ""

    def speak(self, text):
        
        
        tts = gTTS(text=text, lang=self.lang, slow=False)
        audio_file = "audio.mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(text)
        os.remove(audio_file)

    def set_alexa_lang_en(self):
        self.lang = "en"
    def set_alexa_lang_ar(self):
        self.lang = "ar"
    def set_my_lang_en(self):
        self.mylang = "en-US"
    def set_my_lang_ar(self):
        self.mylang = "ar-EG"


def search_words_in_string(word_list, text):
    found_words = [word for word in word_list if word in text]
    return len(found_words) != 0

def respond(voice_data):
    # say my name
    if search_words_in_string(["my name","say my name","اسمى", "الاسم", "اسم"], voice_data):
        if alexa.lang == "ar":
            alexa.speak("مرحبا بك استاذ عبدالرحمن")
        elif alexa.lang == "en":
            alexa.speak("hey you are my devolper, Abdelrahman")
    # say her name
    if search_words_in_string(["your name","what is your name","انت تبقي ايه","اسمك ايه","انت مين", "انتى مين"], voice_data):
        if alexa.lang == "ar":
            alexa.speak("انا خددامتك اليكسا")
        elif alexa.lang == "en":
            alexa.speak("my name is alexa how can i help you")
        
    # clock
    if search_words_in_string(["the time","time","الوقت", "الساعة", "الساعه", "ساعه", "ساعة"], voice_data):
        time = ctime().split(" ")[-2]
        if alexa.lang == "ar":
            alexa.speak("الوقت الآن " + time)
        elif alexa.lang == "en":
            alexa.speak("the time now is "+ time)
    # date
    if search_words_in_string(["what day is today","the date","date","اليوم", "التاريخ", "النهارده", "يوم"], voice_data):
        if alexa.lang == "ar":
            alexa.speak("التاريخ اليوم هو " + ctime())
        elif alexa.lang == "en":
            alexa.speak("the date today is " + ctime())
        
    # discord
    if search_words_in_string(["discord","open discord","افتح ديسكورد", "ديسكورد", "الديسكورد", "افتح ديسك"], voice_data):
       subprocess.run(['discord'])
    # alexa talk english
    if search_words_in_string(["حول انجليزي","حول english",'اليكس حول انجلش',"حول انجلش","اليكسا حول انجلش","change your language to english","change your language english"], voice_data):
        alexa.set_alexa_lang_en() 
        print(alexa.lang)
    # alexa talk arabic
    if search_words_in_string(["change your language to arabic","حول عربي",'اليكس حول عربي',"اليكسا حول عربي","change your language arabic","change your language to arab"], voice_data):
        alexa.set_alexa_lang_ar() 
        print(alexa.lang)
    # change my language
    if search_words_in_string(['change my language','change language','اليكس حول لغتي',"حول لغتي","حول لغه","حول اللغه"], voice_data):
        if(alexa.mylang == "ar-EG"):
            alexa.set_my_lang_en() 
            print(alexa.mylang)
        elif(alexa.mylang == "en-US"):
            alexa.set_my_lang_ar() 
            print(alexa.mylang)
    # terminal
    if search_words_in_string(["terminal","open terminal","افتح ترمنال","ترمنا", "ترمنال", "ترمينال", "افتح ترمينال","term"], voice_data):
       subprocess.run(['gnome-terminal'])
    # whatsapp
    if search_words_in_string(["whatsapp","open whatsapp","افتح واتساب", "واتس", "افتح واتس", "افتح الواتساب"], voice_data):
       subprocess.run(['whatsdesk'])
    # telegram
    if search_words_in_string(["open telegram","telegram","افتح تيليجرام", "تلجرام", "تليجرام", "افتح تليجرام"], voice_data):
       subprocess.run(['telegram-desktop'])
    # google search
    if search_words_in_string(["search in google","search google","سرش ", "اعمل سيرش", "سيرش", "يلا سيرش"], voice_data):
       def google_search(query):
        
            encoded_query = query.replace(' ', '+')
            
            url = f'https://www.google.com/search?q={encoded_query}'
            
            webbrowser.open(url)

       if alexa.lang == "ar":
            alexa.speak("عايز تسيرش على ايه")
       elif alexa.lang == "en":
            alexa.speak("what do you want to search about")
       audio = alexa.record_audio()
       voice_data = alexa.recognize_speech(audio)
    #    user_query = input("Enter your search query: ")
       google_search(voice_data)

    # weather
    if search_words_in_string(["weather","weather today","الجو النهارده","الطقس","الطقس النهارده", " الجو النهارده عامل ايه", "درجة الحرارة ايه"], voice_data):
        headers = {
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) firefox/58.0.3029.110 Safari/537.3'}
        def weather(city):
            city = city.replace(" ", "+")
            res = requests.get(
                f'https://www.google.com/search?q={city}&oq={city}&aqs=firefox.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=firefox&ie=UTF-8', headers=headers)
            print("Searching...\n")
            soup = BeautifulSoup(res.text, 'html.parser')
            location = soup.select('#wob_loc')[0].getText().strip()
            time = soup.select('#wob_dts')[0].getText().strip()
            info = soup.select('#wob_dc')[0].getText().strip()
            weather = soup.select('#wob_tm')[0].getText().strip()
            alexa.speak(location)
            # alexa.speak(time)
            alexa.speak(info)
            alexa.speak(weather+"°C")
        weather("alexandria weather")
        print("Have a Nice Day:)")
    # battary
    if search_words_in_string(["battary percentage","battary","البطاريه","البطارية", "البطاريه كام", "فاضل كام في البطاريه"], voice_data):
        battery = psutil.sensors_battery()
        percent = battery.percent
        percent = int(percent)
        alexa.speak(str(percent))
        notification.notify(title="Battery Full",message="Battery is almost fully charged. You may disconnect the charger.",timeout=10)

    # google
    if search_words_in_string(["جوجل", "google"], voice_data):
        webbrowser.open('https://www.google.com')
    # calender
    if search_words_in_string(["التقويم", "كالندر","calendar","كاليندر"], voice_data):
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        alexa.speak(str(now.date()))
        print(calendar.month(year, month))
    # youtube
    if search_words_in_string(["يوتيوب","اليوتيوب", "youtube"], voice_data):
        webbrowser.open('https://www.youtube.com')
    # calculator
    if search_words_in_string(["افتح كالكولاتر","كلك","كالك", "كالكولاتر","calculator"], voice_data):
        subprocess.run(["gnome-calculator"])
    # facebook
    if search_words_in_string(["فيسبوك","الفيسبوك", "facebook"], voice_data):
        webbrowser.open('https://www.facebook.com')
    # linkedin
    if search_words_in_string(["لينكد","لينكد ان","لينكدن","افتح لينك دن", "لينك دين","linkedin", "linkdin"], voice_data):
        webbrowser.open('https://www.linkedin.com/feed/')
    # github
    if search_words_in_string(["جيت اب","جيت هاب","github", "افتح جيت هاب","افتح جيت هب","gethub","githab"], voice_data):
        webbrowser.open('https://github.com/')
    # chatgpt
    if search_words_in_string(["افتح شات جي بي تي","chatgpt", "شات جي بي","شادي بي تي","شادي بي","chat gbt","chat gbd","chat gpd","chatgbt"], voice_data):
        webbrowser.open('https://chatgpt.com/?model=auto')
    # camera
    if search_words_in_string(["حمل برنامج","حملي", "عايز احمل","download software","software"], voice_data):
        def open_ubuntu_software(app_name):
            
            command = f'gnome-software --search "{app_name}"'
            subprocess.run(command, shell=True)
            os.system("wmctrl -a 'Software'")
        app_name = input("Enter the name of the application: ").strip()
        open_ubuntu_software(app_name)
    # camera
    if search_words_in_string(["افتح الكاميرا","الكاميرا", "كاميرا","camera","open camera"], voice_data):
        subprocess.run(["kamoso"])
    # sound up
    if search_words_in_string(["علي الصوت","على الصوت", "علي","volume up","sound up"], voice_data):
        def increase_volume():
            # Increase the volume by 10%
            subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "15%+"])
        increase_volume()
        alexa.speak("عاليت الصوت")
        print("Volume increased.")
    # sound down
    if search_words_in_string(["وطي الصوت","وطى الصوت", "وطي","volume down","sound down"], voice_data):
        def decrease_volume():
            # Decrease the volume by 15%
            subprocess.run(["amixer", "-D", "pulse", "sset", "Master", "15%-"])
        decrease_volume()
        alexa.speak("وطيت الصوت")
        print("Volume decreased.")
    # search for file 
    if search_words_in_string(["دور فايل","دور علي فايل", "فايل","search file","search on file"], voice_data):
        def search_for_file(filename):
            
            search_command = f"find /home -name {filename}"
            result = subprocess.run(search_command, shell=True, capture_output=True, text=True)
            
            if result.stdout:
                return result.stdout.strip()  
            else:
                return "File not found."
            
        def get_filename_from_user():
            alexa.speak("عايز تسيرش على ايه")
            filename = pyautogui.prompt(text='Enter the filename to search for:', title='File Search', default='')
            if filename:
                return filename.strip()
            else:
                pyautogui.alert("No filename provided. Exiting...")
                exit()
        if __name__ == "__main__":
            
            filename = get_filename_from_user()

            # Search for the file
            search_result = search_for_file(filename)

            # Show the search result in an alert
            pyautogui.alert(f"Search result:\n{search_result}")

            
            pyautogui.hotkey('ctrl', 'alt', 't') 
            sleep(1)  
            pyautogui.typewrite(search_result, interval=0.05)  
            pyautogui.press('enter')

    # En ti AR
    if search_words_in_string(["كيبورد عربى","حول كيبورد عربي", "كيبورد عربي","keyboard arabic","keyboard to arabic","change keyboard to arabic"], voice_data):
        pyautogui.hotkey('win','\\')
        if alexa.lang == "ar":
            alexa.speak("تم التحويل للعربية")
        elif alexa.lang == "en":
            alexa.speak("the keyboard is arabic")
     # Ar ti EN
    if search_words_in_string(["كيبورد انجليزي","حول كيبورد انجليزي", "كيبورد انجلش","keyboard english","keyboard to english","change keyboard to english"], voice_data):
        pyautogui.hotkey('win','\\')
        if alexa.lang == "ar":
            alexa.speak("تم التحويل للنجليزية")
        elif alexa.lang == "en":
            alexa.speak("the keyboard is english")
    # open VS coed
    if search_words_in_string(["كود", "الكود", "code","vs code"], voice_data):
        os.system("code &")
    # todays matches
    if search_words_in_string(["ماتش النهارده","ماتشات", "ماتش", "match","matches"], voice_data):
        # Automatically get today's date in the format MM/DD/YYYY
        today = datetime.now().strftime("%m/%d/%Y")
        print(f"Fetching matches for today: {today}")

        page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={today}")

        def main(page):
            src = page.content
            soup = BeautifulSoup(src, "lxml")
            matches_details = []

            championchips = soup.find_all("div", {"class": "matchCard"})

            def get_match_info(championchips):
                championchip_title = championchips.contents[1].find('h2').text.strip()
                all_matches = championchips.contents[3].find_all("div", {"class": "liItem"})
                num_matches = len(all_matches)
                
                for i in range(num_matches):
                    # names
                    team_A = all_matches[i].find("div", {"class": "teamA"}).text.strip()
                    team_B = all_matches[i].find("div", {"class": "teamB"}).text.strip()
                    # score
                    match_result = all_matches[i].find("div", {"class": "MResult"}).find_all('span',{'class':'score'})
                    score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
                    # time 
                    match_time = all_matches[i].find('div', {'class': 'MResult'}).find('span',{'class':'time'}).text.strip()

                    matches_details.append({
                        "نوع البطولة": championchip_title,
                        "الفريق الاول": team_A,
                        "الفريق الثانى": team_B,
                        "ميعاد المباراة": match_time,
                        "النتيجة": score
                    })

            for i in range(len(championchips)):
                get_match_info(championchips[i])
            keys = matches_details[0].keys()
            # Print all matches details
            with open('/home/abdelrahman/del/lec5/Alexa/matches-detail.csv','w') as output_file :
                dict_Writer = csv.DictWriter(output_file,keys)
                dict_Writer.writeheader()
                dict_Writer.writerows(matches_details)
                print("file created")

        main(page)


        def minimize_window():
            
            pyautogui.hotkey('win', 'd')

        minimize_window()

        def open_file_explorer(folder_path):
            
            subprocess.Popen(['nautilus', folder_path])
            

        folder_path = "/home/abdelrahman/del/lec5/Alexa/"  
        open_file_explorer(folder_path)
        sleep(1)

        folder_location = None
        while folder_location is None :
            try:
                folder_location = pyautogui.locateOnScreen('1.png')
                
            
            except pyautogui.ImageNotFoundException:
                print("image not found")


        if folder_location:
                    
                    folder_x, folder_y = pyautogui.center(folder_location)

                    
                    pyautogui.moveTo(folder_x, folder_y, duration=0.5)

                    
                    pyautogui.doubleClick()
                    sleep(2)
                    try:
                            folder_location = pyautogui.locateOnScreen('2.png')
                
            
                    except pyautogui.ImageNotFoundException:
                            print("image not found")
        else:
                    print("Folder not found on the screen.")


        if folder_location:
                
                    folder_x, folder_y = pyautogui.center(folder_location)

                    
                    pyautogui.moveTo(folder_x, folder_y, duration=0.2)

                    
                    pyautogui.click()
        else:
                    print("Folder not found on the screen.")

    # shut down
    if search_words_in_string(["اقفل الجهاز", "اقفل جهاز","shutdown","shut down" , "turn off the laptop"], voice_data):
        subprocess.run([ "shutdown", "now"])
    # restart
    if search_words_in_string(["راستر الجهاز", "رستر", "راستر","restart the laptop","restart laptop"], voice_data):
        os.system("reboot")
    # download from youtube
    if search_words_in_string(["حمل فيديو", "حملى الفيديو دا", "حمل الفيديو","download from youtube","download a video","download the video"], voice_data):
        pyautogui.hotkey('win', 'd')
        pyautogui.hotkey('ctrl','alt','1')
    # exit alexa
    if search_words_in_string(["شكرا","شكرا اليكس شكرا","شكرا اليكس","شكرا اليكسا", "شكرا الكسا", "مش عايز حاجه خلاص","thank you","thanks","that is all","that's all"], voice_data):
        if alexa.lang == "ar":
            alexa.speak("العفو")
        elif alexa.lang == "en":
            alexa.speak("you are welcome")
        os.system("wmctrl -a 'Visual Studio Code'")
        sleep(1)
        pyautogui.hotkey('ctrl','`')
        pyautogui.hotkey('ctrl','c')
        


alexa = VoiceAssistant()



# ctimer = localtime().tm_hour
# if ctimer >= 6 and ctimer <=16 :

#     alexa.speak('صباح الخير')
# else:
#     alexa.speak('مساء الخير')
# while True:
#     audio = alexa.record_audio()
#     voice_data = alexa.recognize_speech(audio)
#     if voice_data:  # Ensure there's valid voice data
#         respond(voice_data.lower())
def func():
    while True:
        audio = alexa.record_audio()
        voice_data = alexa.recognize_speech(audio)
        if voice_data:  
            respond(voice_data.lower())

eng_list = ['انجليزي','انجلش','english']
ar_list = ['عربي' ,'العربي','arabic']
def my_language():
    if alexa.lang == "ar":
        alexa.speak('ما اللغة التي تريد التكلم بها')
    elif alexa.lang =="en":
        alexa.speak('what the language do you want to talk with')
    while True:
        audio = alexa.record_audio()
        voice_data = alexa.recognize_speech(audio)
        if voice_data in eng_list:
            alexa.set_my_lang_en() 
            print(alexa.mylang)
            func()
        elif voice_data in ar_list:
            alexa.set_my_lang_ar()  
            print(alexa.mylang)
            func()

# ('انجليزي'or 'انجلش' or "english")
def change_language():
    alexa.speak('ما اللغة التي تريد انن اكلمك بها')
    while True:
        audio = alexa.record_audio()
        voice_data = alexa.recognize_speech(audio)
        if voice_data in eng_list:
            alexa.set_alexa_lang_en() 
            print(alexa.lang)
            my_language()
        elif voice_data in ar_list:
            alexa.set_alexa_lang_ar()  
            print(alexa.lang)
            my_language()


# ('اليكسا' or 'اليكس' or 'اليكسيا')
alexa_list=['اليكسا','اليكس','اليكسيا']
while True:
    text = alexa.record_audio()
    voice_data = alexa.recognize_speech(text)
    ctimer = localtime().tm_hour
    if voice_data in alexa_list:
        if ctimer > 6 and ctimer < 16:
           alexa.speak('صباح الخير')
           sleep(1)
        #    func()
           change_language()
        else:
            alexa.speak('مساء الخير')
            sleep(1)
            change_language()
            # func()


