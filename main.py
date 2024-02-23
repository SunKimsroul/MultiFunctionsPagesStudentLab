from pythonapp2 import get_user_details, display_greeting, get_contact_info, display_contact_info
from pythonapp import calculate_age

def main():
    user_name = get_user_details()
    display_greeting(user_name)
    email, phone_number = get_contact_info()
    birth_year = int(input("Enter your birth year: "))
    age = calculate_age(birth_year)
    display_contact_info(email, phone_number, age)

if __name__ == "__main__":
    main()

