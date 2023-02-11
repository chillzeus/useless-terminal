import time
import platform

def system(input1):
    input1 = input1.split()
    match(input1[1]):
        case "machine":
            print(platform.machine())
        case "processor":
            print(platform.processor())
        case "version":
            print(platform.version())
        case "uname":
            print(platform.uname().system)
            print(platform.uname().node)


def help_system():
    time.sleep(0.5)
    print("'system' is a command used to find information about the user's system.")
    time.sleep(0.5)
    print("Commands are prefixed with 'system'. Supported terms:")
    print("'machine', 'version', 'platform', 'uname", 'processor', "systemos")
    print("This uses the python 'platform' module.")


# This is the main function, defined after the others
def new_command(input1):
    input1 = input(">> ")
    if input1[0:6] == "system":
        system(input1)
    elif input1 == "help system":
        help_system()
    else:
        print("The term '" + input1 + "' is not recognized")
        new_command("blank")

print("welcome to the useless terminal!")
print("type 'help' to learn more.")
time.sleep(0.5)

new_command("blank")