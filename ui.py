import customtkinter
import ddd
from PIL import Image

def button_callback():
    print("УДАР")
    textbox.delete("0.0", end)
    textbox.insert("0.0", ddd.main())

app = customtkinter.CTk()
app.geometry("400x150")

button_image = customtkinter.CTKImage(Image.open("microphone.png"), size = (26,26))

button = customtkinter.CTkButton(app, text="бити", command=button_callback)
button.pack(padx=20, pady=20)

textbox = customtkinter.CTkTextbox(app)
textbox.insert("0.0","")
textbox.pack(padx = 20, pady = 20)

app.mainloop()