from tkinter import*
import wikipedia

root=Tk()
# root.title('who wants to be a millionaire')
root.geometry('800x500')
root.configure(background='black')

textfied=Entry(root,width=50,text='enter summary')
textfied.pack()

def search():
    mylabel=Label(root,text=wikipedia.summary(textfied.get))
    mylabel.pack()
mybutton=Button(root,text='search imformaton',command=search)
mybutton.pack()


root.mainloop()