from tkinter import *
import  math

project_root = Tk()

ammeter_reading2 = DoubleVar()
voltmeter_reading2 = DoubleVar()
wattmeter_reading2 = DoubleVar()

ammeter_reading = DoubleVar()
voltmeter_reading = DoubleVar()
wattmeter_reading = DoubleVar()

core_loss_resistance = DoubleVar()
core_loss_reactance = DoubleVar()
equivalent_resistance = DoubleVar()
equivalent_reactance = DoubleVar()
no_load_power_factor = DoubleVar()
sine_value = DoubleVar()
impedance = DoubleVar()


def open_circuit():
    global no_load_power_factor
    global core_loss_resistance
    global core_loss_reactance
    global sine_value
    no_load_power_factor.set((wattmeter_reading.get() / (ammeter_reading.get() * voltmeter_reading.get())))
    sine_value.set(math.sqrt(1 - (no_load_power_factor.get() * no_load_power_factor.get())))

    core_loss_reactance.set(voltmeter_reading.get() / (ammeter_reading.get() * sine_value.get()))
    core_loss_resistance.set(voltmeter_reading.get() / (ammeter_reading.get() * no_load_power_factor.get()))


def short_circuit():
    global equivalent_resistance
    global equivalent_reactance
    global impedance
    equivalent_resistance.set((wattmeter_reading2.get() / (ammeter_reading2.get() * ammeter_reading2.get())))
    impedance.set((wattmeter_reading2.get() / (ammeter_reading2.get() * voltmeter_reading2.get())))
    equivalent_reactance.set(math.sqrt((impedance.get() * impedance.get()) - (equivalent_resistance.get() * equivalent_resistance.get())))

def getvals():
    global ammeter_reading2
    global ammeter_reading
    global voltmeter_reading
    global voltmeter_reading2
    global wattmeter_reading
    global wattmeter_reading2
    ammeter_reading.get()
    voltmeter_reading.get()
    wattmeter_reading.get()
    ammeter_reading2.get()
    voltmeter_reading2.get()
    wattmeter_reading2.get()

def logic(event):
    getvals()
    open_circuit()
    short_circuit()
    a.config(text="Core Loss Resistance : {a}".format(a=core_loss_resistance.get()))
    b.config(text="Core Loss Reactance : {a}".format(a=core_loss_resistance.get()))
    c.config(text="Copper Loss Resistance : {a}".format(a=equivalent_resistance.get()))
    d.config(text="Copper Loss Reactance : {a}".format(a=equivalent_reactance.get()))
    e.config(text="No Load Power Factor : {a}".format(a=no_load_power_factor.get()))

project_root.geometry("900x800")
project_root.title("Electrical Machines Assignment 1")
main_frame = Frame(project_root)
main_frame.pack(fill="both")

intro = Label(main_frame,
              text="The program gives the equivalent \n circuit parameters for the given \n values of open circuit "
                   "and \n short circuit test.",
              font="alice 30 bold").grid(pady=20, padx=40)

oc_input_frame = Frame(main_frame)

Label(oc_input_frame, text="Open Circuit Test Readings", font="alice 15 bold").grid(row=1, column=2, pady=10)
Label(oc_input_frame, text="Ammeter Reading (Amperes)").grid(row=2, column=2)
Label(oc_input_frame, text="Voltmeter Reading (Volts)").grid(row=3, column=2)
Label(oc_input_frame, text="Wattmeter Reading (Watts)").grid(row=4, column=2)

ammeter_entry = Entry(oc_input_frame, textvariable=ammeter_reading).grid(row=2, column=3)
volmmeter_entry = Entry(oc_input_frame, textvariable=voltmeter_reading).grid(row=3, column=3)
wattmeter_entry = Entry(oc_input_frame, textvariable=wattmeter_reading).grid(row=4, column=3)

oc_input_frame.grid(padx=90, pady=25)

sc_input_frame = Frame(main_frame)

Label(sc_input_frame, text="Short Circuit Test Readings", font="alice 15 bold").grid(row=1, column=2, pady=10)
Label(sc_input_frame, text="Ammeter Reading (Amperes)").grid(row=2, column=2)
Label(sc_input_frame, text="Voltmeter Reading (Volts)").grid(row=3, column=2)
Label(sc_input_frame, text="Wattmeter Reading (Watts)").grid(row=4, column=2)

ammeter_entry2 = Entry(sc_input_frame, textvariable=ammeter_reading2).grid(row=2, column=3)
voltmeter_entry2 = Entry(sc_input_frame, textvariable=voltmeter_reading2).grid(row=3, column=3)
wattmeter_entry2 = Entry(sc_input_frame, textvariable=wattmeter_reading2).grid(row=4, column=3)

sc_input_frame.grid(padx=90, pady=25)

widget = Button(main_frame, background="lightblue", text="Get Parameters")
widget.grid(row=9, column=0)
widget.bind('<Button-1>', logic)

output_frame = Frame(main_frame)

a = Label(output_frame, text="Core Loss Resistance : {a}".format(a=core_loss_resistance.get()))
a.grid(row=2, column=2)
b = Label(output_frame, text="Core Loss Reactance : {a}".format(a=core_loss_resistance.get()))
b.grid(row=3, column=2)
c = Label(output_frame, text="Copper Loss Resistance : {a}".format(a=equivalent_resistance.get()))
c.grid(row=4, column=2)
d = Label(output_frame, text="Copper Loss Reactance : {a}".format(a=equivalent_reactance.get()))
d.grid(row=5, column=2)
e = Label(output_frame, text="No Load Power Factor : {a}".format(a=no_load_power_factor.get()))
e.grid(row=6, column=2)

output_frame.grid(padx=90, pady=25)


project_root.mainloop()
