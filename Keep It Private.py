class myClass:

    __privateVar = 27


    def __privMeth(self):
        print("I'm inside class myClass")


    def hello(self):
        self.__privMeth()
        print("Private Variable value: ",myClass.__privateVar)


foo = myClass()
foo.hello()
 # the private method cannot be called outside the class. It has to be called through something (here, it is hello) which acts as a pharmacist. Otherwise, this code will not execute the __privMeth function, keeping it a secret.