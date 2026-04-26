from summarise import summarise_notes
from init import init_query_engine
from helpers import clear_console

def main():
    clear_console()
    print("Initializing AI Study Assistant...")
    query_engine = init_query_engine()
    print("Ready.\n")

    options = {
        "1": ("Summarise notes", lambda: summarise_notes(query_engine)),
        "2": ("Exit", None)
    }

    while True:
        print("=== MAIN MENU ===")
        
        # Print menu dynamically
        for key, (label, _) in options.items():
            print(f"{key}. {label}")

        choice = input("Select an option: ").strip()

        if choice not in options:
            print("Invalid option. Try again.\n")
            continue

        label, action = options[choice]

        if action is None:   # Exit option
            print("Goodbye.")
            break

        # Call the linked function
        action()
        print()

if __name__ == "__main__":
    main()