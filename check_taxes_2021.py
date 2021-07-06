import time
import inquirer
from inquirer.themes import GreenPassion

sleva_na_poplatnika = 27840
print ("Hello, today im gonna count your taxes for you.")

#loopinka aby nemohli dát jinej input než čísla
while True:
    try:
        gainz = int(input("How much money did you make last year? "))
    except ValueError:
        print("Please enter numbers.")
        continue
    else:break
# ještě jedna loopinka
while True:
    try:
        children = int(input("How many children do you have? if none type 0 please. "))
    except ValueError:
        print("Please enter numbers.")
        continue
    else: break

if children == 1:
    children = 15204
elif children == 2:
    children = 34608
#inquirer pro náklady
questions = [
    inquirer.List('expenses',
                message="How do you count your expenses?",
                choices=['40%', '60%', 'individually'],
                ),
]
answers = inquirer.prompt(questions)

#ifko pro dotazník záleží co si vyberou
if answers == {'expenses': '40%'}:
    naklady = (gainz * 0.40)
    zaklad_dane1 = gainz - naklady
elif answers == {'expenses': '60%'}:
    naklady = (gainz * 0.60)
    zaklad_dane1 = gainz - naklady
else:
    iexpenses = int(input("please count your expenses and type them in. "))
    zaklad_dane1 = gainz - iexpenses

#základ daně
print ("Your tax base is " + str(zaklad_dane1) + "Let's count your actual tax now .")
time.sleep(3)

# DPFO - slevy
#if na nevznik daňového bonusu při uplatňování pouze slevy na poplatníka
if zaklad_dane1 <= 27840:
    tax = (zaklad_dane1 * 0.15) - children
else:
    tax = (zaklad_dane1 * 0.15) - sleva_na_poplatnika - children

#if na zjištění daňového bonusu
if tax >= 1:
    print (" this is your tax to state " + str(tax) + " .")
elif tax == 0:
    print("You don't owe anything to state nor state to you.")
else:
    print("Your tax bonus is " + str(tax) + " .")
