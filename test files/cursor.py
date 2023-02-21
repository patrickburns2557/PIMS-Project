from tkinter import *
  
# Create Object
root = Tk()
  
# Set geometry
root.geometry("200x530")
  
# List of cursors
cursors =[
        "arrow",
        "circle",
        "clock",
        "cross",
        "dotbox",
        "exchange",
        "fleur",
        "heart",
        "man",
        "mouse",
        "pirate",
        "plus",
        "shuttle",
        "sizing",
        "spider",
        "spraycan",
        "star",
        "target",
        "tcross",
        "trek"
]
  
  
  
# Iterate through all cursors
for cursor in cursors:
    Button(root,text=cursor,cursor=cursor, width=30, height=2).pack()
  
  
# Execute Tkinter
root.mainloop()