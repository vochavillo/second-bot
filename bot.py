from alumni import main

def ask_question:
    response = input("Would you like to know if there are Stanford affiliates at PolicyLink? (Y/N): ")
    return response

def bot():
    response = ask_question()
    if response == 'Y':
        main()
