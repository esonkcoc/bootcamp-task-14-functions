# Fixed price variables assigned at the start

nightly_hotel_cost = 100
hire_cost = 40

# Choice of destinations made clear to user
print("Destinations:\nLondon\nParis\nMadrid\nRome\nLisbon\n")

# Dictionary data structure  used to store the destination names as keys and their corresponding flight costs as values
destinations = {
"london": 400,
"paris": 500,
"madrid": 350,
"rome": 450,
"lisbon": 200
}

# Anticipated and coded against user input errors with .lower() and while loop else: message
def flight_cost():
    while True:
        destination = input("To which destination will you be flying? ").lower()
        if destination in destinations:
            flight = destinations[destination]
            print(f"Total flight expense: £{flight}")
            return flight
        else:
            print("This destination is not available. Please try again.")

def hotel_cost():
    num_nights = int(input("How many nights will you be staying?"))
    hotel_cost = num_nights * nightly_hotel_cost
    print(f"Total accommodation expense: £{hotel_cost}")
    return hotel_cost

def car_hire():
    num_hire_days = int(input("For how many days will you be hiring a car?"))
    car_hire = num_hire_days * hire_cost
    print(f"Total car hire expense: £{car_hire}")
    return car_hire

# Function calculates the total holiday cost by calling the flight_cost(), hotel_cost(), and car_hire() functions and adding their respective input intergers
def holiday_cost():
    holiday_cost = flight_cost() + hotel_cost() + car_hire()
    print(f"Total holiday expense: £{holiday_cost}")

# Executes the holiday_cost() function, which in turn executes the other functions as needed
holiday_cost()

"""The `return` statement in a function is used to specify the value that the function should output or "return" when it is called. It allows the function to pass a result back to the code that called it. Here's why we use `return` at the end of every function:

1. **Returning a value**: Functions often perform calculations or process data to produce a result. By using the `return` statement, we can send that result back to the caller. This allows the caller to use the value returned by the function for further computations, assignments, or printing.

2. **Terminating the function**: When the `return` statement is encountered in a function, it immediately exits the function and returns to the point of the function call. This ensures that the function's execution is stopped at that point, and any code following the `return` statement is not executed.

3. **Communicating information**: Functions can be designed to perform a specific task and provide information or results to the code that called them. By using `return`, we can pass information between functions and the main program, enabling modular and reusable code.

In the given code, each function is designed to calculate and provide a specific cost (flight cost, hotel cost, car hire cost) back to the `holiday_cost()` function. The `return` statement allows these functions to communicate their respective results to the `holiday_cost()` function, which then adds up all the costs and prints the total expense.

Note that not all functions require a `return` statement. Some functions may perform tasks without producing a result or may modify variables outside the function scope. In such cases, the `return` statement is not necessary."""