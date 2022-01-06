from tkinter import *

tiles_calculation = Tk()
tiles_calculation.geometry("350x350")
tiles_calculation.title("tiles calculator")


def lb():
    total.delete(0, END)
    ans = int(customer_length_entry.get()) * int(customer_breath_entry.get())
    total.insert(0, ans)


def cost():
    total_cost.delete(0, END)
    ans = int(customer_cost_entry.get()) * (int(customer_length_entry.get()) * int(customer_breath_entry.get()))
    total_cost.insert(0, ans)


def clear():
    total.delete(0, END)
    customer_breath_entry.delete(0, END)
    customer_length_entry.delete(0, END)


# label

customer_name = Label(tiles_calculation, text="Customer Name : ").place(x=0, y=0)
customer_phone_number = Label(tiles_calculation, text="customer ph no : ").place( x = 0,y = 25)
para_one = Label(tiles_calculation, text="Area to cover ").place(x=0, y=50)
a = Label(tiles_calculation,
          text="-----------------------------------------------------------------------------------").place(x=0, y=75)
para_two = Label(tiles_calculation, text="Length of the area").place(x=0, y=100)
para_three = Label(tiles_calculation, text="Breath of the area").place(x=0, y=125)
para_four = Label(tiles_calculation, text="One sq feet cost").place(x=0, y=150)
para_five = Label(tiles_calculation, text="Total area ").place(x=0, y=215)
para_six = Label(tiles_calculation, text="Total tiles cost ").place(x=0, y=240)

# entry

customer_name_entry = Entry(tiles_calculation)
customer_name_entry.place(x=120, y=0)

customer_phone_entry = Entry(tiles_calculation)
customer_phone_entry.place(x=120, y=25)

customer_length_entry = Entry(tiles_calculation)
customer_length_entry.place(x=120, y=100)

customer_breath_entry = Entry(tiles_calculation)
customer_breath_entry.place(x=120, y=125)

customer_cost_entry = Entry(tiles_calculation)
customer_cost_entry.place(x=120, y=150)

total = Entry(tiles_calculation)
total.place(x=120, y=215)

total_cost = Entry(tiles_calculation)
total_cost.place(x=120, y=240)

# button


calculation_button_add = Button(tiles_calculation, text="total area", command=lb)
calculation_button_add.place(x=75, y=175)

calculation_button_cost = Button(tiles_calculation, text="total cost", command=cost)
calculation_button_cost.place(x=150, y=175)

calculation_button_clear = Button(tiles_calculation, text="clear", command=clear)
calculation_button_clear.place(x=250, y=175)

exit_button = Button(tiles_calculation, text="Exit", command=tiles_calculation.destroy)
exit_button.place(x=125, y=300)

tiles_calculation.mainloop()
