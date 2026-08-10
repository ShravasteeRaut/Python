class Account:
 
    def __init__(self, name, pin):
        self.name = name
        self.__pin = pin  


    def show_pin_status(self):
        print("Account Name:", self.name)
        print("PIN is safely stored inside the class.")
 
   
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN updated successfully.")
        else:
            print("Invalid PIN. PIN must be exactly 4 digits.")
 
    
    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("Access granted.")
        else:
            print("Access denied.")



    def __str__(self):
        return "Account holder: " + self.name
 
 

my_account = Account("Shravastee", "2023")
 

print(my_account)
 

my_account.show_pin_status()
 

my_account.__pin = "2203"
print("Tried changing PIN directly from outside.")
 

my_account.check_pin("2203")
my_account.check_pin("2023")
 

my_account.set_pin("2203")
 

my_account.check_pin("2203")
