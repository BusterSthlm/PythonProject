from tkinter import messagebox, simpledialog

# KONSTANT SKRIVA MED STORA BOKSTÄVER

# input
hours_string = simpledialog.askfloat("hours","how many hours did you work?")
hourly_pay_rate = simpledialog.askfloat("hours","how many hourly you pay rate?")

# Konvertera användarens input till float.
hours_worked = float(input("How many hours did  you work?"))
hourly_pay_rate = float(input("what is your hourly payrate?"))
grosspay = hours_worked * hourly_pay_rate
print("your paymnent is", grosspay)
print(f"your payment{grosspay: .2f}")
# Konvertera int till str
hours_worked = int(hours_string)


payment = float(hourly_pay_rate)
# Process gör en beräkning
# Operatorn opererar de olike variablerna.
pay = hours_worked * payment

# Visa betalning

messagebox.showinfo(F"Your payment wil be: {pay:.2f} based on the hours worked which was {hours_worked} and with the payrate of {pay:.2f}")
messagebox.showinfo(F"Your payment wil be: {pay:.2f}", f"based on the hours worked which was {hours_worked} and with the payrate of {pay:.2f}")
#Meddelande


