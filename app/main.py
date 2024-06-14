import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    if command == "exit 0":
        exit(0)
    else:
        sys.stdout.write(f"{command}: command not found\n")

    main()



if __name__ == "__main__":
    main()
