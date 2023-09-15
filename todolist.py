from tkinter import *
from tkinter import messagebox



root = Tk()
root.geometry("500x400")
root.title("ToDo List")
root.configure(bg="#00FFFF")

task2 = StringVar()
getvalue = []

def add1():

  task = add_task.get()
  
  getvalue.append(task)
  task2.set(getvalue)
  listbox.insert(END,task)
  add_task.delete(0,END)
def delete():
  task = str(listbox.get(ANCHOR))
  listbox.delete(ANCHOR)

def on_item_double_click(event):
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task = getvalue[index]
        add_task.delete(0, 'end')
        add_task.insert(0, task)

def Edit():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = int(selected_task_index[0])
        updated_task = add_task.get()
        if updated_task:
            getvalue[index] = updated_task
            update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please enter an updated task!")
    else:
        messagebox.showwarning("Warning", "Please select a task to update!")

def update_task_listbox():
    listbox.delete(0, 'end')
    for task in getvalue:
        listbox.insert('end', task)
        add_task.delete(0,END)

label1 = Label(root,text="Add items into your TO-DO-LIST",bg="#FF7F50",font="label_font")
label1.place(x=10,y=10)

label1 = Label(root,bg="#BF3EFF",text="Select the row you want to change/Double click. Enter new data \nclick 'Update' button, if you want to change any items from the list",
               width=50)
label1.place(x=10,y=260)

label1 = Label(root,bg="#E3CF57",text="Select any row from the above To-Do-List and \nclick 'Delete' button, if you want to remove any items from the list",
               width=50)
label1.place(x=10,y=310)

add_task = Entry(root,font=15,bg="#FFF8DC")
add_task.place(x=15,y=50,height=30,width=400)

frame1 = Frame(root,bd=3,width=100,height=100)
frame1.pack(pady=(110,0))

listbox = Listbox(frame1,font=('arial',12),width=50,height=7,bg="#32405b",fg="white",cursor="hand2",selectbackground="red")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
listbox.bind('<Double-Button-1>', on_item_double_click)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

Button1 = Button(root,width=7,height=2,text="Add",command=add1,bg="green").place(x=420,y=40)

Button2 = Button(root,width=7,height=2,text="Update",command=Edit,bg="#FF1493").place(x=410,y=260)

Button2 = Button(root,width=7,height=2,text="Delete",command=delete,bg="#8B8878").place(x=410,y=310)





root.mainloop()