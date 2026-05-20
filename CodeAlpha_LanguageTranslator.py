from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# ----------------- WINDOW SETUP ----------------- #
root = Tk()
root.title("Language Translator")
root.geometry("650x550")
root.config(bg="#1e1e2e")  # Sleek dark mode background

languages = {
    "English": "en", "Hindi": "hi", "French": "fr", "German": "de", 
    "Spanish": "es", "Telugu": "te", "Tamil": "ta", "Japanese": "ja", 
    "Chinese": "zh-CN", "Korean": "ko", "Thai": "th"
}

# ----------------- TRANSLATE LOGIC ----------------- #
def translate_text():
    try:
        text = input_box.get("1.0", END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to translate!")
            return

        translated = GoogleTranslator(
            source=languages[source_lang.get()], 
            target=languages[target_lang.get()]
        ).translate(text)
        
        output_box.config(state=NORMAL)
        output_box.delete("1.0", END)
        output_box.insert(END, translated)
        output_box.config(state=DISABLED)  # Lock output box so users can't accidentally type in it
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ----------------- UI DESIGN ----------------- #
# Header Title
Label(root, text="🌍 LANGUAGE-TRANSLATOR", font=("Helvetica", 18, "bold"), bg="#1e1e2e", fg="#89b4fa").pack(pady=20)

# Dropdown Selection Frame
frame = Frame(root, bg="#1e1e2e")
frame.pack(pady=10)

Label(frame, text="From:", font=("Arial", 11, "bold"), bg="#1e1e2e", fg="#a6adc8").grid(row=0, column=0, padx=8)
source_lang = ttk.Combobox(frame, values=list(languages.keys()), width=15, state="readonly")
source_lang.grid(row=0, column=1, padx=5)
source_lang.set("English")

Label(frame, text=" જ⁀➴  To:", font=("Arial", 11, "bold"), bg="#1e1e2e", fg="#a6adc8").grid(row=0, column=2, padx=8)
target_lang = ttk.Combobox(frame, values=list(languages.keys()), width=15, state="readonly")
target_lang.grid(row=0, column=3, padx=5)
target_lang.set("Hindi")

# Input Box
Label(root, text="Enter Text:", font=("Arial", 11, "bold"), bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w", padx=55, pady=(10,2))
input_box = Text(root, height=6, width=65, font=("Arial", 11), bg="#313244", fg="#cdd6f4", bd=0, insertbackground="white", padx=10, pady=10)
input_box.pack()

# Clean Accent Translation Button
translate_btn = Button(root, text="TRANSLATE", font=("Helvetica", 11, "bold"), bg="#FFD1DC", fg="#11111b", activebackground="#94e2d5", cursor="hand2", bd=0, width=20, pady=8, command=translate_text)
translate_btn.pack(pady=20)

# Output Box
Label(root, text="Translated Text:", font=("Arial", 11, "bold"), bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w", padx=55, pady=(5,2))
output_box = Text(root, height=6, width=65, font=("Arial", 11), bg="#45475a", fg="#a6e3a1", bd=0, state=DISABLED, padx=10, pady=10)
output_box.pack()

root.mainloop()