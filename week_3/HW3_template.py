#Welcome to Python Kitchen!

#Here is a list of dishes Python Kitchen provides. It is a list of tuples.
#Each tuple has information of one dish in order: (Number, Name, Price, Origin, Whether is vegetarian)
dishes=[(1,'Salmon Sushi', 30, 'Japan', 'N'),(2,'Pork Dumplings', 25, 'China', 'N'),(3,'Choziro Tacos', 20, 'Mexico', 'N'),
(4, 'Chickpea Curry', 36, 'India', 'Y'),(5, 'Apple Pie', 16, 'USA', 'Y'),(6, 'Jollof Rice', 18, 'Nigeria', 'N'),
(7, 'Dolma', 45, 'Azerbaijan', 'N'),(8, 'Vegetable Pho', 25, 'Vietnam', 'Y'),(9, 'Kvass', 12, 'Russia',  'Y'),(10, 'Luau', 30, 'Samoa', 'Y')]

#TO DO: put the dishes into this dictionary. The key of the dictionary is the dish's name, the value is the dish's price.
#Example: Salmon Sushi: 30
prices={}
#--Complete the code here--

#FUNCTIONS
def print_menu():
    #--Complete the function here--
    pass

def print_vegetarian_menu():
    #--Complete the function here--
    pass

def print_dishes_ordered_by_price():
    #--Complete the function here--
    pass

def add_dish():
    #--Complete the function here--
    pass

def apply_discount(price,percentage):
    #--Complete the function here--
    #USE LAMDA FUNCTION
    pass

def get_order():
    #--Complete the function here--
    pass


#The main menu and main function have been written for you this time. Look over the code and try to understand it. You will be writing your own
#menu and main function soon.
def menu():
    print('Welcome to Python Kitchen. How may I help you? Enter the number of the option you want to do.')
    print('1.See menu')
    print('2.Order')
    print('3.See dishes in order of price')
    print('4.I am the chef, I want to add a dish to the menu.')
    print('5.Exit')
    pass

#Main Function. This function calls the functions above. The main function is like the manager of the train station.
#It determines which functions are called, in what order, how many times. It often has additional code as well.

def main():
    c=0
    while(c!=5):
        menu()
        c=int(input())
        if c is 1:
            a=input('Are you vegatarian? Enter Y or N.')
            if (a=='y' or a=='Y'):
                print_vegetarian_menu()
            else:
                print_menu()
        if c is 2:
            sum=get_order()
            print('Your total is ',sum)
            b=input('What is your discount percentage?')
            sum=apply_discount(sum,float(b))
            print('After discount your total is ',sum)
        if c is 3:
            print_dishes_ordered_by_price()
        if c is 4:
            add_dish()
            print('Your new menu is: ')
            print_menu()

    print('Have a good day!')

    pass

#Execute main
main()
