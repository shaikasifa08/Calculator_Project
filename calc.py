
from tkinter import *

root = Tk()
root.title("Calculator")

# Center Window
window_width = 500
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Background Color
root.configure(bg="#2C3E50")

# Center Frame
frame = Frame(root, bg="#2C3E50")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Display
entry = Entry(
    frame,
    width=18,
    font=("Arial", 22),
    borderwidth=5,
    bg="lightyellow",
    fg="blue",
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Functions
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Button Style
btn_font = ("Arial", 14, "bold")
btn_bg = "#3498DB"
btn_fg = "white"

# Row 1
Button(frame, text="7", font=btn_font, bg=btn_bg, fg=btn_fg,
       width=5, height=2, command=lambda: button_click(7)).grid(row=1, column=0, padx=5, pady=5)

Button(frame, text="8", font=btn_font, bg=btn_bg, fg=btn_fg,
       width=5, height=2, command=lambda: button_click(8)).grid(row=1, column=1, padx=5, pady=5)

Button(frame, text="9", font=btn_font, bg=btn_bg, fg=btn_fg,
       width=5, height=2, command=lambda: button_click(9)).grid(row=1, column=2, padx=5, pady=5)

Button(frame, text="/", font=btn_font, bg="orange", fg="white",
       width=5, height=2, command=lambda: button_click("/")).grid(row=1, column=3, padx=5, pady=5)

# Row 2
Button(frame, text="4", font=btn_font, bg=btn_bg, fg=btn_fg,
       width=5, height=2, command=lambda: button_click(4)).grid(row=2, column=0, padx=5, pady=5)

Button(frame, text="5", font=btn_font, bg=btn_bg, fg=btn_fg,
       width=5, height=2, command=lambda: button_click(5)).grid(row=2, column=1, padx=5, pady=5)

Button(frame, text="6", font=btn_font, bg=btn_bg, fg=btn_fg,
       width=5, height=2, command=lambda: button_click(6)).grid(row=2, column=2, padx=5, pady=5)

Button(frame, text="*", font=btn_font, bg="orange", fg="white",
       width=5, height=2, command=lambda: button_click("*")).grid(row=2, column=3, padx=5, pady=5)

# Row 3
Button(frame, text="1", font=btn_font, bg=btn_bg, fg=btn_fg,
       width=5, height=2, command=lambda: button_click(1)).grid(row=3, column=0, padx=5, pady=5)

Button(frame, text="2", font=btn_font, bg=btn_bg, fg=btn_fg,
       width=5, height=2, command=lambda: button_click(2)).grid(row=3, column=1, padx=5, pady=5)

Button(frame, text="3", font=btn_font, bg=btn_bg, fg=btn_fg,
       width=5, height=2, command=lambda: button_click(3)).grid(row=3, column=2, padx=5, pady=5)

Button(frame, text="-", font=btn_font, bg="orange", fg="white",
       width=5, height=2, command=lambda: button_click("-")).grid(row=3, column=3, padx=5, pady=5)

# Row 4
Button(frame, text="0", font=btn_font, bg=btn_bg, fg=btn_fg,
       width=5, height=2, command=lambda: button_click(0)).grid(row=4, column=0, padx=5, pady=5)

Button(frame, text="C", font=btn_font, bg="red", fg="white",
       width=5, height=2, command=button_clear).grid(row=4, column=1, padx=5, pady=5)

Button(frame, text="=", font=btn_font, bg="green", fg="white",
       width=5, height=2, command=button_equal).grid(row=4, column=2, padx=5, pady=5)

Button(frame, text="+", font=btn_font, bg="orange", fg="white",
       width=5, height=2, command=lambda: button_click("+")).grid(row=4, column=3, padx=5, pady=5)

root.mainloop()