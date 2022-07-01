import tkinter


def miles_to_km():
    miles=float(entry_box.get())
    km=miles * 1.609
    kilometer_results_label.config(text=str(km))
window = tkinter.Tk()
window.title("Miles to Kms converter")
window.config(padx=20,pady=20)

entry_box=tkinter.Entry(width=7)
entry_box.grid(column=1,row=0)

label_1=tkinter.Label(text="Miles")
label_1.grid(column=2,row=0)


label_2=tkinter.Label(text="is equal to")
label_2.grid(column=0,row=1)


kilometer_results_label=tkinter.Label(text="0")
kilometer_results_label.grid(column=1, row=1)


kilometer_label=tkinter.Label(text="Km")
kilometer_label.grid(column=2,row=1)


calc_button=tkinter.Button(text="Calculate",command=miles_to_km)
calc_button.grid(column=1,row=2)


window.mainloop()

















window.mainloop()