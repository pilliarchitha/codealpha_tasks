import tkinter as tk
def chatbot():
    user = entry.get().lower()
    if user == "hello":
        reply = "Hi!"

    elif user == "hi":
        reply = "Hello!"

    elif user == "how are you":
        reply = "I'm fine, thanks!"

    elif user == "bye":
        reply = "Goodbye!"

    else:
        reply = "I don't understand."

    chat.insert(tk.END, "You: " + user + "\n")
    chat.insert(tk.END, "chatBot: " + reply + "\n\n")
    entry.delete(0, tk.END)
window = tk.Tk()
window.title("Basic Chatbot")
window.geometry("500x500")
chat = tk.Text(window, height=20, width=50)
chat.pack()
entry = tk.Entry(window, width=30)
entry.pack(pady=15)
button = tk.Button(window, text="Send", command=chatbot)
button.pack()
window.mainloop()
