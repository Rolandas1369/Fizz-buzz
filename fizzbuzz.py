
class FizzBuzz:

    # After creating new instance of FizzBuzz constructor runs immediately if passed argument is True
    def __init__(self, run_or_not_to_run=False):

        if (run_or_not_to_run):
            i = 1
            while i < 101:
                print("FizzBuzz") if i % 3 == 0 and i % 5 == 0 else print("Fizz") \
                    if i % 3 == 0 else print("Buzz") if i % 5 == 0 else print(i)
                i += 1

    # creating Fizzbuzzer class inside FizzBuzz class also argument for running code thought constructor
    # class can be set to True
    class Fizzbuzzer:

        def __init__(self, run_or_not_to_run=False):

            if run_or_not_to_run:
                i = 1
                while i < 101:
                    print("FizzBuzz") if i % 3 == 0 and i % 5 == 0 else print("Fizz") \
                        if i % 3 == 0 else print("Buzz") if i % 5 == 0 else print(i)
                    i += 1

    #-------------FizzBuzz Functions------------------

    # Fizzbuzz with conversion values to binary
    def fizz_with_binary(self):

        for i in range(1, 101):
            print(self.convert_to_binary("FizzBuzz")) if i % 3 == 0 and i % 5 == 0 \
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

    # Fizzbuzz with function calls
    def fizz_with_function_calls(self):

        i = 1
        while i < 101:
            self.print_fizz_buzz(i)
            i += 1

    # Function calls is stacked on stack and when all of them realised
    # fizz_buzz with recursion
    def fizz_with_recursion(self, start):

        if start < 101:
            self.print_fizz_buzz(start)
            start += 1
            self.fizz_with_recursion(start)

    #------------------FizzBuzz calling functions ----------------

    # Print answer of fizz buzz
    def print_fizz_buzz(self, i):

        print("FizzBuzz") if i % 3 == 0 and i % 5 == 0 else print("Fizz") \
            if i % 3 == 0 else print("Buzz") if i % 5 == 0 else print(i)

    # Converts answers from fizzbuzz too binary
    def convert_to_binary(self, convertable):

        return ' '.join(format(ord(x), 'b') for x in convertable)


new_buzz = FizzBuzz(True)


