import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=5, width=30)
T.grid(row = 0, column = 0)

def sendText():
    T.insert(tk.INSERT, "Just a text Widget\nin two lines\n")
    #T.mark_set("insert", "%d.%d" % (line + 1, column + 1))
btn = tk.Button(root, text = "Send", command = sendText)
btn.grid(row = 0, column = 1)
btn1 = tk.Button(root, text = "Send1", command = sendText)
btn1.grid(row = 0, column = 2)
tk.mainloop()