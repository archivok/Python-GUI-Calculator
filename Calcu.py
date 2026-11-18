
import tkinter as tk

def val_input(event):
    if event.char.isdigit() or event.keysym in (
        "BackSpace", "Delete", "Left", "Right"
    ):
        return None
    return "break"


def button_click(value):
    global expression

    expression += str(value)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)


def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)


def calculate():
    global expression

    try:
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(tk.END, str(result))

        expression = str(result)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "ERROR")
        expression = ""


# Main Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Color Palette
MINT = "#98FF98"
SAGE = "#6B8E75"
DARK_GREEN = "#355E3B"
WHITE = "#FFFFFF"
CORAL = "#E88D8D"

root.configure(bg=MINT)

expression = ""

# Display
display = tk.Entry(
    root,
    font=("Arial", 24),
    bg=WHITE,
    fg=DARK_GREEN,
    insertbackground=DARK_GREEN,
    justify="right",
    bd=0,
    relief="flat"
)

display.pack(
    fill="x",
    padx=15,
    pady=20,
    ipady=20
)

# Prevent manual string input
display.bind("<KeyPress>", val_input)


# Button Layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    [".", "0", "=", "+"]
]

button_frame = tk.Frame(
    root,
    bg=MINT,
    highlightbackground=SAGE,
    highlightthickness=2
)

button_frame.pack(
    expand=True,
    fill="both",
    padx=10,
    pady=5
)


# Clear Button
clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 16, "bold"),
    bg=CORAL,
    fg=WHITE,
    bd=0,
    activebackground="#D97979",
    command=clear
)

clear_button.grid(
    row=0,
    column=0,
    columnspan=4,
    sticky="nsew",
    padx=4,
    pady=4
)


# Calculator Buttons
for row_index, row in enumerate(buttons, start=1):
    for col_index, value in enumerate(row):

        if value == "=":
            command = calculate
            color = DARK_GREEN
            text_color = WHITE

        elif value in ["+", "-", "*", "/"]:
            command = lambda v=value: button_click(v)
            color = SAGE
            text_color = WHITE

        else:
            command = lambda v=value: button_click(v)
            color = WHITE
            text_color = DARK_GREEN

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18, "bold"),
            bg=color,
            fg=text_color,
            bd=0,
            activebackground=MINT,
            command=command
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=4,
            pady=4
        )


# Grid Configuration
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)


root.mainloop()
