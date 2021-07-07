BigNewYorker = ['Big New Yorker', 'Big Margherita', 'Big BBQ Bacon', 'Big Triple Cheese']
Favourites = ['Roast Veggie & Caramelised Onion with Vegan Cheese', 'Margherita', 'Beef, Bacon & Caramelized Onion', 'Meat Lovers', 'Super Supreme', 'Loaded Pepperoni With Double Toppings', 'Loaded Hawaiian With Double Toppings', 'Triple Meat & Cheese', 'BBQ Beef & Onion', 'BBQ Bacon & Mushroom', 'Italian Lovers', 'Hot & Spicy Veggie', 'Veggie Lovers']
Deluxe = ['Hot Buffalo Fried Chicken', 'Hotter Buffalo Fried Chicken', 'Hottest Buffalo Fried chicken', 'Chicken Cranberry', 'Sticky Chicken with Honey Garlic', 'Peri Peri Chicken', 'Fried Chicken & Bacon Ranch', 'Garlic Shrimp Deluxe', 'Mega Meat Lovers', 'Apricot Chicken Deluxe', 'Chicken Deluxe', 'BBQ Chicken & Bacon Deluxe']
ClassicValue = ['Classic Cheese', 'Americano', 'Ham & Cheese', 'Classic Vege', 'Pepperoni', 'Hawaiian', 'Cheesy Garlic', 'Beef & Onion']
Size = ['Snack', 'Large', 'Extra Large']
Crust = ['Pan', 'San Fransisco Style', 'Thin''n''Crispy', 'Mozzarella Stuffed Crust', 'Cheesy Garlic Stuffed Crust', 'Gluten Free']
Base = ['Buffalo Sauce', 'Honey Garlic Sauce', 'Authentic Tomato', 'BBQ Sauce', 'No Sauce']
Cheese = ['Cheese', 'Extra Cheese', 'Vegan Cheese', 'No Cheese']
Sauce = ['Hot Chilli Drizzle', 'Buffalo Drizzle', 'BBQ Drizzle', 'Mayo Drizzle', 'Basil Drizzle', 'Honey Garlic', 'Peri Peri Drizzle', 'Aioli Drizzle', 'Apricot Drizzle', 'Ranch Drizzle']
MeatExtra = ['Pepperoni', 'Ham', 'Bacon', 'Beef', 'Chicken', 'Shrimp', 'Italian Sausage']
VegeExtra = ['Onion Rings', 'Pineapple', 'Tomato', 'Olives', 'Green Capsicum', 'Dried Red Capsicum', 'Jelepenos', 'Mushrooms', 'Red Onions']
Extra = ['Parmesan Cheese', 'Garlic Sprinkle', 'Lemon Pepper Sprinkle', 'Oregano', 'Chilli Flakes']
Pizzas = (BigNewYorker, Favourites, Deluxe, ClassicValue)
Order = []
Price = 0
Choice = ''
Choices = []

n = 0
s = ''

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
    while True:
        try:
            key
        except KeyError:
            print("That is not avalible, Try again!")
            break

        

prompt = ''

while True:
    Collect = str(input('Would you like deliverly or pickup? '))
    Collect = Collect.lower().strip().replace(' ', '')
    if Collect == 'delivery':
        Price += 3
        FirstName = str(input('What is the first name? '))
        LastName = str(input('What is the last name? '))
        Address = str(input('What is the address? '))
        prompt = 'Whats the phone number? '
        NumError()
        PhoneNumber = int(n)
        print('\nFirst name: ', FirstName, '\nLast name: ', LastName, '\nAddress: ', Address, '\nPhone number: ', PhoneNumber)
        while True:
            Correct = str(input('Is this information correct? (y/n) '))
            if Correct in ('y', 'n'):
                break
            print('Invalid input')
        if Correct == 'n':
            continue
        else:
            break
    elif Collect == 'pickup':
        FirstName = str(input('What is the first name? '))
        LastName = str(input('What is the last name? '))
        print('\nFirst name: ', FirstName, '\nLast name: ', LastName)
        while True:
            Correct = str(input('Is this information correct? (y/n) '))
            if Correct in ('y', 'n'):
                break
            print('Invalid input')
        if Correct == 'n':
            continue
        else:
            break
    else:
        print('that is not an option')
    if Collect in ('delivery', 'pickup'):
        break

while True:
    prompt = 'What range would you like? (Big New Yorker, Favorites, Deluxe, Classic Value)'
    Range = Range.lower().title().strip().replace(' ', '')
    StrError()
    Range = locals()[key]
    if Range in Pizzas:
        while Choice != 'Done': 
            print("\nHere is the deluxe range:\n", *Range, sep='\n')
            prompt = "\nWhat pizza would you like? "
            StrError()
            Choice = str(s)
            Choice = Choice.lower().title().strip()
            Choices.append(Choice)
            if Choice in Range:
                ChoiceSize = str(input('What size would you like?\nSnack, Large, Extra Large\n'))
                ChoiceSize = ChoiceSize.lower().title().strip()
                Choices.append(ChoiceSize)
                print(Choices)
                if ChoiceSize == 'Large':
                    ChoiceCrust = str(input('What crust would you like?\nPan, San Fransisco Style, Thin'"'"'n'"'"'Crispy, Mozzarella Stuffed Crust, Cheesy Garlic Stuffed Crust, Gluten Free\n'))
                    ChoiceCrust = ChoiceCrust.lower().title().strip()
                    Choices.append(ChoiceSize)
                    print(Choices)
    elif Range not in Pizzas:
        print('That is not an avalible range, try again')
        StrError()

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