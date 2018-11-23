class FizzBuzz:

    # After creating new instance of FizzBuzz constructor runs immediately if passed argument is True
    def __init__(self, run_or_not_to_run=False):

        if run_or_not_to_run:
            i = 1
            while i < 101:
                print("FizzBuzz") if i % 15 == 0 \
                    else print("Fizz") if i % 3 == 0 \
                    else print("Buzz") if i % 5 == 0 \
                    else print(i)
                i += 1
        #this will run code them class is iniatilazed
        self.fizz_argument = fizz_with_range()

    # creating Fizzbuzzer class inside FizzBuzz class also argument for running code throught constructor
    # class can be set to True
    class Fizzbuzzer:

        def __init__(self, run_or_not_to_run=False):

            if run_or_not_to_run:
                i = 1
                while i < 101:
                    print("FizzBuzz") if i % 15 == 0 \
                        else print("Fizz") if i % 3 == 0 \
                        else print("Buzz") if i % 5 == 0 \
                        else print(i)
                    i += 1

    #class method can uses FizzBuzz class methods without self
    @classmethod
    def fizz_with_class_method(cls):
        return fizz_with_range()

    #static method independant from class method, but can be accesed throught class
    @staticmethod
    def fizz_with_static_method():

        for i in range(1, 101):
            print("FizzBuzz") if i % 15 == 0 \
                else print("Fizz") if i % 3 == 0 \
                else print("Buzz") if i % 5 == 0 \
                else print(i)

    #-------------FizzBuzz Functions------------------

    # Fizzbuzz with conversion values to binary
    def fizz_with_binary(self):

        for i in range(1, 101):
            print(self.convert_to_binary("FizzBuzz")) if i % 15 == 0 \
                else print(self.convert_to_binary("Fizz")) if i % 3 == 0 \
                else print(self.convert_to_binary("Buzz")) if i % 5 == 0 \
                else print(self.convert_to_binary(str(i)))
            i += 1

    # Fizzbuzz with range
    def fizz_with_range(self):
        for i in range(1, 101):
            self.print_fizz_buzz(i)
            i += 1

    # Fizzbuzz with while
    def fizz_with_while(self):

        i = 1
        while i < 101:
            self.print_fizz_buzz(i)
            i += 1

    # Function calls is stacked on stack after comliting all calls it realises them
    # fizz_buzz with recursion
    def fizz_with_recursion(self, start):

        if start < 101:
            self.print_fizz_buzz(start)
            start += 1
            self.fizz_with_recursion(start)

    #------------------FizzBuzz calling functions ----------------

    # Print answer of fizz buzz
    def print_fizz_buzz(self, i):

        print("FizzBuzz") if i % 15 == 0 \
            else print("Fizz") if i % 3 == 0 \
            else print("Buzz") if i % 5 == 0 \
            else print(i)

    # Converts answers from fizzbuzz too binary
    def convert_to_binary(self, convertable):

        return ' '.join(format(ord(x), 'b') for x in convertable)

#function not in class
def fizz_with_range():
    for i in range(1, 101):
        print("FizzBuzz") if i % 15 == 0 \
            else print("Fizz") if i % 3 == 0 \
            else print("Buzz") if i % 5 == 0 \
            else print(i)
        i += 1

new_buzz = FizzBuzz()
#1. Function call fizzbuzz
#fizz_with_range()
#2. Class initiation fizzbuzz
#$new_buzz = FizzBuzz(False)
#3 Class within class fizzbuzz
#new_buzz.Fizzbuzzer(True)
#4.With range
#new_buzz.fizz_with_range()
#5.With while
#new_buzz.fizz_with_while()
#6.With Binary
#new_buzz.fizz_with_binary()
#7.Static fizz buzz method
#new_buzz.fizz_with_static_method()
#8.Class method
#new_buzz.fizz_with_class_method()
#9. Fizz with recursion
#new_buzz.fizz_with_recursion()

#new_buzz.fizz_argument
new_buzz.fizz_argument