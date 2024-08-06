from groq import Groq
client = Groq(api_key="Ваш API ключ",)
def ganarate(prompt):
    chat_complection = client.chat.complections.create(
        masseges = [
        {
            "role": "user",
            "content":prompt,
            
        }
    
        ],
        
            model = "llame3-8b-8192",
            
    )
    
    return chat_complection.choices[0].massege.content
    

