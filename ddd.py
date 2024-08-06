import GPT
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
        else:
            print("Я Вас не розумію. Повторіть Ваш запит")
        return False
    
def process_voice_command(text):
        if "привіт" in text.lower():
            print("Привіт! Як я можу вам допомогти")
        elif "Як справи" in text.lower():
            print("Супер! А у вас")
        elif "калькулятор" in text.lower():
            subprocess.call(["calc"])
        elif "хром"in text.lower():
            subprocess.call(["розташування вашого файлу"])
        elif "джарвіс" in text.lower():
            resalt = GPT.ganarate(text)
            print(resalt)
        elif "код" in text.lower():
            code = GPT.generate(text)
            with open("generated_code.py", "w", encoding = "utf-8") as file:
                file.write(code)
            return True  
                    
def main():
        end_program = False
        while not end_program:
            audio = capture_voice_input()
            text = convert_to_text(audio)
            
                
        end_program = process_voice_command(text)
 
if __name__ == '__main__':
    main()