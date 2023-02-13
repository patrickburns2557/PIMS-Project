import tkinter as tk
import tkinter.ttk as ttk

top = tk.Tk()
x = " really long bit of text that may need to wrap\n"


list = tk.Listbox(top)
list.insert(1, "Python")
list.insert(2, "Perl")
list.insert(3, "C")
list.insert(4, "PHP")
list.insert(5, "JSP")
list.insert(6, "Ruby")

list.insert(7, x)



text = tk.Text(wrap=tk.WORD)
text.pack(expand=True, fill=tk.BOTH)

for i in range(100):
    text.insert(tk.END, (str(i) + x))



#list.pack(fill=tk.BOTH, expand=True)
top.mainloop()