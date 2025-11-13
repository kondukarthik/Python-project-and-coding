import tkinter as tk

def submit_bt():
    print("Clicked Submit")

def result_action():
    wind = tk.Tk()
    wind.title("Application window")

    label1 = tk.Label(wind, text='label1')
    label1.grid(row=0, column=0, padx=10, pady=5)

    label2 = tk.Label(wind, text='label2')
    label2.grid(row=1, column=0, padx=10, pady=5)

    entry1 = tk.Entry(wind)
    entry1.grid(row=0, column=1, padx=10, pady=5)

    entry2 = tk.Entry(wind)
    entry2.grid(row=1, column=1, padx=10, pady=5)

    submit_button = tk.Button(wind, text='Submit', command=submit_bt)
    submit_button.grid(row=2, column=0, pady=10)

    reset_button = tk.Button(wind, text='Reset', command=result_action)
    reset_button.grid(row=2, column=1, pady=10)

    wind.mainloop()

result_action()
