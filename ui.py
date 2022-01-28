
import tkinter
from tkinter import *
from tkinter import messagebox
import controllers
import logging

class Data:
    def __init__(self):
        self.files=None

    def setFiles(self,files):
        self.files=files

    def getFiles(self):
        return self.files


    def fetchFiles(self,search,all_file_box,pdf_file_box):
        try:
            files = controllers.getFiles(search.get())
            self.setFiles(files)
            self.fillList(files,all_file_box,pdf_file_box)
            logging.info('fetchFiles Successfully Executed')
            messagebox.showinfo('Success','Successfully Fetched Files')
            return files
        except FileNotFoundError as e:
            logging.error('FileNotFound - %s',search.get())
            messagebox.showerror('File Not Found Error','Make sure the path format is like C:\\Users\\...')
        except Exception as e:
            logging.error('Error - %s',e)
            messagebox.showerror('Error',e)


    def fillList(self,files,all_file_box,pdf_file_box):
        all_file_box.delete(0, END)
        pdf_file_box.delete(0, END)
        for i in range (len(files['all_files'])):
            all_file_box.insert(i + 1, files['all_files'][i])
            if(files['all_files'][i].endswith('.pdf')):
                pdf_file_box.insert(i+1,files['all_files'][i])

    def mergePDF(self):
        logging.info('Inside mergePDF')
        try:
            if (self.files is None or len(self.files['pdf_files']) == 0):
                logging.error('PDF Files are empty or null')
                messagebox.showerror('Error','No PDF Files to merge')
            else:
                if (len(self.files['pdf_files'])!=0):
                    controllers.mergePDF(self.files['path'],self.files['pdf_files'])
                    logging.info('Successfully executed mergePDF')
                    messagebox.showinfo('Success','Successfully merged PDF')
        except Exception as e:
            logging.error('Error - %s',e)
            messagebox.showerror('Error',e)


    def userInterface(self):

        root = Tk()
        root.geometry('800x500')

        # Row 1
        Label(root,text='Path').grid(column=1,row=1)
        search=tkinter.StringVar()
        Entry(root, textvariable=search,font= ('calibre',10,'bold'),width=48).grid(column=2,row=1)
        Button(root,text='Search',command=lambda : self.fetchFiles(search,all_file_box,pdf_file_box)).grid(column=3,row=1)
        Button(root,text='Quit',command=root.destroy).grid(column=5,row=1)
        #Row 2
        Label(root, text=" ALL FILES").grid(column=1,row=2, columnspan=2)
        Label(root, text=" PDF FILES").grid(column=3,row=2, columnspan=2)

        #Row 3

        all_file_box = Listbox(root, height=23,
                               width=40,
                               # bg="grey",
                               activestyle='dotbox',
                               font=('calibre',8)
                               )
        all_file_box.grid(column=1, row=3, columnspan=2)

        pdf_file_box = Listbox(root, height=23,
                               width=40,
                               # bg="grey",
                               activestyle='dotbox',
                               font=('calibre',8)
                               # fg="yellow"
                               )

        pdf_file_box.grid(column=3, row=3, columnspan=2)

        # Row 4

        Button(root,text='Merge',command=self.mergePDF).grid(column=3,row=4, columnspan=2)

        root.mainloop()


logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.DEBUG)
obj= Data();
obj.userInterface();