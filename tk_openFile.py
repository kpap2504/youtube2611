import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from kp_readFile import get_youtube_links

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('400x150')


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='C:/__KOSTAS-26-10',
        filetypes=filetypes)

    if filename:
        ent.delete(0, tk.END)
        ent.insert(tk.END, filename)

    showinfo(title='Selected File', message=filename)

def get_links(): 
    filename = ent.get()
    if filename:
        youtube_video_ids = get_youtube_links(filename)
        showinfo(title='YouTube Video IDs', message='\n'.join(youtube_video_ids))
    else:
        showinfo(title='Error', message='Please select a file first.')


# open button
open_button = ttk.Button(root, text='Open a File', command=select_file)
open_button.pack(expand=True, fill=tk.X, padx=10, pady=10)

ent = ttk.Entry(root, width=40)
ent.pack(expand=True, fill=tk.X, padx=10, pady=10)

get_button = ttk.Button(root, text='Get YouTube Links', command=get_links)
get_button.pack(expand=True, fill=tk.X, padx=10, pady=10)


# run the application
root.mainloop()
