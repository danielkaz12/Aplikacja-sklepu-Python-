#Main code for executing the shop app, outputing the GUI menues

import menu_classes as mc

if __name__ == "__main__":
    choose = mc.menu.show()                                             #adding the chosen number by the button
    while True:
        if choose == 1:                                                 #checking if it is chosen the admin menu
            password = input("Password (click enter to go out): ")
            if password == 'admin':                                     #checking the password wor admin menu
                mc.admin_menu.show()                                    #executing the admin menu
                break
            elif password == '':
                break
            else:
                print("Wrong password. Try again.")
        elif choose == 2:                                               #checking if it is chosen the worker menu
            mc.worker_menu.show()                                       #executing the worker menu
            break
