# Приймає команду юзера
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()  
    return cmd, *args

# Добавляє контакт в базу
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

# Міняє номер
def change_number(args, contacts):
    name, new_number = args
    if name in contacts:
        contacts[name] = new_number
        return "Contact updated."
    else:
        return "Name not found!"

def show_base(adress_book):
    for key, value in adress_book.items():
        print(f"Name: {key}, number: {value}")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        try:
            
            if command in ["close", "quit", "exit"]:
                print("Good bye!")
                break
            elif command == 'hello':
                print("Hello im here for help you!")
            
            elif command == 'all':
            
                if len(contacts) == 0:
                    print("Base is empty.")
                else:
                    show_base(contacts)
                
            elif command == 'add':
                add_contact(args, contacts)
                
            match command:
                
                case 'change':
                    print (change_number(args, contacts))
                    
                case 'phone':
                    print(f"Phone {args[0]} - {contacts[args[0]]}")
                
        except ValueError as e:
            print("Number argumets is required!")
        

if __name__ == "__main__":
    main()
