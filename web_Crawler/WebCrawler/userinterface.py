from tkinter import *
import os
import sendmail as sm
from PIL import Image,ImageTk

count = 0
def main():
    #root Frame
    root=Tk()
    #Frame specifications
    root.title('WebCrawler')
    root['bg'] = 'gray34'
    root.geometry("725x700")
    root.minsize(200,200)
    root.maxsize(1000 , 1000)

    #loading gif file
    info = Image.open('icons/spider.gif')
    frames = info.n_frames
    im2 = [PhotoImage(file='icons/spider.gif', format=f'gif -index {i}') for i in range(frames)]
    img2=Label(image="",bg='gray34',height=300,width=800)
    lab1=Label(root,text="Spider ", font=('Elephant',42),bg='grey34')
    photo3=PhotoImage(file='icons/computer.png')
    computer=Button(root, image=photo3, command=computer_crawl, fg='black', font='David',cursor='spider',bg='grey34')
    photo4=PhotoImage(file='icons/music.png')
    music=Button(root, image=photo4, command=music_crawl, fg='black', font='Helvetica 10 bold',cursor='spider',bg='grey34')
    photo5=PhotoImage(file='icons/cookicon.png')
    cook=Button(root, image=photo5, command=cook_crawl, fg='black', font='Helvetica 10 bold',cursor='spider',bg='grey34')
    ins=Label(root,text='Send mail',font='Stencil',bg='grey34')
    photo6=PhotoImage(file='icons/gmail.png')
    mails=Button(root,image=photo6,command=send_mail,fg='black',font='Helvetica 10 bold',cursor='spider',bg='grey34')
    l1=Label(root,text='Music Books',font='Vivaldi',bg='grey34')
    l2 = Label(root, text='cookery Books', font='Vivaldi',bg='grey34')
    l3 = Label(root, text='Computer Books', font='Vivaldi',bg='grey34')


    #Nested Function for displaying animation
    def animation(count):
        im = im2[count]
        img2.configure(image=im)
        count = count + 1
        if count == frames:
            count = 0
        root.after(50, lambda: animation(count))

    #placing the elements in the frame
    img2.pack()
    animation(count)
    lab1.place(x=250,y=290)
    l1.place(x=160,y=375)
    l2.place(x=320,y=375)
    l3.place(x=460,y=375)
    music.place(x=170,y=400)
    cook.place(x=320,y=400)
    computer.place(x=470,y=400)
    ins.place(x=320,y=520)
    mails.place(x=320,y=550)
    root.mainloop()

#Function for executing computer books crawler
def computer_crawl():
    cwd=os.getcwd()
    os.chdir(cwd+"\WebCrawler")
    #command to start the crawler
    os.system('scrapy crawl crawler')
    # changing the directory back to current working directory
    os.chdir(cwd)

#Function for executing music books crawler
def music_crawl():
    cwd = os.getcwd()
    os.chdir(cwd + "\WebCrawler")
    # command to start the crawler
    os.system('scrapy crawl music')
    # changing the directory back to current working directory
    os.chdir(cwd)

#functions for executing cookery books crawler
def cook_crawl():
    cwd = os.getcwd()
    os.chdir(cwd + "\WebCrawler")
    # command to start the crawler
    os.system('scrapy crawl cookbook')
    # changing the directory back to current working directory
    os.chdir(cwd)



#Function for sending  crawled details through mail
def send_mail():
    sm.send_mail()

#function for executing main function
if __name__ == "__main__":
    main()

