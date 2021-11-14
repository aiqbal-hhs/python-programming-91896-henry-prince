import sys

#Error control for int or floats
def NumError(prompt):
    global Prompt
    global answer
    Prompt = prompt
    #tries to find if number is a valid number
    try:
        answer = float(input(prompt))
        #invalid number if pulled up by these
        if answer <= 0:
            print('number had to be positive')
            NumError(prompt)
        if answer >= 9999999999:
            print('That is too much, try again')
            NumError(prompt)
        #valid number it passes through to here and checks if input is correct
        else:
            correct("num")
            if Correct == 'y':
                return answer
    #not a number if picked up here
    except ValueError:
        print('Thats not a number! Try again')
        NumError(prompt)


#Error control for Strings
def StrError(prompt):
    global Prompt
    global answer
    while True:
        Prompt = prompt
        answer = str(input(prompt))
        #identifies if input is number and raises and error if it is
        for f in [int, float]:
            try:
                _ = f(answer)
            except:
                pass
            else:
                print('Input shouldnt be a number')
                StrError(Prompt)
        #if passes checks if input is correct
        correct("str")
        return answer


#Asks users if their input is correct
def correct(return_):
    global Prompt
    global Correct
    Correct = str(input('Please check if this information correct? (y/n) '))
    if Correct in ('y', 'n'):
        #if correct continues program as normal
        if Correct == 'y':
            return
        #if incorrect determines where call came from and sends it back to ask again
        elif Correct == 'n':
            if return_ == "str":
                StrError(Prompt)
            elif return_ == "num":
                NumError(Prompt)
    else:
        print('Invalid input')
        correct(return_)


#collects first name, last name, phone number, address and adds $3 to total when delivery is selected
def delivery():
    global ordertotal
    ordertotal += 3
    FirstName = StrError('What is the first name? ')
    FirstName = answer
    LastName = StrError('What is the last name? ')
    LastName = answer
    Address = StrError('What is the address? ')
    Address = answer
    PhoneNumber = NumError('Whats the phone number? ')
    PhoneNumber = int(answer)
    print('\nFirst name: ', FirstName, '\nLast name: ', LastName, '\nAddress: ', Address, '\nPhone number: ', PhoneNumber)


# Collects first and last name when pickup is selected
def pickup():
    FirstName = StrError('What is the first name? ')
    FirstName = answer
    LastName = StrError('What is the last name? ')
    LastName = answer
    print('\nFirst name: ', FirstName, '\nLast name: ', LastName)


#sellect range
def Range_():
    global pizzaprice
    global _Range
    while True:
        n = input('\nPlease select a range: (1. Regular 2. Gourmet)? ')
        n = int(n)
        #if regular sets pizza price to 8.5 and gets ready to print
        if n == 1:
            _Range = regular
            pizzaprice = 8.5
        #if gourmet sets pizza price to 12.5 and gets ready to print
        elif n == 2:
            _Range = gourmet
            pizzaprice = 12.5
        #handles invalid inputs
        else:
            print('Invalid input')
            continue
        #prints range that has been selected one by one
        for i in range(len(_Range)):
            print(i + 1, '- ', _Range[i + 1])
        return


#selects pizza
def _pizza():
    global Pizza
    pizza = NumError("\nWhat Pizza would you like? (please select number when making choice) ")
    pizza = int(answer)
    #determines if selected pizza is in selected range
    if pizza in _Range:
        Pizza = _Range[pizza]
        print('\nYou have selected: ', Pizza, '\n')
    else:
        _pizza()


#finds out how many pizzas user wants and handles costomizing each individual pizza
def ammount():
    #compliles nessercary variables
    global tpammount
    global toppingprice
    global pizzaorder
    global pizzan
    #gets ammount of pizzas wanted and processes that information (with error control)
    pammount = NumError('How many pizzas would you like? ')
    pammount = int(answer)
    tpammount += pammount
    #checks if total pizzas is a viable number and if total pizzas is less than 5 pizzas
    if pammount >= 1 and pammount <= 5 and tpammount <= 5:
        print('\nYou have selected: ', pammount, Pizza, 'pizzas')
        #goes through pizza individually and handles topping and pricing funtions for each individual pizza + adds them to order dictionary
        for i in range(pammount):
            pizzan += 1
            toppingprice = 0
            pizzaorder["Pizza"] = str(Pizza)
            topping_(pizzan)
            Pricecalc()
            order[pizzan] = pizzaorder
            pizzaorder = {}
        return
    #handles if total pizzas have reached limit
    elif tpammount > 5 or pammount > 5:
        tpammount -= pammount
        print('You have selected: ', pammount, Pizza, 'pizzas')
        print('You have exceeded the maximum amount of 5 pizzas, you can order up to', 5 - tpammount, 'more pizzas')
        ammount()
    #handles error/invalid input
    else:
        print("You have given an invaid input, please try again\n")
        ammount()


