#Code to creating object for the given lines from "dane.txt"
#and making a list of this object

class item():
    """Class of 3 atributes: name, code, prize for every vegetable or fruit"""
    def __init__(self, code, name, prize):
        self.code = code
        self.name = name
        self.prize = prize
    
    def result(self, weight):
        """function to calculate total result 
        for each input item and weight in main_app code"""
        self.weight = weight
        return self.prize*self.weight

class items_list(item):
    """Class for creating a list of all objects
    created by using the "item" class and records for "dane.txt"
    """
    list_val = [] #list of objects
    def write():
        f = open('dane.txt', 'r')
        lines = f.readlines()
        for line in lines:
            # Reading dane.txt line by line and adding all of the lines
            # ass new products(created with class items) into list list_val
            object = line.replace("\n","").split(',')
            items_list.list_val.append(item(object[0],object[1],float(object[2])))
        f.close()

    

  

        







