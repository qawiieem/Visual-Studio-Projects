from Chef import Chef

class ChineseChef(Chef): #inside ChineseChef class, i able to use all the func inside Chef class (Inheritance)
    
    def make_special_dish(self):    #override make_special_dish function from Chef class
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")

