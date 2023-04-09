import tkinter as tk
import PCcleanerBusinessLogic as pbl
import PCcleanerGuiFunctions as pblgui


bg = "#252525"
fg = "white"

root = tk.Tk()
root.geometry('400x250')
root.resizable(False, False)
root.title("PcCleaner")
root.config(bg=bg)
pblgui.dark_title_bar(root)

app_title = tk.Label(root, text="PcCleaner 3000", bg=bg, fg=fg, font=("Times New Roman", 15))
app_title.place(relx=0.5, rely=0.0, anchor=tk.N)

entry_description = tk.Label(root, text="File path:", bg=bg, fg=fg, font=("Times New Roman", 10))
entry_description.place(relx=0.01, rely=0.2, anchor=tk.W)

result_label = tk.Label(root, text="Hello", fg=fg, bg=bg, font=("MS Sans Serif", 8))
result_label.place(relx=0.5, rely=0.32, anchor=tk.CENTER)

entry_path = tk.Entry(root, width=50, borderwidth=3, bg='#505050', fg=fg)
entry_path.place(relx=0.95, rely=0.2, anchor=tk.E)

remove_button = tk.Button(root, text="Remove", bg='#505050', fg=fg, font=("MS Sans Serif", 15),
                          command=lambda: pbl.remove_something(result_label, entry_path.get()))
remove_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER, height=75, width=350)
pblgui.change_on_hover(remove_button, "#FFFFFF", "#505050")

root.mainloop()
