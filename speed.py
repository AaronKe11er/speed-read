from spellchecker import SpellChecker
from PyPDF2 import PdfReader
from time import sleep
from tkinter import *
import tkinter as tk
import os
import threading


class Need_For_Speed():
    def mainloop(self):
        self.pdf_grabber()
        self.remove_white_spaces()
        self.tkinter_block()

    def pdf_grabber(self):
        self.page_count = 25
        self.index = 0
        self.paused = 0
        self.back = 0
        self.the_book = []
        reader = PdfReader("/home/Aznable/Documents/Books/Building Microservices (Sam Newman) (z-lib.org).pdf")
        number_of_pages = len(reader.pages)
        tracker = 1
        five_pages = self.page_count + 5
        spell = SpellChecker()
        while self.page_count < five_pages:
            page = reader.pages[self.page_count]
            for x in page:
                text = page.extract_text()
                for words in text.split('\n'):
                    for i in words.split(' '):
                        # Looking for periods and spliting up words via end and start of a sentence. 
                        if '.' in i:
                            x = i.split('.')
                            self.the_book.append(x[0])
                            self.the_book.append(x[1])
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
                        self.remove_tabs(i)
                        tracker+=1
                        print('now page' + str(self.page_count))
            # input('Current page is ' + str(self.page_count) + '. Press Enter key to continue...')
            self.page_count+=1 

    def remove_tabs(self, i):
        if '\t' in i:
            breakpoint()
            self.the_book.remove(i)
            for x in i.split('\t'):
                self.the_book.append(x)

    def remove_white_spaces(self):
        for i in self.the_book:
            if i == ' ' or i == '':
                self.the_book.remove(i)

    def iono(self,the_book):
        bad_words = []
        for i in self.the_book:
            if spell[i] == 0 or len(i) == 1 and i not in '1234567890' or i.split(',') != [i] or i.split('?') != [i] or i.split('!') != [i] or i.split('.') != [i] or i.split('-') != [i]:
                breakpoint()
                pass
        breakpoint()

    def pause_book(self):
        global back
        global paused
        self.back = 0
        self.paused += 1
        
    def back_book(self):
        global back
        self.back += 1  
        self.index = self.index - 1
        print('checking: ' + str(self.index)) 
        print(self.the_book[self.index]) 

    def changeText(self):
        x = 350
        if self.paused % 2 == 0:
            if len(self.the_book[self.index]) >= 7 and len(self.the_book[self.index]) < 12:
                x = 800
                self.label.configure(font=("futura", 70), text = self.the_book[self.index])
                print('Current Word: ' + str(self.index))
                print(self.the_book[self.index])
            elif len(self.the_book[self.index]) >= 12:
                x = 1000
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
        self.label.after(x, self.changeText)

    def tkinter_block(self):
        root = Tk()
        root.geometry('900x400')
        mainContainer = Frame(root)
        self.label = Label(mainContainer, text="")
        self.label.configure(text="msg will change every sec")
        self.label.pack(side=LEFT, ipadx=5, ipady=5)
        mainContainer.pack()
        self.label.after(1000, self.changeText)
        root.title(self.page_count)
        start_text = tk.StringVar()
        back_text = tk.StringVar()
        start_text.set("Play/Pause")
        back_text.set("Go Back")
        start_btn = tk.Button(root, textvariable=start_text, command=self.pause_book, font=("futura", 15), fg="black", height=2, width=10)
        back_btn = tk.Button(root, textvariable=back_text, command=self.back_book, font=("futura", 15), fg="black", height=2, width=10)
        back_btn.pack()
        start_btn.pack()
        root.mainloop()


bearserkar = Need_For_Speed().mainloop()

