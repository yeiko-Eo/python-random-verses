import json, random

def load_verses(filename = "rand-verses.json"): # Load verses from a JSON file
    try:
        with open(filename, "r", encoding="utf-8") as file: # Open the file in read mode with UTF-8 encoding
            data = json.load(file) # Load the JSON file into the data variable
        return data["verses"] # Return the list of verses
    except FileNotFoundError: # If the file is not found
        print("File not found: ", filename) 
        return []
    except json.JSONDecodeError: # If there is an error reading the JSON file
        print("Error: Could not read the JSON file correctly")
        return [] # Return an empty list

def get_random_verse():
    verses = load_verses()
    if verses:
        return random.choice(verses) # Return a random verse
    return "No verses available" # If no verses are available

if __name__ == "__main__":
    while True:
        try:
            print("\n-- MENU --\n1. Generate random verse\n2. Exit") 
            opc = int(input("\nOption: "))
            if opc == 1:
                print(get_random_verse())
            elif opc == 2:
                print("See ya!")
                break
            else:
                print("Invalid option")
        except ValueError as e:
            print(f"Error: {e}")