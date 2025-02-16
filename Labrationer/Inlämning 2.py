from calendar import month
from codecs import backslashreplace_errors
from tkinter import simpledialog, messagebox

#UPG 2
#upg 3



"""
Budget analysis 

Write a program that ask the user to enter the amount that he or she budgeted for this month. 
A loop should then promt the user to enter each of his or hers expenses for the month and keep a running of total. 
When the loop finishes, the program should display the amount that the user is over and under budget. 
"""
sum_total = 0 #kr
budget_condition = True

# 1 - Be användaren skriva in hens budget
budget = simpledialog.askfloat("Hej", "Skriv in din budget för månden")

while budget_condition:
    expenses = simpledialog.askfloat("Fråga", "Lägg till utgift här")
    # Om användaren trycker Avbryt eller inte skriver något → bryt loopen
    if expenses < 0:
        break
    else:
        if sum_total > budget:
            messagebox.showinfo("Budget", "Din budget sprack för den här månaden!")
        elif sum_total < budget:
            messagebox.showinfo("Budget", f"Grattis! Du ligger {budget - sum_total} kr under budgeten.")
        else:
            messagebox.showinfo("Budget", "Du höll budgeten precis!")

        messagebox.showinfo("Beräkning", f"Din budget var {budget} kr, och dina totala utgifter var {sum_total} kr.")

    sum_total += expenses  # Lägg till utgiften i summan

    # Fråga om användaren vill lägga till fler utgifter
    user_input = messagebox.askyesno("Fråga", "Har du fler utgifter du vill lägga till?")


    if not user_input:  # Om användaren trycker "Nej", bryt loopen
        break


#Uppgift 5
"""
Write a program that uses nested loops to collect data and calculate the avertage rainfall over a period of years. 
The program should first ask for the number of years. 
The outer loop will iterate once for each year. the inner loop will iterate twelve times for each month. 
Each 296 iterations of the inne loop will ask the uesrs for the inces of the railfor for that month.
After all iterations, the program should display the number of month, inches of rainfall and the average rainfall per month for that entire period 
"""

#samla all data in en array
rainfall_data = []

# Fråga användare antal år
question = (simpledialog.askinteger("Fråga", "Skriv antalet år du vill se cm regn för :"))

#loop
for year in range(question):
    for month in range (1, 13):
        cm_per_month = simpledialog.askinteger("Fråga", "Hur många cm har det regnat den här månaden?")
        rainfall_data.append(cm_per_month)
        # Om användaren trycker "Avbryt", bryt ur båda looparna
        if cm_per_month is None:
            messagebox.showinfo("Avslutat", "Datainsamling avbröts.")
            break
        else:
            break
            #Säkerställ att användaren inte anger negativa tal

    if cm_per_month < 0:
        messagebox.showwarning("Fel", "Nederbörd kan inte vara negativ. Försök igen.")
        continue  #Hoppar över denna iteration och frågar igen
    break

#Lagrar och Beräkna data
total_rainfall = sum(rainfall_data)
total_months = question * 12
avg_rainfall = total_rainfall / total_months

# Visar resultat
messagebox.showinfo("Resultat",
                    f"Totalt antal månader: {total_months}\n"
                    f"Total nederbörd: {total_rainfall} "
                    f"cm\n "
                    f"Genomsnittlig nederbörd per månad: {avg_rainfall:.2f} cm")