import os
import json

with open("pizza.json") as plist:
    pizza = json.load(plist)
with open("order.json", "w") as order:
    json.load(order)


Pizzas = plist['Ranges']
Options = plist['Options']
extras = plist['Extras']
Price = 0
Choice = ''


OrderData = {
    "pizzas" : pizza,
}

n = 0
s = ''
prompt = ''
Correct = ''

def NumError():
    global n 
    while True:
        try:
            n = float(input(prompt))
            if n <= 0:
                print('number had to be positive')
                NumError()
            if n >= 9999999999:
                print('That is too much, try again')
            break
        except ValueError or TypeError:
            print('Thats not a number! Try again')

def StrError():
    global key
    global s
    while True:
        try:
            s = globals()[key]
            return()
        except KeyError:
            break

def correct():
    while True:
        Correct = str(input('Please check if this information correct? (y/n) '))
        if Correct in ('y', 'n'):
            break
        print('Invalid input')
    else:
        return()

print(pizza)

while True:
    Collect = str(input('Would you like deliverly or pickup? '))
    Collect = Collect.lower().strip().replace(' ', '')
    if Collect == 'delivery':
        Price += 3
        while Correct == '' or 'n' and True:
            FirstName = str(input('What is the first name? '))
            LastName = str(input('What is the last name? '))
            Address = str(input('What is the address? '))
            prompt = 'Whats the phone number? '
            NumError()
            PhoneNumber = int(n)
            print('\nFirst name: ', FirstName, '\nLast name: ', LastName, '\nAddress: ', Address, '\nPhone number: ', PhoneNumber)
            correct()
    elif Collect == 'pickup':
        while Correct == '' or 'n':
            FirstName = str(input('What is the first name? '))
            correct()
            LastName = str(input('What is the last name? '))
            correct()
            print('\nFirst name: ', FirstName, '\nLast name: ', LastName)
            break
    else:
        print('that is not an option')
    if Collect in ('delivery', 'pickup'):
        break


while True:
    Range = str(input('What range would you like? (Big New Yorker, Favorites, Deluxe, Classic Value)'))
    key = Range.lower().title().strip().replace(' ', '')
    StrError()
    Range = s
    if Range in Pizzas:
        while Choice != 'Done': 
            print("\nHere is the {} range:\n" .format(key), *Range, sep='\n')
            Choice = str(input('What pizza would you like? '))
            Choice = Choice.lower().title().strip().replace("Bbq", "BBQ").replace("And", "&")
            if Choice in Range:
                
                Size = str(input('What size would you like?\nSnack, Large, Extra Large\n'))
                Size = Size.lower().title().strip()
                if Size in Crust or Large:
                    Choices.append(Size)
                print(Choices)
                if Size == 'Large':
                    print(Choices)
                if Size in Crust:
                        Crust = str(input('What crust would you like?\nPan, San Fransisco Style, Thin'"'"'n'"'"'Crispy, Mozzarella Stuffed Crust, Cheesy Garlic Stuffed Crust\n'))
                        Crust = Crust.lower().title().strip()
                        Choices.append(Size)
            elif Choice not in Range:
                print("\nThat is not an option, please select again.\n")
    else:
        print('That is not a range, try again!')
#TODO
#fix error handling in {} = locals()[{}]


#import PySimpleGUI as sg

#layout = [ [sg.Text('cum')],
#           [sg.Text('cum?'), sg.InputText()],
#           [sg.Button('ok'), sg.Button('exit')] ]
#window = sg.Window('cum?', layout)

#while True:
#    event, values = window.read()
#    if event == sg.WIN_CLOSED or event == 'cancle':
#        break
#    print('CUM')

#window.close()
