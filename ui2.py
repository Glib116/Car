import customtkinter
import voiceBot
from PIL import Image

def button_callback():
    print("button clicked")
    textbox.delete("0.0", "end")
    textbox.insert("0.0", voiceBot.main())

app = customtkinter.CTk()
app.geometry("400x150")



button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

textbox = customtkinter.CTkTextbox(app)
textbox.insert("0.0","")
textbox.pack(padx = 20, pady = 20)

app.mainloop()
