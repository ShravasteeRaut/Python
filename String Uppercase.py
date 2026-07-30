class IOString():


    def __init__(self):
        self.str1 = ""

    def get_String(self):
            self.str1 = input("Enter String : ")

    def print_String(self):
            print("Result is :", self.str1.upper())

    def length_String(self):
          print("Length of the string is: ", len(self.str1))

obj = IOString()

obj.get_String()
obj.print_String()
obj.length_String()
