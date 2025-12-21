import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

def clear():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create window
window = tk.Tk()
window.title("Calculator")
window.configure(bg="violet")

# Entry field
entry = tk.Entry(window, width=20, font=("Arial", 24), borderwidth=2, relief="solid", bg="violet", fg="purple")
entry.grid(row=0, column=0, columnspan=4)

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Add buttons to window
row = 1
col = 0
for button in buttons:
    action = lambda x=button: click(x) if x not in ['=', 'C'] else None
    if button == '=':
        tk.Button(window, text=button, width=5, height=2, bg= "pink",fg="black", command=evaluate).grid(row=row, column=col)
    else:
        tk.Button(window, text=button, width=5, height=2,bg= "pink",fg="black", command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(window, text='C', width=22, height=2,bg= "pink",fg="black", command=clear).grid(row=5, column=0, columnspan=4)

# Run the app
window.mainloop()