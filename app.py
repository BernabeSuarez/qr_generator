from tkinter import *
from tkinter import ttk
import pyqrcodeng


# Creating a window with a title, icon, size, and background color.
root = Tk()
root.iconbitmap('icon.ico')
root.title("Generador de QR")
root.geometry("550x300")
root.resizable(False,False)
root.config(bg='Silver')
title=Label(root,text="Genera tu Qr", fg='MintCream')
title.config(bg='Silver')

title.config(font=('Arial',14))
title.grid(row=0,column=0)


# Creating a label and an entry box for each of the four data fields.
data1=Label(root, text='Ingresa el primer dato: ')
data1.grid(row=1,column=0)
data1.config(pady=10,padx=10,bg='Silver')
input_data1=Entry(root)
input_data1.grid(row=1,column=1,ipadx=30)

data2=Label(root, text='Ingresa el segundo dato: ')
data2.grid(row=2,column=0)
data2.config(pady=10,padx=10,bg='Silver')
input_data2=Entry(root)
input_data2.grid(row=2,column=1,ipadx=30)

data3=Label(root, text='Ingresa el tercer dato: ')
data3.grid(row=3,column=0)
data3.config(pady=10,padx=10,bg='Silver')
input_data3=Entry(root)
input_data3.grid(row=3,column=1,ipadx=30)

data4=Label(root, text='Ingresa el cuarto dato: ')
data4.grid(row=4,column=0)
data4.config(pady=10,padx=10,bg='Silver')
input_data4=Entry(root)
input_data4.grid(row=4,column=1,ipadx=30)

qr_name=Label(root, text='Nombre del Qr: ')
qr_name.grid(row=5,column=0)
qr_name.config(pady=10,padx=10,bg='Silver')
input_qr_name=Entry(root)
input_qr_name.grid(row=5,column=1,ipadx=30)



# Creating a list and a variable.
data= []
datos=None


"""
    It takes the data from the entry boxes and creates a QR code.
"""
def qr_gen():
    data.extend([input_data1.get(),input_data2.get(),input_data3.get(),input_data4.get()])
    datos = "\n".join(data)
    qr = pyqrcodeng.create(datos)
    qr.png(f'{input_qr_name.get()}.png', scale=6, module_color=(0, 0, 0), background=(255, 255, 255))
    

# Creating a button that will call the function qr_gen when clicked.
btn=ttk.Button(root,text="Generar",command=qr_gen)
btn.grid(row=7,column=4,pady=15, ipadx=30,ipady=10)

# A method that keeps the window open until the user closes it.
root.mainloop()
