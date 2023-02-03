import time
import platform

def new_command(input1):
    input1 = input(">> ")
    if input1 == "help system":
        time.sleep(0.5)
        print("'system' is a command used to find information about the user's system.")
        time.sleep(0.5)
        print("Commands are prefixed with 'system'. Some terms to use are:")
        print("'machine', 'version', 'platform', 'uname", 'processor')
        print("This uses the python 'platform' module.")
    else:
        print("The term '" + input1 + "' is not recognized")
        time.sleep(1)
        new_command("blank")

print("welcome to the useless terminal!")
print("type 'help' to learn more.")
time.sleep(0.5)

new_command("blank")