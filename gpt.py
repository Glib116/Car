from groq import Groq
client = Groq(api_key="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",)
def generate(prompt):
    chat_complection = client.chat.complections.create(
        messages = [
        {
            "role": "user",
            "content":prompt,
            
        }
    
        ],
        
            model = "llama3-8b-8192",
            
    )
    
    return chat_complection.choices[0].message.content

