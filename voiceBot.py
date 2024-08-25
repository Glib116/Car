import gpt
import speech_recognition as sr
import subprocess
import webbrowser
recognizer = sr.Recognizer()


def capture_voice_input():
    with sr.Microphone() as source:
        print('Слухаю...')
        audio = recognizer.listen(source)
    return audio

def convert_to_text(audio):
    try:
        text = recognizer.recognize_google(audio, language = 'uk-UK')

        print('Ви сказали:' + text)
    except sr.UnknownValueError:
        text = ''
        print('Sorry, I didn`t understand that')
    except sr.RequestError as e:
        text = ''
        print('Error; {0}'.format(e))
    return text

    
    
    

    
def process_voice_command(text):
        if "привіт" in text.lower():
            print("Привіт! Як я можу Вам допомогти?")
        elif "прощавай" in text.lower():
            print("До побачення! Гарного дня!")
            return True
        elif "Як справи" in text.lower():
            print("Супер! А у вас")
        elif "калькулятор" in text.lower():
            subprocess.call(["calc"])
        elif "хром"in text.lower():
            subprocess.call(["розташування вашого файлу"])
        elif "джарвіс" in text.lower():
            resalt = gpt.generate(text)
            print(resalt)
        elif "код" in text.lower():
            code = gpt.generate(text)
            with open("generated_code.py", "w", encoding = "utf-8") as file:
                file.write(code)
            return True  
            
        elif "код" in text.lower():
            code = gpt.generate(text)
            with open("generated_code.py", "w", encoding = "utf-8") as file:
                file.write(code)
        elif "логіка" in text.lower():
            webbrowser.open("https://learn.logikaschool.com/logika")
        elif "малювання" in text.lower():
            webbrowser.open("https://quickdraw.withgoogle.com/?locale=ru")
        elif "класрум" in text.lower():
            webbrowser.open("https://classroom.google.com/u/0/h?hl=ru")
        elif "анекдоти" in text.lower():
            webbrowser.open("https://etnosvit.com/uk/anekdoty_uk.html")
        elif "меми" in text.lower():
            webbrowser.open("https://www.pinterest.com/sofnxx/%D1%83%D0%BA%D1%80-%D0%BC%D0%B5%D0%BC%D0%B8-%D0%B9-%D0%BF%D1%96%D0%BA%D1%87%D1%96/")
        elif "молитва" in text.lower():
            webbrowser.open("https://www.bible-ru.org/powerful-prayer-in-times-of-difficulty.html?gad_source=1&gclid=EAIaIQobChMIuMya_-yPiAMVqJpoCR33ESQREAAYAiAAEgJsTPD_BwE")
        elif "youtube" in text.lower():
             webbrowser.open(f"https://www.youtube.com/results?search_query={text.lower()[7:]}")
        return True                  
def main():
        end_program = False
        while not end_program:
            audio = capture_voice_input()
            text = convert_to_text(audio)
            end_program = process_voice_command(text)
 
if __name__ == '__main__':
    main()