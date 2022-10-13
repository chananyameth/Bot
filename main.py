from tkinter import *
from csv_data import rows


def take_input():
    text = input_text.get("1.0", "end").strip('\r\n')
    input_text.delete('1.0', END)
    return text


def print_output(text):
    menu['state'] = 'normal'
    menu.delete('1.0', END)

    for row in rows:
        for keyword in row[0].split(', '):
            if text in keyword:
                menu.insert(END, row[1])
                break
    menu['state'] = 'disabled'


def process_input():
    print_output(take_input())


def on_input_key_press(event):
    value = event.widget.get("1.0", "end-1c")
    if '\n' in value:
        process_input()


root = Tk()
root.geometry("600x600")
root.title("Chat bot")

headline = Label(text="Select item from the menu:")

menu = Text(root,
            state='disabled',
            )

input_text = Text(root,
                  height=1,
                  width=25,
                  bg="light yellow")
input_text.focus_set()
input_text.bind("<KeyPress>", on_input_key_press)

display = Button(root,
                 height=1,
                 width=20,
                 text="Ok",
                 command=process_input)

headline.pack()
menu.pack()
input_text.pack()
display.pack()

mainloop()
