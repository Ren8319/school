import tkinter as tk
root = tk.Tk()
root.title("OMG")

mylabel = tk.Label(text="Hello World", fg="blue", font="96").pack()

def showMessage():
    tk.Label(text="ชื่อ: นายศรัณยพงศ์ เอกอัครพรพล\nชั้น: ม.5/8\n เลขที่: 20", fg="green", font="48").pack()
    
btn1 = tk.Button(root, text="Press Me!", command=showMessage).pack()

root.geometry("469x469")
root.mainloop()