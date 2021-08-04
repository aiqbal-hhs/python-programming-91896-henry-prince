import os
import json


with open("pizza.json") as plist:
    selection = json.loads(plist.read())

Pizzas = selection['Ranges']
Options = selection['Options']
extras = selection['Extras']
Price = 0
Choice = ''

n = 0
s = ''
prompt = ''
Correct = ''
direct = ''

def NumError():
    global n
    global direct
    while True:
        try:
            n = float(input(prompt))
            if n <= 0:
                print('number had to be positive')
                NumError()
            if n >= 9999999999:
                print('That is too much, try again')
            direct = 2
            correct()
            break
        except ValueError or TypeError:
            print('Thats not a number! Try again')


def StrError():
    global s
    global direct
    while True:
        try:
            s = str(input(prompt))
            direct = 1
            correct()
            break
        except KeyError:
            print('Theres invalid characters in there!')


def correct():
    global s
    Correct = ''
    while True:
        Correct = str(input('Please check if this information correct? (y/n) '))
        if Correct in ('y', 'n'):
            if Correct == 'y':
                return
            else:
                if direct == 1:
                    StrError()
                else:
                    NumError()
        else:
            print('Invalid input')
            continue

def delivery():
    global prompt
    prompt = ('What is the first name? ')
    StrError()
    FirstName = s
    prompt = ('What is the last name? ')
    StrError()
    LastName = s
    prompt = ('What is the address? ')
    StrError()
    Address = s
    prompt = 'Whats the phone number? '
    NumError()
    PhoneNumber = int(n)
    print('\nFirst name: ', FirstName, '\nLast name: ', LastName, '\nAddress: ', Address, '\nPhone number: ', PhoneNumber)
    ContactInfo = {
        "Name" : (FirstName, LastName),
        "Address" : Address,
        "PhoneNumber" : PhoneNumber
        }
def pickup():
    global prompt
    prompt = ('What is the first name? ')
    StrError()
    FirstName = s
    prompt = ('What is the last name? ')
    StrError()
    LastName = s
    print('\nFirst name: ', FirstName, '\nLast name: ', LastName)
    ContactInfo = {
        "Name" : (FirstName, LastName)
        }

while True:
    Collect = str(input('Would you like deliverly or pickup? '))
    Collect = Collect.lower().strip().replace(' ', '')
    if Collect == 'delivery':
        Price += 3
        delivery()
    elif Collect == 'pickup':
        pickup()
    else:
        print('that is not an option')
    if Collect in ('delivery', 'pickup'):
        break


while True:
    Range = str(input('What range would you like? (Big New Yorker, Favorites, Deluxe, Classic Value) '))
    Range = Range.lower().title().strip().replace(' ', '')
    for item in selection:
        if item in ['Ranges']:
    
    #LEFT OFF FROM HERE, NEED TO PRINT OFF LIST OF PIZZAS


#                Choice = str(input('What pizza would you like? '))
#                Choice = Choice.lower().title().strip().replace("Bbq", "BBQ").replace("And", "&")
#                if Choice in Range:
#                    
#                    Size = str(input('What size would you like?\nSnack, Large, Extra Large\n'))
#                    Size = Size.lower().title().strip()
#                    if Size in Crust or "Large":
#                        print('cum')
#                    if Size == 'Large':
#                        print("cum")
#                    if Size in Crust:
#                            Crust = str(input('What crust would you like?\nPan, San Fransisco Style, Thin'"'"'n'"'"'Crispy, Mozzarella Stuffed Crust, Cheesy Garlic Stuffed Crust\n'))
#                            Crust = Crust.lower().title().strip()
#                elif Choice not in Range:
#                    print("\nThat is not an option, please select again.\n")
#        else:
#            print('That is not a range, try again!')
#            continue
#    OrderData = {
#        "pizzas" : pizza,
#    }
#    json_order = json.dumps(OrderData, indent = 4)
#    with open("order.json", "w") as order:
#        order.write(json_order)

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
