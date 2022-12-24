import pyqrcode
from pyqrcode import create
import tkinter as tk
from tkinter import * 
import png # pip install pypng 

def generate_qr():
    global qr_image
    qr_code = pyqrcode.create(text_box.get()) 
    qr_code = qr_code.xbm(scale=10)
    qr_image=tk.BitmapImage(data=qr_code)
    label.config(image=qr_image)
    
    
def save_qr():
    qr_code = pyqrcode.create(text_box.get()) 
    qr_code.png('qr_code.png', 
                scale=6, 
                module_color=[0, 0, 0, 128], 
                background=[0xff, 0xcc, 0xcc]
    )

    
if __name__ == "__main__":

    main_window = tk.Tk()
    main_window.geometry("1000x600")
    main_window.title("QR Code Generator")

    text_box=tk.Entry(main_window, font=25, width=40)
    text_box.grid(row=0, column=0, padx=8, pady=8)
    
    button=tk.Button(main_window, 
                     font=25, 
                     text="Generate and Show QR Code",
                     command=lambda:generate_qr()
    )
    button.grid(row=0, column=1, padx=8, pady=8)
    
    button2=tk.Button(main_window, 
                     font=25, 
                     text="Generate and Save QR Code",
                     command=lambda:save_qr()
    )
    button2.grid(row=0, column=3, padx=8, pady=8)

    label=tk.Label(main_window,text='')
    label.grid(row=1, column=0, columnspan=2)

    main_window.mainloop()

