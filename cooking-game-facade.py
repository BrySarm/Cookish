# Import the original game code
from cooking-game-english-learning import Game, User

class CookingGameFacade:
    def __init__(self):
        self.game = Game()

    def create_account(self, username, password):
        self.game.register(username, password)

    def start_session(self, username, password):
        return self.game.login(username, password)

    def start_game(self):
        if not self.game.current_user:
            print("Please log in first.")
            return
        self.game.play_level()

    def get_user_stats(self):
        if not self.game.current_user:
            return None
        user = self.game.current_user
        return {
            "username": user.username,
            "level": user.level,
            "experience": user.exp
        }

    def run_game(self):
        while True:
            print("\n--- Cooking Game ---")
            print("1. Create Account")
            print("2. Log In")
            print("3. Quit")
            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.create_account(username, password)
            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.start_session(username, password)
            elif choice == '3':
                self.start_game()
            elif choice == '4':
                stats = self.get_user_stats()
                if stats:
                    print(f"User: {stats['username']}")
                    print(f"Level: {stats['level']}")
                    print(f"Experience: {stats['experience']}")
                else:
                    print("Please log in to view stats.")
            elif choice == '2AAAAAAAAAAAAAAAAAAAQS                EWS':
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    facade = CookingGameFacade()
    facade.run_game()
