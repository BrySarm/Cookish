import random

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.level = 1
        self.exp = 0

class Game:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.verbs = {
            1: ["chop", "slice", "dice"],
            2: ["boil", "simmer", "steam"],
            3: ["fry", "sauté", "grill"]
        }

    def register(self, username, password):
        if username not in self.users:
            self.users[username] = User(username, password)
            print(f"User {username} registered successfully!")
        else:
            print("Username already exists. Please choose another.")

    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            self.current_user = self.users[username]
            print(f"Welcome back, {username}!")
            return True
        else:
            print("Invalid username or password.")
            return False

    def play_level(self):
        if not self.current_user:
            print("Please log in first.")
            return

        print(f"\nLevel {self.current_user.level} - Learn and Cook!")
        verbs = self.verbs[min(self.current_user.level, max(self.verbs.keys()))]
        verb = random.choice(verbs)
        
        print(f"Your task: {verb.capitalize()} the ingredients.")
        action = input("What do you do? ").lower()

        if action == verb:
            print("Correct! You completed the cooking task.")
            self.current_user.exp += 10
            if self.current_user.exp >= self.current_user.level * 20:
                self.current_user.level += 1
                print(f"Congratulations! You've reached level {self.current_user.level}!")
        else:
            print(f"Oops! The correct action was to '{verb}'. Try again!")

    def main_menu(self):
        while True:
            print("\n--- Cooking Game Menu ---")
            print("1. Register")
            print("2. Login")
            print("3. Play")
            print("4. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.register(username, password)
            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.login(username, password)
            elif choice == '3':
                self.play_level()
            elif choice == '4':
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game = Game()
    game.main_menu()
