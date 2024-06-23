import sys
import os
import subprocess

command_list = ["echo", "exit", "type"]
PATH = os.environ.get("PATH")


def get_file_path(PATH, file_name):
    """Helper function to get path of command"""
    directories = PATH.split(":")
    for directory in directories:
        path = os.path.join(directory, file_name)
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    return None


def print_type(command):
    """Prints the command type"""
    command = command[len("type "):]
    if command in command_list:
        sys.stdout.write(f"{command} is a shell builtin\n")
    elif PATH:
        file_name = get_file_path(PATH, command)
        if file_name:
            sys.stdout.write(f"{command} is {file_name}\n")
        else:
            sys.stdout.write(f"{command}: not found\n")
    else:
        sys.stdout.write(f"{command}: not found\n")


def main():
    """main for shell"""
    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input()
    if command == "exit 0":
        exit(0)
    elif command.startswith("echo "):
        print(command[len("echo "):])
    elif command.startswith("type "):
        print_type(command)
    elif command == "pwd":
        print(os.getcwd())
    else:
        parts = command.split()
        executable = get_file_path(PATH, parts[0])
        if executable:
            try:
                subprocess.run(parts)
            except subprocess.CalledProcessError as e:
                sys.stderr.write(f"{command}: {e}\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")

    main()


if __name__ == "__main__":
    main()
