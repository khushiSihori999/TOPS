class EvenNumberError(Exception):
    """Custom Exception for even numbers"""
    pass


try:
    num = int(input("Enter an odd number: "))
    if num % 2 == 0:
        # Raise custom exception
        raise EvenNumberError("You entered an even number, only odd numbers are allowed!")
    else:
        print(f"Great! You entered an odd number: {num}")
except EvenNumberError as e:
    print("Exception:", e)
except ValueError:
    print("Invalid input! Please enter an integer.")
finally:
    print("Program finished.")
