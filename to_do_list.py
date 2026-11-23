from customtkinter import *
import json 
import os

FILE_HAME = "to_do_list.json"

if os.path.exists(FILE_HAME):
    with open(FILE_HAME, "r", encoding="utf-8")  as file:
        todo_list = json.load(file)
else:
    todo_list = []

app = CTk()
app.title("TO DO LIST")
app.geometry("500x500")
app.resizable(False, False)

title_Label = CTkLabel(
    app,
    text= "MY TODO list",
    font= ("Arial", 20, "bold")
)

title_Label.pack(pady = 20)

entry = CTkEntry(
    app,
    placeholder_text= "Write new task, for ex. - read a book",
    width= 450,
    height= 40,
    font= ("Arial", 14)
)

entry.pack(pady = 10)

text_box = CTkTextbox(
    app,
    width= 450,
    height= 200,
    font= ("Arial", 14)
)

text_box.pack(pady = 10)

def update_display():
    text_box.delete("0.0", END)
    if not todo_list:
        text_box.insert("end", "There are no tasks\nYou can add the first one")
    else:
        for i, task in enumerate(todo_list, start=1):
            text_box.insert("end", f"{i}. {task}\n")

def add_task():
    new_task = entry.get().strip()
    if new_task:
        todo_list.append(new_task)
        entry.delete(0, END)
        with open(FILE_HAME, "w", encoding="utf-8") as file:
            json.dump(todo_list, file, ensure_ascii=False, indent=4)
            update_display()

def delete_last():
    if todo_list:
        todo_list.pop()
        with open(FILE_HAME, "w", encoding="utf-8") as file:
                   json.dump(todo_list, file, ensure_ascii=False, indent=4)
        update_display()           
def clear_all():
     if todo_list:
          todo_list.clear()
          with open(FILE_HAME, "w", encoding="utf-8") as file:
            json.dump(todo_list, file, ensure_ascii=False, indent=4)
          update_display()      
button_frame = CTkFrame(app)
button_frame.pack(pady = 10)

add_button = CTkButton(
    button_frame,
    text= "Add new tast",
    width= 150,
    command=add_task
)

add_button.pack(side = "left", padx = 10)

delete_button = CTkButton(
    button_frame,
    text= "Delete the last one",
    width= 150,
    command=delete_last
)
delete_button.pack(side = "left", padx = 10)

clear_button = CTkButton(
    app,
    text= "Claer all",
    width=  350,
    fg_color="red",
    hover_color="darkred",
    command=clear_all
)
clear_button.pack(padx = 15)

update_display()

app.mainloop()