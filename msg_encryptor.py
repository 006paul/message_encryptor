import tkinter as tk
from tkinter import ttk

#design
BG_COLOR = "#1e1e2e"
CARD_COLOR = "#2a2a3e"
ACCENT_COLOR = "#7c3aed"
HOVER_COLOR = "#6d28d9"
TEXT_COLOR = "#e2e8f0"
RESULT_COLOR = "#10b981"

def _copy_to_clipboard():
    result_text = result_box.get("1.0", tk.END).strip()
    if result_text:
        app.clipboard_clear()
        app.clipboard_append(result_text)
        app.update()

def _encrypt():
    text = message.get("1.0", tk.END).strip()
    encrypted_text = ""
    for i in text:
        if i.isalpha():
            shift = 3
            if i.islower():
                encrypted_text += chr((ord(i) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(i) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += i
            
    result_box.config(state=tk.NORMAL)
    result_box.delete("1.0", tk.END)
    result_box.insert("1.0", encrypted_text)
    result_box.config(state=tk.DISABLED)

def _decrypt():
    text = message.get("1.0", tk.END).strip()
    decrypted_text = ""
    for i in text:
        if i.isalpha():
            shift = 3
            if i.islower():
                decrypted_text += chr((ord(i) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(i) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_text += i
            
    result_box.config(state=tk.NORMAL)
    result_box.delete("1.0", tk.END)
    result_box.insert("1.0", decrypted_text)
    result_box.config(state=tk.DISABLED)
    
    
app = tk.Tk()
app.title("Message Encryptor")
app.geometry("650x800")
app.config(bg=BG_COLOR)

header = tk.Frame(app, bg=BG_COLOR)
header.pack(pady=30)
tk.Label(header, text="🔐 Message Encryptor", font=("Segoe UI", 24, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack()
tk.Label(header, text="Your messages, fully secured.", font=("Segoe UI", 10), bg=BG_COLOR, fg="#94a3b8").pack()

input_frame = tk.Frame(app, bg=CARD_COLOR, padx=20, pady=20, highlightthickness=1, highlightbackground="#3b3b5c")
input_frame.pack(pady=20)

tk.Label(input_frame, text="INSERT MESSAGE:", font=("Segoe UI", 9, "bold"), bg=CARD_COLOR, fg="#94a3b8").pack(anchor="w")
message = tk.Text(input_frame, height=6, font=("Segoe UI", 11), bg="#13131f", fg=TEXT_COLOR, insertbackground="white", bd=0, padx=10, pady=10)
message.pack(fill="x", pady=(5, 0))

btn_frame = tk.Frame(app, bg=BG_COLOR)
btn_frame.pack(pady=25)

def _create_btn(frame, text, cmd, clr):
    btn = tk.Button(frame, text=text, font=("Segoe UI", 11, "bold"), bg=clr, fg="white", activebackground=HOVER_COLOR, activeforeground="white", bd=0, padx=25, pady=10, cursor="hand2", command=cmd)
    btn.original_color = clr
    btn.bind("<Enter>", lambda e: e.widget.config(bg=HOVER_COLOR))
    btn.bind("<Leave>", lambda e: e.widget.config(bg=e.widget.original_color))
    return btn

encrypt_btn = _create_btn(btn_frame, "Encrypt", _encrypt, ACCENT_COLOR)
encrypt_btn.pack(side="left", padx=10)
decrypt_btn = _create_btn(btn_frame, "Decrypt", _decrypt, "#334155")
decrypt_btn.pack(side="left", padx=10)


tk.Label(app, text="RESULT:", font=("Segoe UI", 9, "bold"), bg=BG_COLOR, fg="#94a3b8").pack(pady=(10, 0))
result_box = tk.Text(app, height=4, width=45, font=("Consolas", 16, "bold"), bg="#13131f", fg=RESULT_COLOR, padx=15, pady=15, bd=0)
result_box.pack(pady=10)

btn_frame2 =tk.Frame(app, bg=BG_COLOR)
btn_frame2.pack(pady=25)
copy_btn = _create_btn(btn_frame2, "Copy to clipboard", _copy_to_clipboard, "#334155")
copy_btn.pack(pady=10)

app.mainloop()