import os

def run_file(filename):
    print(f"Running {filename}...")
    os.system(f"python {filename}")
    print(f"{filename} has finished running.")

def get_valid_file():
    files = [f for f in os.listdir() if f.endswith(".py")]
    if not files:
        print("There are no Python files in this directory.")
        return None
    elif len(files) == 1:
        return files[0]
    else:
        print("Select a file to run:")
        for i, f in enumerate(files):
            print(f"{i+1}. {f}")
        while True:
            try:
                selection = int(input("> "))
                if 1 <= selection <= len(files):
                    return files[selection-1]
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input.")

def main():
    filename = get_valid_file()
    if filename:
        run_file(filename)
        with open("history.txt", "a") as f:
            f.write(f"{filename}\n")

        while True:
            choice = input("Run again? (y/n): ").lower()
            if choice == 'y':
                run_file(filename)
                with open("history.txt", "a") as f:
                    f.write(f"{filename}\n")
            elif choice == 'n':
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()