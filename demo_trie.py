from trie import Trie

def print_help():
    print("\nCommands:")
    print("  insert <word>      - Insert a word into the Trie")
    print("  search <word>      - Search for a complete word")
    print("  starts <prefix>    - Check if any word starts with prefix")
    print("  delete <word>      - Delete a word from the Trie")
    print("  quit               - Exit demo\n")

def main():
    t = Trie()
    print("🔵 Trie Live Demo")
    print_help()

    while True:
        cmd = input("> ").strip().split()

        if not cmd:
            continue

        action = cmd[0].lower()

        if action == "quit":
            print("Exiting demo.")
            break

        elif action == "insert" and len(cmd) == 2:
            t.insert(cmd[1])
            print(f"Inserted '{cmd[1]}'")

        elif action == "search" and len(cmd) == 2:
            result = t.search(cmd[1])
            print(f"Search '{cmd[1]}': {result}")

        elif action == "starts" and len(cmd) == 2:
            result = t.startswith(cmd[1])
            print(f"StartsWith '{cmd[1]}': {result}")

        elif action == "delete" and len(cmd) == 2:
            t.delete(cmd[1])
            print(f"Deleted '{cmd[1]}' (if it existed)")

        else:
            print("❗ Invalid command or missing argument.")
            print_help()

if __name__ == "__main__":
    main()