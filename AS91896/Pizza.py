import os
import json


with open("pizza.json") as plist:
    selection = json.loads(plist.read())

with open('pizza.json') as pfind:
    Selection = json.load(pfind)


Price = 0
n = 0
s = ''
Prompt = ''
direct = ''
Rangeli = {}
Pizzali = {}
Pizzas = {}
Extrali = {}


def NumError(prompt):
    global direct
    while True:
        try:
            answer = float(input(prompt))
            if answer <= 0:
                print('number had to be positive')
                NumError(prompt)
            if answer >= 9999999999:
                print('That is too much, try again')
            else:
                direct = 2
                correct()
                return answer
        except ValueError:
            print('Thats not a number! Try again')


def StrError(prompt):
    global direct
    global Prompt
    while True:
        Prompt = prompt
        answer = str(input(prompt))
        for f in [int, float]:
            try:
                _ = f(answer)
            except:
                pass
            else:
                print('Input shouldnt be a number')
                StrError(Prompt)
        direct = 1
        correct()
        return answer


def correct():
    global Prompt
    Correct = ''
    while Correct == '':
        Correct = str(input('Please check if this information correct? (y/n) '))
        if Correct in ('y', 'n'):
            if Correct == 'y':
                return
            else:
                if direct == 1:
                    StrError(Prompt)
                else:
                    NumError(Prompt)
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
        "Name": (FirstName, LastName),
        "Address": Address,
        "PhoneNumber": PhoneNumber
        }


def pickup():
    FirstName = StrError('What is the first name? ')
    LastName = StrError('What is the last name? ')
    print('\nFirst name: ', FirstName, '\nLast name: ', LastName)
    ContactInfo = {
        "Name": (FirstName, LastName)
        }


def RangeSelect():
    Range = int(input('What range would you like? (1: Big New Yorker, 2: Favorites, 3: Deluxe, 4: Classic Value) '))
    Range -= 1
    n = 1
    if Range > -1 and Range <= len(selection["Ranges"]) - 1:
        _Range = Selection["Ranges"][Range]
        for _Pizza in _Range:
            for _Pizzaname in _Range[_Pizza]:
                for key, val in _Pizzaname.items():
                    if key == 'Pizza':
                        print("{}. {}" .format(n, val))
                        Rangeli[n] = val
                        n += 1
    else:
        print('That is not an option!')


def PSelect():
    global Pizza
    Pizza = NumError("What Pizza would you like? ")
    if Pizza in Rangeli:
        return Rangeli[Pizza]
    else:
        print("That is not an avalible pizza in the range")


def PAmmount():
    global Pizza
    global _Pizza
    _Pizza = Rangeli[Pizza]
    Pammount = NumError("How many {} pizzas would you like? (up to 5)".format(_Pizza))
    if Pammount <= 5:
        return Pammount
    elif Pammount > 5:
        print('That is too many!')
        PAmmount()


def PToppings():
    global _Pizza
    n = 1
    for _Topping in Selection["Extras"]:
        for key, val in _Topping.items():
            if key == "Name":
                print("{}. {}".format(n, val))
                Extrali[n] = val
                n += 1
    while True:
        Toppings = NumError('Which toppings would you like? (1-{}) '.format(n))
        if Toppings in Extrali:
            _Toppings = Extrali[Toppings]
            Pizzali["Toppings"] = _Toppings
            print(Pizzali)
            break
        else:
            print("That is not an avalible topping!")



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
        continue
    RangeSelect()
    PSelect()
    PAmmount()
    for Pammount in range:
        _Pizza = Rangeli[Pizza]
        Pizzali["Name"] = _Pizza
        continue
    PToppings()
        

#collects pizza type, ammount, seperates pizza into seperate list in Pizzali from ammount selected
#go through each and adds to price, goes onto next type of pizza repeat.
#create a function that takes the price and adds it to the total price.
#create a list of all pizzas
    


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
