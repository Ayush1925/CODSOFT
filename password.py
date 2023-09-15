from tkinter import *
import string
import random
import emoji
from tkinter import font
from tkinter import messagebox
import pyperclip
from PIL import Image, ImageTk

def password_generator():

  emojies = """\U0001F601\U0001F602\U0001F603\U0001F604\U0001F605\U0001F606\U0001F607\U0001F608\U0001F609\U0001F610
  \U0001F611\U0001F612\U0001F613\U0001F614\U0001F615\U0001F616\U0001F617\U0001F618\U0001F619\U0001F620\U0001F621\U0001F622
  \U0001F623\U0001F624\U0001F625\U0001F626\U0001F627\U0001F628\U0001F629\U0001F630\U0001F631\U0001F632\U0001F633\U0001F634
  \U0001F635\U0001F636\U0001F637\U0001F638\U0001F639\U0001F640\U0001F641\U0001F642\U0001F643\U0001F644\U0001F645\U0001F646
  \U0001F647\U0001F648\U0001F649\U0001F650
  """

  root = Tk()
  root.geometry("900x400")

  
  image = Image.open('password.png')
  image = image.convert("RGBA")
  opacity = 200
  transparent = Image.new("RGBA",image.size,(255,255,255,opacity))
  result = Image.blend(image,transparent,alpha=opacity/255)
  showImage = ImageTk.PhotoImage(result)

  showImagelabel = Label(root, image=showImage)
  showImagelabel.image = showImage
  showImagelabel.place(x=480, y=0)


  def Exit_window():
    root.quit()

  def reset_window():
     
     
     getpass.config(text="")
     getpass_label.config(text="")
     lenghtlabelEntry.delete(0,END)
     pass
     
  def generate_password():

    getpass.config(text="")

    length = lenghtlabelEntry.get().strip()
  
    characters = ""
    password = []

    if not length:
        messagebox.showerror("Wrong Length", "Enter a Valid Length (1 - 20)")
        return

    length = int(length)
    if length < 1:
      messagebox.showerror("Wrong Lenght","Enter A Valid Lenght (1 - 20)")
      return
    
    selected_button = passtype.get()
      

    if selected_button == "Alphabets Only":
      characters+=string.ascii_letters

    elif selected_button == "Digits Only":
       characters+=string.digits

    elif selected_button == "Alphanumericals":
       characters+=string.ascii_letters + string.digits
    
    elif selected_button == "Special Characters":
       characters+=string.punctuation

    elif selected_button == "Combination":
       characters+=string.ascii_letters + string.digits + string.punctuation

    elif selected_button == "Emoji Password":
       characters=emojies
      
    
    for i in range(length):
      randomchr = random.choice(characters)
      password.append(randomchr)
    pswd = ("".join(password))

    getpass_label.config(text="Generated Password Is:",font=('arial',13,'bold'))
    getpass.config(text=f'{pswd}',font=('arial',13,'bold'),fg="#FF1493")
    
    copy_clipbutton = Button(root,text="Copy To Clipboard",font=('arial',13,'bold'),
                             fg="black",bg="#BCEE68",activebackground="#CD950C")
    copy_clipbutton.place(x=500,y=160)

    copy_clipbutton.config(state=NORMAL,command=lambda:copyto_clip(pswd))

    def copyto_clip(password_to_copy):
      pyperclip.copy(password_to_copy)
      messagebox.showinfo("Successfull","Password Copied To Clipboard!")
 
  passtype = StringVar()
  passtype.set("None")

  title_font = ("Arial", 15, "bold")

  titlelabel = Label(root,text="CODSOFT PASSWORD GENERATOR",font=title_font,fg="red")
  titlelabel.place(x=80,y=30)

  lenghtlabel = Label(root,text="Enter Password Lenght",font=('arial',13,'bold'))
  lenghtlabel.place(x=20,y=100)

  lenghtlabelEntry = Entry(root,font=('arial',13,'bold'))
  lenghtlabelEntry.place(x=250,y=100)


  buttonstr = Radiobutton(root,width=15,height=2,text="Alphabets Only",font=('arial',12,'bold'),bg="#EED5B7",
                    activebackground="#DFFF00",variable=passtype,value="Alphabets Only")
  buttonstr.place(x=40,y=200)

  buttonint = Radiobutton(root,width=15,height=2,text="Digits Only",font=('arial',12,'bold'),bg="#EED5B7",
                    activebackground="#DFFF00",variable=passtype,value="Digits Only")
  buttonint.place(x=40,y=263)

  buttonintstr = Radiobutton(root,width=15,height=2,text="Alphanumericals",font=('arial',12,'bold'),bg="#EED5B7",
                    activebackground="#DFFF00",variable=passtype,value="Alphanumericals")
  buttonintstr.place(x=250,y=200)

  buttonsp = Radiobutton(root,width=15,height=2,text="Special Characters",font=('arial',12,'bold'),bg="#EED5B7",
                    activebackground="#DFFF00",variable=passtype,value="Special Characters")
  buttonsp.place(x=250,y=263)

  buttonevery = Radiobutton(root,width=15,height=2,text="Combination",font=('arial',12,'bold'),bg="#EED5B7",
                    activebackground="#DFFF00",variable=passtype,value="Combination")
  buttonevery.place(x=40,y=325)

  buttonemoji = Radiobutton(root,width=15,height=2,text="Emoji Password",font=('arial',12,'bold'),bg="#EED5B7",
                    activebackground="#DFFF00",variable=passtype,value="Emoji Password")
  buttonemoji.place(x=250,y=325)

  buttonexit = Button(root,width=15,height=2,text="Exit",font=('arial',12,'bold'),bg="#FF1493",
                    activebackground="#DFFF00",command=Exit_window)
  buttonexit.place(x=600,y=290)

  buttongenerate = Button(root,width=15,height=2,text="Generate Password",font=('arial',12,'bold'),bg="#FF1493",
                    activebackground="#DFFF00",command=generate_password)
  buttongenerate.place(x=500,y=220)

  buttonreset = Button(root,width=15,height=2,text="Reset",font=('arial',12,'bold'),bg="#FF1493",
                    activebackground="#DFFF00",command=reset_window)
  buttonreset.place(x=720,y=220)

  getpass_label = Label(root, text="", font=('arial', 13, 'bold'))
  getpass_label.place(x=500, y=95)

  getpass = Label(root, text="", font=('arial', 13, 'bold'), fg="#FF1493")
  getpass.place(x=500, y=130)

  copy_clip_button = Button(root, text="Copy To Clipboard", font=('arial', 13, 'bold'), fg="black",
                            bg="#BCEE68", activebackground="#CD950C")
  copy_clip_button.place(x=500, y=160)
  copy_clip_button.config(state=DISABLED)

  root.mainloop()


if __name__ == "__main__":
    password_generator()