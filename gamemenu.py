import os
import json
documents =r"c:\Users\parga\OneDrive\Documents"
os.makedirs(documents,exist_ok=True)

file_path = os.path.join(documents, "games.json")
print(f"Games list will be saved to: {file_path}")


games =[]

try:
   with open(file_path, "r") as file:
     games =json.load(file)
except FileNotFoundError:
   pass

def save_games():
   with open(file_path, "w") as file:
      json.dump(games, file , indent=4)


while True:
     print("MAIN____MENU")
     print(24 * "=")
     print("1. Add games")
     print("2. Remove games")
     print("3. Search games")
     print("4. Show games")
     print("5. Count games")
     print("6. Exit")
     print("7. Clear games list")
     print("8. Rename game")
     print(24 * "=")
     choice = input("Enter your choice (1-8): ")

     try:
         choice = int(choice)
     except ValueError:
         print("Invalid input. Please enter a valid number.")
         continue
     
     if choice == 1:
      try:
         a = input("how many games do you want to add?").strip()
         a = int(a)
      except ValueError:
         print("Invalid input. Please enter a valid number.")
         continue
      if a <= 0:
         print("Invalid input. Please enter a positive number.")
         continue

      for i in range(a):
         game_name = input("enter the game name: ").strip()

         if game_name == "":
             print("game name cannot be empty. Please enter a valid game name.")
         elif game_name in games:
             print("the game is already in your games list")
         else:
             games.append(game_name)
             save_games()
             print("the game is added to your games list")

      if len(games) > 0:
        for i, game in enumerate(games, start=1):
         print(f"{i}. {game}")
      else:
         print("no games added")
     elif choice == 2:
          print(" select the option to remove games")
          b = input(" which game do you want to remove? ").strip()
          if b in games:
            games.pop(games.index(b))
            save_games()
            print(f"{b} is removed from your games list")
          else:
            print(f"{b} is not found in your games list")
          

       
     elif choice == 3:
          print(" select the option to search games")
          c = input(" which game do you want to search? ").strip()
          if c in games:
            print(f"{c} is found in your games list")
          else:
            print(f"{c} is not found in your games list")

      
     elif choice == 4:
          print(" select the option to show games")
          if len(games) > 0:
            for i, game in enumerate(games, start=1):
              print(f"{i}. {game}")
          else:
            print("no games added")


     elif choice == 5:
          count = len(games)
          print(f"you have {count} games in your list")

     elif choice == 6:
          print("Exiting the program...")
          break
     elif choice == 7:
          print("warning: this will clear your games list")
          confirm = input("Are you sure you want to clear the games list? (yes/no): ").strip().lower()
          if confirm == "yes":
             games.clear()
             save_games()
             print("your games list is cleared")
          else:
             print("clear operation canceled")

     elif choice == 8:
        print("select the option to rename a game")
        old_name = input("Enter the name of the game you want to rename: ").strip()
        if old_name in games:
           new_name = input("Enter the new name for the game: ").strip()
           if new_name == "":
              print("New game name cannot be empty .please enter a valid game naem")
           elif new_name in games:
              print("The new game name already exists in your games list.")
           else:
              games[games.index(old_name)] = new_name
              save_games()
              print(f"{old_name} has been renamed to {new_name}.")
        else:
            print(f"{old_name} is not found in your games list.")

      

