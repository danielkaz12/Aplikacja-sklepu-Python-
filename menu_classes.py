#Code to creating the GUI main, admin and worker menu
#and executing by using them components the functions from "execute_fun"

from tkinter import *
import execute_fun as rs

#Main menu
class menu():
    """Main menu which has a metod to show GUI menu
    and a method to show GUI database
    """

    @classmethod
    def show(cls):
        """Outputing the main menu (by clicking the selected button, there will
        be returned a value "choose" to identify what menu is selected)"""
        
        #execute function for buttons
        def admin_ex():
            root.destroy()
            global choose
            choose = 1
            return choose

        def worker_ex():
            root.destroy()
            global choose
            choose = 2
            return choose
        
        #creating GUI with used buttons
        root = Tk()
        user = Button(root, text ="Admin", padx = 80, pady = 40, command=admin_ex)
        user.pack()
        worker = Button(root, text ="Worker", padx = 80, pady = 40, command=worker_ex)
        worker.pack()
        root.mainloop()
        return choose

    @classmethod
    def database(cls):
        """Printing the database as outputed labels
        """
        root2 = Tk()
        f = open('dane.txt', 'r')
        lines = f.readlines()
        for line in lines:
            list = line.replace('\n', '').split(',')
            line = "Code: " + list[0] + " Name: " + list[1] + " Prize (per kg): " + list[2]
            l = Label(root2, text = line)
            l.pack()
        f.close()
        root2.mainloop()

#Worker menu
class worker_menu(menu):
    """Worker menu which has a metod to show GUI worker menu
    and execute the "calculate" function from "execute_fun" file
    """

    @classmethod
    def show(cls):
        """Outputing the worker menu (by clicking the selected button, adequate function will be execute)"""
        #execute function for buttons
        def details():
            menu.database()

        def calculate():
            rs.calculate()
        
        #creating GUI with used buttons
        root = Tk()
        user = Button(root, text ="Show details", padx = 40, pady = 20, command=details)
        user.pack()
        worker = Button(root, text ="Calculate", padx = 40, pady = 20, command=calculate)
        worker.pack()
        root.mainloop()

#Admin menu
class admin_menu(menu):
    """Admin menu which has a metod to show GUI worker menu
    and execute the "delete_item" and "new_item" functions from "execute_fun" file
    """

    @classmethod
    def show(cls):
        """Outputing the worker menu (by clicking the selected button, adequate function will be execute)"""
        #execute function for buttons
        def details():
            menu.database()

        def add_item():
            rs.new_item()

        def del_item():
            rs.delete_item()
        
        #creating GUI with used buttons
        root = Tk()
        user = Button(root, text ="Show details", padx = 40, pady = 20, command=details)
        user.pack()
        worker = Button(root, text ="Add item", padx = 40, pady = 20, command=add_item)
        worker.pack()
        worker = Button(root, text ="Delete item", padx = 40, pady = 20, command=del_item)
        worker.pack()
        root.mainloop()




