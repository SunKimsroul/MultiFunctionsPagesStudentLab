from pythonapp2 import get_user_details, display_greeting

def main():
    user_name = get_user_details()
    display_greeting(user_name)

if __name__ == "__main__":
    main()