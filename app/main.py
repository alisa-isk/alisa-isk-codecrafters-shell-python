import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    user_input = input()
    if user_input not in commands:
        sys.stdout.write(f"{user_input}: command not found\n")


if __name__ == "__main__":
    main()