#select toppings (if wanted)
def topping_(pizzan):
    global toppingprice
    toppingli = []
    topping = ''
    s = ''
    s = input('\nWould you like any extra toppings for pizza #' + str(pizzan) + '? (y/n) ')
    #allows selection of toppings
    if s == 'y':
        print("\n")
        #prints off toppings one by one
        for i in range(len(toppings)):
            print(i + 1, '- ', toppings[i + 1])
        #allows user to select topping
        while True:
            topping = NumError('\nPlease select a topping you would like: ')
            topping = int(answer)
            #determines if topping is in avalible list and if so adds to list + .50 charge
            if topping in toppings:
                toppingli.append(toppings[topping])
                toppingprice += 0.5
                #asks if user wants more toppings if no adds list to dictionary, if yes repeates code
                s = input('Would you like any more toppings? (y/n) ')
                if s == 'y':
                    continue
                elif s == 'n':
                    pizzaorder["Toppings"] = "toppings: " + ", ".join(toppingli)
                    return
                else:
                    print('Invalid input')
                    continue
            else:
                print('Invalid input')
                topping_()
        print('You have selected: ', topping)
    #sets toppings to none
    elif s == 'n':
        pizzaorder["Toppings"] = "Toppings: None"
        return
    else:
        print('Invalid input')
        topping_()


#calculates the cost of pizza + total cost
def Pricecalc():
    global ordertotal
    pizzaorder["PizzaCost"] = "Pizza: $" + str(pizzaprice)
    pizzaorder["ToppingsCost"] = "Toppings: $" + str(toppingprice)
    pizzatotal = pizzaprice + toppingprice
    pizzaorder["TotalCost"] = "Total: $" + str(pizzatotal)
    ordertotal += pizzatotal


# Main loop
while True:
    #sets up all varibles and if restarted resets varibles to default values
    ordertotal = 0
    toppingprice = 0
    pizzaprice = 0
    n = 0
    s = ''
    Prompt = ''
    tpammount = 0
    pizzan = 0
    regular = {1:"Hawaian", 2:"Ham & Cheese", 3:"Pepperoni", 4:"Vegetarian", 5:"Cheese", 6:"Margareta",  7:"Cheesy Garlic"}
    gourmet = {1:"Meat lovers", 2:"Vege Supreme", 3:"Chicken Deluxe", 4:"Triple Cheese", 5:"New Yorker"}
    toppings = {1:"Pepperoni", 2:"Sausage", 3:"Bacon", 4:"Ham", 5:"Chicken", 6:"Mushrooms", 7:"Onions", 8:"Olives", 9:"Green Peppers", 10:"Pineapple", 11:"Spinach", 12:"Jalapenos", 13:"Banana Peppers"}
    order = {}
    pizzaorder = {}
    Topping = {}
    #selects pickup or delivery
    Collect = str(input('Would you like deliverly or pickup? '))
    Collect = Collect.lower().strip().replace(' ', '')
    #sends to delivery function
    if Collect == 'delivery':
        delivery()
        deliveryc = 3
    #sends to pickup function
    elif Collect == 'pickup':
        pickup()
        deliveryc = 0
    else:
        print('that is not an option')
        continue
    #loop for pizza ordering
    while True:
        Range_()
        _pizza()
        ammount()
        #allows user to order another pizza
        RepeatOrder = input('\nwould you like another pizza? (y/n) ')
        #determines if user already ordered 5 pizzas, continues to order breakdown is they have
        if tpammount == 5 and RepeatOrder == 'y':
            print("You have already ordered 5 pizzas, you cannot order more")
            break
        else:
            #allows user to add another pizza
            if RepeatOrder == 'y':
                continue
            #continues to cost breakdown
            elif RepeatOrder == 'n':
                break
    #cost breakdown of the order, spit into individual pizzas + total cost
    print("Here's your order total:")
    for i in range(len(order)):
        print(i + 1, ". \n", order[i + 1]["Pizza"], "\n", order[i + 1]["Toppings"], "\n", order[i + 1]["PizzaCost"], "\n", order[i + 1]["ToppingsCost"], "\n", order[i + 1]["TotalCost"], "\n")
    print('Delivery: ${}' .format(deliveryc))
    print("\nYour total is: $" + str(ordertotal))
    #allows user to restart to quit the program
    while True:
        restart = input('\nwould you like to restart the program? (y/n) ')
        if restart == 'y':
            continue
        elif restart == 'n':
            print("goodbye!")
            sys.exit()
        else:
            print("Invalid input, please try again!")
            continue


#do flow chart
#film program working example