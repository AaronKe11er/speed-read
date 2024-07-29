from PyPDF2 import PdfReader
from tkinter import filedialog
from tkinter import filedialog
from time import sleep
from tkinter import *
import tkinter as tk
import os
import threading
from PIL import Image, ImageTk


class NeedForSpeed():
    def main_loop(self):
        self.pdf_grabber()
        self.remove_white_spaces()
        self.tkinter_block()

    def pdf_grabber(self):
        self.page_count = 25
        self.index = 0
        self.paused = False
        self.back = 0
        self.the_book = []
        reader = PdfReader(self.file)
        number_of_pages = len(reader.pages)
        five_pages = self.page_count + 5
        while self.page_count < five_pages:
            page = reader.pages[self.page_count]
            for x in page:
                text = page.extract_text()
                for words in text.split('\n'):
                    for i in words.split(' '):
                        # Looking for periods and spliting up words via end and start of a sentence. 
                        self.splice_array(i)
            # input('Current page is ' + str(self.page_count) + '. Press Enter key to continue...')
            self.page_count+=1 

    def splice_array(self, i):
        if '\t' in i:
            self.remove_tabs(i)
        # elif '.' in i:
        #     x = i.split('.')
        #     self.the_book.append(x[0])
        #     self.the_book.append(x[1])
        elif ',' in i:
            self.the_book.append(i)
        elif len(i) == 1 and i not in 'ai123456789':
            prev_word = self.the_book[len(self.the_book)-1]
            joined_word = prev_word+i
            self.the_book[len(self.the_book)-1] = joined_word
        elif '\n' in i:
            x = i.split('\n')
            self.the_book.append(x[0])
            self.the_book.append(x[1])
        elif len(i) == 1 and i.upper() == i and i not in '1234567890':
            next_word = self.the_book[len(self.the_book)+1]
            next_word+=1
        else:
            self.the_book.append(i)

    def remove_tabs(self, i):
        if '\t' in i:
            for x in i.split('\t'):
                self.the_book.append(x)

    def remove_white_spaces(self):
        for i in self.the_book:
            if i == ' ' or i == '':
                self.the_book.remove(i)

    def pause_book(self):
        global back
        global paused
        self.back = 0
        self.paused = not self.paused
        
    def back_book(self):
        global back
        self.back += 1
        self.index = self.index - 1

    def change_text(self):
        x = 350
        if self.paused:
            if len(self.the_book[self.index]) >= 7 and len(self.the_book[self.index]) < 12:
                x = 500
                self.label.configure(font=("futura", 70), text = self.the_book[self.index])
                print('Current Word: ' + str(self.index))
                print(self.the_book[self.index])
            elif len(self.the_book[self.index]) >= 12:
                x = 800
                self.label.configure(font=("futura", 70), text = self.the_book[self.index])
                print('Current Word: ' + str(self.index))
                print(self.the_book[self.index])
            else:
                self.label.configure(font=("futura", 70), text = self.the_book[self.index])
                print('Current Word: ' + str(self.index))
                print(self.the_book[self.index])
            self.index+=1
        else:
            if self.back != 0:
                self.label.configure(font=("futura", 70), text = self.the_book[self.index - self.back])
            sleep(0.1)
        self.label.after(x, self.change_text)

    def tkinter_block(self):
        root = Tk()
        root.geometry('900x400')
        mainContainer = Frame(root)
        self.label = Label(mainContainer, text="")
        self.label.configure(font=("futura", 30), text="Press play to start \nreading your book")
        self.label.pack(side=LEFT, ipadx=5, ipady=5)
        mainContainer.pack()
        self.label.after(1000, self.change_text)
        root.title(self.page_count)
        start_text = tk.StringVar()
        back_text = tk.StringVar()
        start_text.set("Play/Pause")
        back_text.set("Go Back")
        start_btn = tk.Button(root, text='Play/Pause', command=self.pause_book, font=("futura", 15), fg="black", height=2, width=10)
        back_btn = tk.Button(root, text='Go Back', command=self.back_book, font=("futura", 15), fg="black", height=2, width=10)
        back_btn.pack()
        start_btn.pack()
        root.mainloop()

    def pick_out_book(self):
        from tkinter import filedialog
        #setting up parent window
        root = Tk()
        self.file = 'Nothing selected'

        #function definition for opening file dialog
        def openf():
            path = old_path() 
            file = filedialog.askopenfilename(initialdir=path, title="select file")
            self.file=new_path(file)
            self.selected_book = tk.Label(root, text=self.file)

        def old_path():
            with open('path.txt', 'r') as file:
                line = file.read()
                path = line.split('\n')[0]
                print(path) 
                if os.path.exists(path):
                    return path
                else:
                    return '/'

        def new_path(path):
            with open('path.txt', 'r') as file:
                old_p = file.read().split('\n')[0]
                new_path = ''
                for i in path.split('/')[1:-1]:
                    new_path+='/'+i+'/'
                    print(new_path)
                if old_p != new_path:
                    file.close()
                    with open('path.txt', 'w') as file:
                        file.write(new_path)
                return path

        file_open = Button(root, text="Open file", command= openf)
        file_open.pack(pady=20)
        start_text = tk.StringVar()
        start_text.set("Play Book")
        start_btn = tk.Button(root, textvariable=start_text, command=threading.Thread(target=self.main_loop).start, font=("futura", 9), fg="black", height=2, width=5)
        start_btn.pack()
        self.selected_book = tk.Label(root, text=self.file)
        self.selected_book.pack()
        root.geometry("350x200")
        root.title("Select a Book")
        root.mainloop()


speedReader = NeedForSpeed().pick_out_book()
