# '''
# Call a function from within another function
# in the same class in Python
# '''


class Main:

    # constructor of Main class 
    def __init__(self):
        # Initialization of the Strings 
        self.String1 = "Hello"
        self.String2 = "World"

    def Function1(self):
        # calling Function2 Method 
        self.Function2()
        print("Function1 : ", self.String2)
        return

    def Function2(self):
        print("Function2 : ", self.String1)
        return


# Instance of Class Main
Object = Main()

# Calling Function1 
Object.Function1() 