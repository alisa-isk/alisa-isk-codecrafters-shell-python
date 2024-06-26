import sys
import os
import subprocess

command_list = ["echo", "exit", "type", "pwd"]
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
    """Main function for the shell.

    This function continuously prompts the user for input, processes the commands
    provided, and executes built-in commands or external programs. It supports
    built-in commands such as `echo`, `exit`, `type`, `pwd`, and `cd`, and can
    run external programs found in the system's PATH.

    Built-in commands:
    - echo: Prints the provided string to standard output.
    - exit: Exits the shell.
    - type: Displays information about the specified command.
    - pwd: Prints the current working directory.
    - cd: Changes the current working directory to the specified path. Supports `~` for the home directory.

    If a command is not a built-in, it attempts to find and execute it as an external program."""
    while True:
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
            sys.stdout.write(f"{os.getcwd()}\n")
        elif command.startswith("cd "):
            newpath = command[len("cd "):].strip()
            if newpath == "~":
                newpath = os.path.expanduser("~")
            try:
                os.chdir(newpath)
            except FileNotFoundError:
                sys.stdout.write(f"cd: {newpath}: No such file or directory\n")
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


if __name__ == "__main__":
    main()
