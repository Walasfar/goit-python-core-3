
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()        
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

def change_number(args, contacts):
    name, new_number = args
    if name in contacts:
        contacts[name] = new_number
        return "Contact update."
    else:
        return "Name not found!"

def main():
    
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            name = args[0]
            
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            
            try:
                match command:
                    
                    case "all":
                        
                        if len(contacts) > 0:
                            
                            for name, number in contacts.items():
                                print(f"Ім'я: {name}, номер: {number}")
                        
                        else:
                            print("Book contacts is empty.")
                        
                    case "hello":
                        print("How can I help you?")
                        
                    case "add":
                        if name in contacts:
                            print("Name exists!")
                        else:
                            print(add_contact(args, contacts))
                    
                    case "change":
                        print(change_number(args, contacts))
                    
                    case "phone":
                        if name in contacts:
                            print(f"Phone {name}: ", contacts[args[0]])
                        else:
                            print("Contact not found.")
                    
                    case _:
                        print("Invalid command.")
                    
            except ValueError as e:
                print(f"You enter bad commands! Need: command name number")
                
    return contacts


if __name__ == "__main__":
    main()
