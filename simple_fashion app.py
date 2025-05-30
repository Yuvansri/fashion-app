import random

class FashionApp:

    def __init__(self):

        self.categories = {

            "Casual": ["Jeans & T-Shirt", "Hoodie & Joggers"],

            "Formal": ["Suit", "Blazer & Trousers"],

            "Party": [" Sequin Dress", "Shirt & Slim Pants"]

        }

    def show_menu(self):

        print("\n--- Fashion App Menu ---")

        print("1. View Categories")

        print("2. Choose Outfit")

        print("3. Suggest Random Outfit")

        print("4. Exit")

    def view_categories(self):

        print("\nAvailable Categories:")

        for cat in self.categories:

            print(f"- {cat}")

    def choose_outfit(self):

        category = input("Enter category name: ")

        if category in self.categories:

            print(f"Outfits in {category}:")

            for outfit in self.categories[category]:

                print(f"- {outfit}")

        else:

            print("Category not found.")

    def suggest_outfit(self):

        category = random.choice(list(self.categories.keys()))

        outfit = random.choice(self.categories[category])

        print(f"\nTry this {category} outfit: {outfit}")

def main():

    app = FashionApp()

    while True:

        app.show_menu()

        choice = input("Choose an option (1-4): ")

        if choice == "1":

            app.view_categories()

        elif choice == "2":

            app.choose_outfit()

        elif choice == "3":

            app.suggest_outfit()

        elif choice == "4":

            print("Goodbye!")

            break

        else:

            print("Invalid choice, Try again.")

if __name__ == "__main__":

    main()                                                             

