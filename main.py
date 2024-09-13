import pyperclip
import readline
from details import details, suggestions

print("\nPlease select the thing to copy")

def completer(text, state):
    print("completing")
    options = [x for x in suggestions if x.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")


while True:
    for option in details.keys():
        print(option, ": ", details[option][0])

    selection = input()

    if selection not in details:
        print("\nPlease select a valid option")
    elif selection == "q":
        exit(0)
    elif selection == "lm" or selection == "lm2":
        name = input("Enter the name of the person: ")
        position = input("Enter the position of the person: ")
        company = input("Enter the company of the person: ")
        complete_dm = details[selection][1] + name + details[selection][2] + position + details[selection][3] + company + details[selection][4]
        pyperclip.copy(complete_dm)
    else:
        pyperclip.copy(details[selection][1])
