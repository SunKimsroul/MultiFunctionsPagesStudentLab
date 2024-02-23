from datetime import date

def format_name(first_name, last_name):
    """Formats the user's name."""
    return f"{first_name.strip().title()} {last_name.strip().title()}"

def calculate_age(birth_year):
    """Calculates the user's age."""
    current_year = date.today().year
    age = current_year - birth_year
    return age