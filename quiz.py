from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

user_responses = []


def welcome():
    global wel
    wel = Tk()
    wel.geometry("600x400")

    welcome_text = "Welcome\n to the CODSOFT \n Quiz Challenge! \n Click 'Start' button\n to start the Quiz. \n Choose your answer\n to move forward \n Enjoy \nthe Python Visual Treat"

    welcome_image = Image.open("welcomeImage.png")
    welcome_image = ImageTk.PhotoImage(welcome_image)
    welcome_image_label = Label(wel, image=welcome_image,text=welcome_text,font=('Mongolian Baiti',24,'bold'),fg='red')
    welcome_image_label.place(x=0, y=0)

    Label2 = Label(wel,text=welcome_text,font=('Arial',18,'bold'),fg="white",bg="black",height=10,width=20,bd=2)

    Label2.place(x=10,y=25)

    OptionButton7 = Button(wel,text="Start",font=('arial',18,'bold'),bg='black',fg='white',
                    bd=4,activebackground='red',cursor='hand2',width=7,height=1)
    OptionButton7.place(x=420,y=285)

    OptionButton7.bind('<Button-1>',welcome1)

    wel.mainloop()

def welcome1(event):
    b = event.widget
    value = b['text']
    print(value)
    if value == "Start":
        wel.destroy()
        start_quiz()   
    else:
        pass

def start_quiz():
    root = Tk()
    root.geometry("600x400")

    current_question = 0

    QuizImage = PhotoImage(file='QuizImage.png')

    Questions = [" Which State Has The Highest Literacy Rate In India",
                "  Look at this series: 7, 10, 8, 11, 9, 12, ... What number should come next?",
                "  Look at this series: 36, 34, 30, 28, 24, ... What number should come next?",
                "  Which team won the IPL 2023 title?",
                "  Which of the following is the capital of Arunachal Pradesh?"]

    FirstOption = ["Goa","10","22","MI","Panaji"]
    SecondOption = ["Kerala","11","12","CSK","Imphal"]
    ThirdOption = ["Mizoram","30","26","RCB","Dispur"]
    FourthOption = ["Manipur","15","13","KKR","Itanagar"]

    CorrectAnswers = ["Kerala","10","22","CSK","Itanagar"]

    result = 0

    def select(event):
        nonlocal result
        nonlocal current_question
        b = event.widget
        value = b['text']

        response = messagebox.askquestion("Confirmation", f"Are you sure you want to select '{value}' as your answer?")

        if response == "yes":

          user_responses.append(value)

          if value == CorrectAnswers[current_question]:
              result+=1
          current_question += 1
          
          if current_question < len(Questions):
              displayQuestion()
          else:
              
              show_result()

    def displayQuestion():
                
        QuestionsDisplay.delete(1.0, END)
        QuestionsDisplay.insert(END, Questions[current_question])

        OptionButton1.config(text=FirstOption[current_question])
        OptionButton2.config(text=SecondOption[current_question])
        OptionButton3.config(text=ThirdOption[current_question])
        OptionButton4.config(text=FourthOption[current_question])
        
    def show_result():

        root.destroy()
        global root1
        root1 = Tk()
        root1.geometry("600x400")
        root1.title('CODSOFT Project')
        root1.configure(bg='#EBEBEB')
        label11 = Label(root1,text=(f'You Scored \n{result} out of {len(Questions)}'),font=('arial','30','bold'),fg="red")
        label11.place(x=320,y=110)

        showImage = Image.open('Dora.png')
        showImage = ImageTk.PhotoImage(showImage)
        showImagelabel = Label(root1,image=showImage)
        showImagelabel.image = showImage
        showImagelabel.place(x=0,y=0)



        OptionButton4 = Button(root1,text="Try Again",font=('arial',18,'bold'),bg='#DA70D6',fg='black',
                    bd=4,activebackground='red',cursor='hand2',width=10,height=1,command=start1)
        OptionButton4.place(x=420,y=285)

        OptionButton5 = Button(root1,text="Check Answers",font=('arial',18,'bold'),bg='#DA70D6',fg='black',
                    bd=4,activebackground='red',cursor='hand2',width=15,height=1,command=status)
        OptionButton5.place(x=50,y=285)

        
    def start1():
        root1.destroy()
        start_quiz()

    def status():
        root1.destroy()
        check_status()

    def start2():
        new.destroy()
        start_quiz()

    def check_status():
        global new
        new = Tk()
        new.geometry("600x400")
        status_text = ""

        for i in range(len(Questions)):
            
          status_text += f'Q{i+1}: {Questions[i]}\n'
          status_text += f'Your Answer: {user_responses[i]}\n'
          status_text += f'Correct Answer: {CorrectAnswers[i]}\n\n'

        
        status_label = Label(new,text=status_text, font=('Arial', 12,'bold'), justify=LEFT,bg="#FFE4C4")
        status_label.pack(pady=0, padx=0)

        OptionButton4 = Button(new,text="Try Again",font=('arial',18,'bold'),bg='black',fg='white',
                    bd=4,activebackground='red',cursor='hand2',width=10,height=1,command=start2)
        OptionButton4.place(x=420,y=340)
              
    lable11 = Label(root,image=QuizImage)
    lable11.place(x=110,y=55)

    QuestionsDisplay = Text(lable11,width=19,height=4,bd=0,font=('arial',18,'bold'),wrap='word',bg='#F0F0F0')
    QuestionsDisplay.place(x=50,y=40)

    QuestionsDisplay.insert(END,Questions[0])

    OptionButton1 = Button(root,text=FirstOption[0],font=('arial',18,'bold'),bg='#DA70D6',fg='black',
                        bd=4,activebackground='red',cursor='hand2',width=7,height=1)
    OptionButton1.place(x=30,y=285)

    OptionButton2 = Button(root,text=SecondOption[0],font=('arial',18,'bold'),bg='#DA70D6',fg='black',
                        bd=4,activebackground='red',cursor='hand2',width=7,height=1)
    OptionButton2.place(x=160,y=285)

    OptionButton3 = Button(root,text=ThirdOption[0],font=('arial',18,'bold'),bg='#DA70D6',fg='black',
                        bd=4,activebackground='red',cursor='hand2',width=7,height=1)
    OptionButton3.place(x=290,y=285)

    OptionButton4 = Button(root,text=FourthOption[0],font=('arial',18,'bold'),bg='#DA70D6',fg='black',
                        bd=4,activebackground='red',cursor='hand2',width=7,height=1)
    OptionButton4.place(x=420,y=285)

    OptionButton1.bind('<Button-1>',select)
    OptionButton2.bind('<Button-1>',select)
    OptionButton3.bind('<Button-1>',select)
    OptionButton4.bind('<Button-1>',select)



    root.mainloop()

if __name__ == "__main__":
    welcome()
