from tkinter import *
from main import getResponse

class gui:
        
        def __init__(self):
            self.window = Tk()
            self._setup_main_window()
        
        def run(self):
            self.window.mainloop()
    
        def _setup_main_window(self):
            self.window.title("ChatBot")
            self.window.iconbitmap('icon.ico')
            self.window.resizable(width=False, height=False)
            self.window.configure(width=300, height=500, bg="#17202A")
        
            # head label
            head_label = Label(self.window, bg="#17202A", fg="#EAECEE",
                            text="Welcome :)", font="Arial 13 bold", pady=10)
            head_label.place(relwidth=1)
        
            # divider
            line = Label(self.window, width=450, bg="#ABB2B9")
            line.place(relwidth=1, rely=0.07, relheight=0.012)
        
            # text widget
            self.text_widget = Text(self.window, width=20, height=2, bg="#17202A", fg="#EAECEE",
                                font="Arial 14", padx=5, pady=5)
            self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
            self.text_widget.configure(cursor="arrow", state=DISABLED)
        
            # scroll tool
            scrollbar = Scrollbar(self.text_widget)
            scrollbar.place(relheight=1, relx=0.98)
            scrollbar.configure(command=self.text_widget.yview)
            
            # bottom label
            bottom_label = Label(self.window, bg="#ABB2B9", height=50)
            bottom_label.place(relwidth=1, rely=0.825)
        
            # message entry box
            self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg="#EAECEE", font="Arial 14")
            self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
            self.msg_entry.focus()
            self.msg_entry.bind("<Return>", self._on_pressed)
        
            # send button
            send_button = Button(bottom_label, text="Send", font="Arial 13 bold", width=20, bg="#ABB2B9",
                                 command=lambda: self._on_pressed(None))
            send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
        def _on_pressed(self, event):
            msg = self.msg_entry.get()
            self._insert_message(msg, "You")
        
        def _insert_message(self, msg, sender):
            if not msg:
                return
        
            self.msg_entry.delete(0, END)
            msg1 = f"{sender}: {msg}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg1)
            self.text_widget.configure(state=DISABLED)
        
            msg2 = f"Hi, How can I help you? :)\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg2)
            self.text_widget.configure(state=DISABLED)
        
            self.text_widget.see(END)
            
            
if __name__ == "__main__":
    app = gui()
    app.run()
    
