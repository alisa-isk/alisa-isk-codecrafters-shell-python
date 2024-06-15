import sys

command_list = ["echo", "exit", "type"]


def print_type(command):
    command = command[len("type "):]
    if command in command_list:
        sys.stdout.write(f"{command} is a shell builtin\n")
    else:
        sys.stdout.write(f"{command}: not found\n")


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    valid_commands = {}
    if command == "exit 0":
        exit(0)
    elif command.startswith("echo "):
        print(command[len("echo "):])
    elif command.startswith("type "):
        print_type(command)
    else:
        sys.stdout.write(f"{command}: command not found\n")

    main()


if __name__ == "__main__":
    main()
