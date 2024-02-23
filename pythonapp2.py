from pythonapp import format_name, calculate_age

def get_user_details():
    """Prompts user for their details and returns the formatted name."""
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return format_name(first_name, last_name)

def get_contact_info():
    """Gets the user's contact information."""
    email = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")
    return email, phone_number

def display_greeting(name):
    """Displays a greeting message to the user."""
    print(f"Hello, {name}! Welcome to our application.")

def display_contact_info(email, phone_number, age):
    """Displays the user's contact information and age."""
    print(f"Contact Information:")
    print(f"Email: {email}")
    print(f"Phone Number: {phone_number}")
    print(f"Age: {age}")
