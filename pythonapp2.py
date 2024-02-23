from pythonapp import format_name

def get_user_details():
    """Prompts user for their details and returns the formatted name."""
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return format_name(first_name, last_name)

def display_greeting(name):
    """Displays a greeting message to the user."""
    print(f"Hello, {name}! Welcome to our application.")