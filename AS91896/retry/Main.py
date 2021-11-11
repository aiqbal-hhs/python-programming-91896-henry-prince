from os import strerror


ordertotal = 0
toppingprice = 0
pizzaprice = 0
n = 0
s = ''
Prompt = ''
tpammount = 0
regular = {1:"Hawaian", 2:"Ham & Cheese", 3:"Pepperoni", 4:"Vegetarian", 5:"Cheese", 6:"Margareta",  7:"Cheesy Garlic"}
gourmet = {1:"Meat lovers", 2:"Vege Supreme", 3:"Chicken Deluxe", 4:"Triple Cheese", 5:"New Yorker"}
toppings = {1:"Pepperoni", 2:"Sausage", 3:"Bacon", 4:"Ham", 5:"Chicken", 6:"Mushrooms", 7:"Onions", 8:"Olives", 9:"Green Peppers", 10:"Pineapple", 11:"Spinach", 12:"Jalapenos", 13:"Banana Peppers"}
order = {}
Topping = {}
toppingli = []

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

#collects first name, last name, phone number, address and adds $3 to total when delivery is selected
def delivery():
    Price = 3
    FirstName = StrError('What is the first name? ')
    LastName = StrError('What is the last name? ')
    Address = StrError('What is the address? ')
    PhoneNumber = NumError('Whats the phone number? ')
    print('\nFirst name: ', FirstName, '\nLast name: ', LastName, '\nAddress: ', Address, '\nPhone number: ', PhoneNumber)


# Collects first and last name when pickup is selected
def pickup():
    FirstName = StrError('What is the first name? ')
    LastName = StrError('What is the last name? ')
    print('\nFirst name: ', FirstName, '\nLast name: ', LastName)


#sellect range
def Range():
    global pizzaprice
    global Range
    Range = input('\nPlease select a range: (1. Regular 2. Gourmet)? ')
    if Range == '1':
        Range = regular
        pizzaprice = 8.5
    elif Range == '2':
        Range = gourmet
        pizzaprice = 12.5
    else:
        print('Invalid input')
        Range()
    for n in range(len(Range)):
        print(n + 1, '- ', Range[n + 1])


def pizza():
    global Pizza
    pizza = NumError("\nWhat Pizza would you like? ")
    if pizza in Range:
        Pizza = Range[pizza]
        print('You have selected: ', Pizza)


def ammount():
    global tpammount
    pammount = NumError('How many pizzas would you like? ')
    pammount = int(pammount)
    if pammount > 1 and pammount <= 5 and tpammount <= 5:
        tpammount += pammount
        print('You have selected: ', pammount, Pizza, 'pizzas')
        n = 0
        for i in range(pammount):
            toppingprice = 0
            n += 1
            order[n] = Pizza
            print("test")
            topping_(n)
            print(order)
            Pricecalc(n)
        return
    if tpammount > 5 or pammount > 5:
        print('You have selected: ', pammount, Pizza, 'pizzas')
        print('You have exceeded the maximum amount of 5 pizzas, you can order up to', 5 - tpammount, 'more pizzas')
        ammount()
    else:
        print("You have given an invaid input, please try again\n")
        ammount()


def topping_(n):
    global toppingprice
    s = ''
    s = input('Would you like any extra toppings for pizza #' + str(n) + '? (y/n) ')
    if s == 'y':
        for i in range(len(toppings)):
            print(i + 1, '- ', toppings[i + 1])
        while True:
            topping = NumError('\nPlease select a topping you would like: ')
            topping = int(topping)
            if topping in toppings:
                toppingli.append(toppings[topping])
                toppingprice += 0.5
                s = input('Would you like any more toppings? (y/n) ')
                if s == 'y':
                    continue
                elif s == 'n':
                    order[n] += " with " + str(toppingli) + "\n"
                    return
                else:
                    print('Invalid input')
                    continue
            else:
                print('Invalid input')
                topping()
        print('You have selected: ', topping)
    elif s == 'n':
        return


def Pricecalc(n):
    global ordertotal
    order[n] += " Cost breakdown: \n Pizza:" + str(pizzaprice) + "\nToppings:" + str(toppingprice) + "\nTotal:" + str(pizzaprice + toppingprice) + "\n"
    pizzatotal = pizzaprice + toppingprice
    ordertotal += pizzatotal

    


# Main loop
while True:
    Collect = str(input('Would you like deliverly or pickup? '))
    Collect = Collect.lower().strip().replace(' ', '')
    if Collect == 'delivery':
        delivery()
    elif Collect == 'pickup':
        pickup()
    else:
        print('that is not an option')
        continue
    while True:
        Range()
        pizza()
        ammount()
        RepeatOrder = input('\nwould you like another pizza? (y/n) ')
        if RepeatOrder == 'y':
            continue
        elif RepeatOrder == 'n':
            break
    print("Here's your order total:")
    print(order)
    print("Your total is: $" + str(ordertotal))
    break