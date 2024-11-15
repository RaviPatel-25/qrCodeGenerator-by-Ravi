import qrcode
from tkinter import *

root = Tk() 

w=root.winfo_screenwidth()
h=root.winfo_screenheight()

root.overrideredirect(True)
root.geometry(str(w)+"x"+str(h)+"+0+0")
root.config(bg='white')
data = StringVar()

def makeqr(): 
	global data,root
	data = str(data.get())
	print(data)

	img = qrcode.make(data)
	img.save('/storage/emulated/0/QRcode/qr.jpg')
	root.destroy()
	root = Tk() 
	bg = PhotoImage(file = '/storage/emulated/0/QRcode/qr.jpg') 
	w=root.winfo_screenwidth()
	h=root.winfo_screenheight()
	
	root.overrideredirect(True)
	root.geometry(str(w)+"x"+str(h)+"+0+0")
	root.config(bg='white')
	
	label=Label(root, text='  Here is Your QRcode', bg='white',fg='black',font="times 15 bold")
	label.place(x=80, y=150)

	label1 = Label(root, image = bg) 
	label1.place(x = 300, y = 400) 
	root.mainloop()
	
label=Label(root, text='   QRcode Generator    ', bg='white',fg='red',font="times 15 bold")
label.place(x=80, y=150)

label=Label(root, text='Enter data or paste:- ', bg='white',fg='black',font="times 7 bold")
label.place(x=50, y=400)

entry1=Entry(root,textvariable=data)
entry1.place(x=500, y=400)

btn_paste=Button(root,text='Paste',bg='gray',bd=5,font=('Georgia',5,'bold'),command=lambda:entry1.event_generate("<<Paste>>"))
btn_paste.place(x=800,y=500,width=150)

makeqrbtn=Button(root,text='MakeQR',bg='yellow',bd=5,font=('Georgia',5,'bold'),command=makeqr)
makeqrbtn.place(x=380,y=800,width=300)

root.mainloop()