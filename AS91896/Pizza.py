BigNewYorkerRange = ['Big New Yorker', 'Big Margherita', 'Big BBQ Bacon', 'Big Triple Cheese']
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
pizzas = [BigNewYorkerRange, Favourites, Deluxe, ClassicValue]

order = []

n = 0
s = ''

def NumError():
    global n 
    while True:
        try:
            n = int(input(prompt))
            if n <= 0:
                print('number had to be positive')
            NumError()
            if n >= 122:
                print('That is too much, try again')
            break
        except ValueError or TypeError:
            print('Thats not a number! Try again')
        

prompt = ''


pickup = str(input('Would you like deliverly or pickup? '))
pickup = pickup.lower().strip().replace(' ', '')

if pickup == 'pickup':

elif pickup == 'delivery':

else:
    print('that is not an option')











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