import os
import json


with open("pizza.json") as plist:
    selection = json.loads(plist.read())

Pizzas = selection['Ranges']
Options = selection['Options']
extras = selection['Extras']
Price = 0
n = 0
s = ''
prompt = ''
direct = ''

def NumError(prompt):
    global direct
    while True:
        try:
            answer = float(input(prompt))
            if n <= 0:
                print('number had to be positive')
                NumError(prompt)
            if n >= 9999999999:
                print('That is too much, try again')
            else:
                direct = 2
                correct()
                return answer
        except ValueError:
            print('Thats not a number! Try again')


def StrError(prompt):
    global direct
    while True:
        answer = str(input(prompt))
        for f in [int, float]:
            try:
                _ = f(answer)
            except:
                pass
            else:
                print('Input shouldnt be a number')
                StrError()
        direct = 1
        correct()
        return answer

def correct():
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
    FirstName = StrError('What is the first name? ')
    LastName = StrError('What is the last name? ')
    Address = StrError('What is the address? ')
    PhoneNumber = NumError('Whats the phone number? ')
    print('\nFirst name: ', FirstName, '\nLast name: ', LastName, '\nAddress: ', Address, '\nPhone number: ', PhoneNumber)
    ContactInfo = {
        "Name" : (FirstName, LastName),
        "Address" : Address,
        "PhoneNumber" : PhoneNumber
        }
def pickup():
    FirstName = StrError('What is the first name? ')
    LastName = StrError('What is the last name? ')
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


with open('pizza.json') as pfind:
    Selection = json.load(pfind)

while True:
    Range = str(input('What range would you like? (Big New Yorker, Favorites, Deluxe, Classic Value) '))
    Range = Range.lower().title().strip().replace(' ', '')
    for Range in Selection:
        if Range in Selection['Ranges']:
            print('hello')
    else:
        print('That is not an option!')
        continue
    
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
