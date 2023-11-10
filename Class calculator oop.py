
#Ken Mutuku
#SCT211-0050/2022
class Oopcalc:
    def _init_(self):
        self.result = 0

    def add(self, no1, no2):
        self.result = no1 + no2

    def subtract(self, no1, no2):
        self.result = no1 - no2

    def multiply(self, no1, no2):
        self.result = num1 * num2

    def divide(self, no1, no2):
        if no2 == 0:
            return "Error: Division by zero"
        self.result = no1 / no2

    def get_result(self):
        return self.result

    def clear(self):
        self.result = 0

def main():
    calculator = Oopcalc()

    while True:
        print("Input the number of your Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Delete the result")
        print("6. Quit the program")

        user_input = input(": ")

        if user_input == "6":
            break
        elif user_input == "5":
            calculator.clear()
            print("Result cleared.")
        elif user_input in ("1", "2", "3", "4"):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if user_input == "1":
                calculator.add(no1, no2)
                print("Result:", calculator.get_result())
            elif user_input == "2":
                calculator.subtract(no1, no2)
                print("Result:", calculator.get_result())
            elif user_input == "3":
                calculator.multiply(no1, no2)
                print("Result:", calculator.get_result())
            elif user_input == "4":
                result = calculator.divide(no1, no2)
                print("Result:", calculator.get_result())
                if result == "Error: Division by zero":
                    print(result)
                else:
                    print("Result:", calculator.get_result())
        else:
            print("Invalid input. Please try again.")

if _name_ == "_main_":
    main()