shopping_basket = {}  #empty dic
                      #{key:value} e.g. {'apples': 5}
print("""
Shopping Basket Options
------------------------
1: Add item,
2: Remove item,
3: View basket,
0: Exit Program

""")

option = int(input('Enter an option: '))

while option != 0:
    if option == 1:
        item = input("Enter an item: ")
        if item in shopping_basket:
            print('Item already in shopping basket')
            qnty = int(input('Enter the quantity: '))
            shopping_basket[item] = shopping_basket[item] + qnty
        else:
            qnty = int(input('Enter the quantity: '))
            shopping_basket[item] = qnty
    elif option == 2:
        item = input("Enter an item: ")
        del(shopping_basket[item])

    elif option == 3:
        for item in shopping_basket:
            print(item, ':',shopping_basket[item])

    elif option != 0:
        print("You didn't enter a valid number.")

    option = int(input('\n\nEnter an option: '))
else:
    print('Shopping basket program closed')
