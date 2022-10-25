#Three functions:
# - calculate - calculating the prize for inputed object with addiced weight
# - new_item - adding a new product to the database
# - delete_item - deleting the product from the database

import making_object as mo

def calculate():
    """Calculating the output result for combination of inputed
    weight and code, where the code defines what prize will be taken to the calculates
    """

    result = 0
    while True:
        code = input('What code?(click enter to end):\n')
        mo.items_list.write()
        if code in [x.code for x in mo.items_list.list_val]:                                            #checking if the code is in the list of codes
            weight = float(input('What weight?:\n'))
            for x in mo.items_list.list_val:
                if code == x.code:                                                                      #finding the object wich have the input code as atrribute
                    result += round(x.result(weight), 2)                                                #adding the cost of product to the sumary result
                    print("Result: ",result)
                    break
        elif code == "":
            break
        else:
            print("wrong code. Try again")


def new_item():
    """Adding a new object to the database, where the
    given code is equal to the object code
    """

    f = open('dane.txt', 'r')
    lines = f.readlines()
    while True:
        f = open('dane.txt', 'a')
        decision = input("Do you want to add a new line?(input y if yes or click enter to end)")
        if decision == "y":
            code = str(input("Code:"))
            name = input("Name:")
            prize = input("Prize:")
            print(code)
            if any(code in line for line in lines):                                                     #checking if the input code is in the database
                print("Wrong code. Try again.")
            else:                                                                                       #if isn't in the database write a new line to database
                new_line = '\n' + code + ',' + name + ',' + prize
                f.write(new_line)
        elif decision == "":
            break
        else:
            print("wrong command. Try again")
    f.close()


def delete_item():
    """Deleteing an object from the database, where the
    code given by user is equal to the object code
    """
    
    f = open('dane.txt', 'r')
    lines = f.readlines()
    while True:
        decision = input("Do you want to delete line?(input y if yes or click enter to end)")
        if decision == "y":
            code2 = str(input("Code: "))
            if any(code2 in line for line in lines):
                f = open('dane.txt', 'w')
                for line in lines:
                    if code2 not in line:                                                                               #checking if the input code is not equal to single line in the database. if it isn't, write it again to database.
                        f.write(line)
                f.close()
            else:
                print("Wrong code, try again")         
        elif decision == "":
            break
        else:
            print("wrong command. Try again")
    f.close()


