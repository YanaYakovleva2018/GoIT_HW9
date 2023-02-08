def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Please, enter the contact like this: \nName number"
        except KeyError:
            return "This contact doesn't exist!"
        except ValueError:
            return "Invalid command entered"
    return inner

def welcome(*args):
    return "How can i help you?"

def to_exit(*args):
    return "Good bye!"

data = {}

@input_error
def add_contact(*args):
    data.update({str(args[0]): int(args[1])})
    return f'Contact {args[0].title()} has added successfully'

@input_error
def change_number(*args):
    data[args[0]] = int(args[1])
    return f"Phone for contact {args[0].title()} has changed."

@input_error
def delete_number(*args):
    del data[args[0]]
    return f"Phone for contact {args[0].title()} has deleted."

@input_error
def print_phone(*args):
    return data[args[0]]

def show_all(*args):
    if len(data)> 0:
        return "\n".join([f"{k.title()} : {v}" for k, v in data.items()])
    else:
        return "Contacts is empty"
      
all_comands = {
    welcome: ["hello", "hi"],
    add_contact: ["add", "new"],
    change_number: ["change",],
    print_phone: ["phone", "number"],
    show_all: ["show", "show all"],
    to_exit: [".", "bye", "close", "good bye", "exit"],
    delete_number: ["del", "delete"]
}

def command(user_input: str):
    for key, value in all_comands.items():
        for i in value:
            if user_input.lower().startswith(i.lower()):
                return key, user_input[len(i):].strip().split()

def main():
    while True:
        user_input = input("Enter the command: ")
        cmd, parser_data = command(user_input)
        print(cmd(*parser_data))
        if cmd is to_exit:
            break

if __name__ == "__main__":
    main()



