# Define a class with a method that performs a division operation. Use try, except, and finally blocks within the method to handle division by zero and print an appropriate message.
class Calci:
    def divide(self, a,b): #self is used to refer to the instance of the class
        try:
            result=a/b
            return result
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
        finally:
            print("Division operation attempted.")

calc=Calci()
print(calc.divide(10,2))
print(calc.divide(10,0))
print(calc.divide(10,'a'))