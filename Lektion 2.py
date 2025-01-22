from tkinter import messagebox, simpledialog

# KONSTANT SKRIVA MED STORA BOKSTÄVER


# input
#hours_string = simpledialog.askfloat("hours","how many hours did you work?")
#hourly_pay_rate = simpledialog.askfloat("hours","how many hourly you pay rate?")
keep_going = True

while (keep_going):
    hours = simpledialog.askfloat("hours", "how many hours?")
    payrate = simpledialog.askfloat("payment", "what is your hourly payrate")

    pay = hours*payrate

    #message
    message =f" your payment will be {pay:.2f} based on the hours worked which was {hours} and the payrate if {payrate}"
    messagebox.showinfo(f"your payment {pay:.2f}", message)


    keep_going=messagebox.askyesno("continue", "do you want to continue?")









