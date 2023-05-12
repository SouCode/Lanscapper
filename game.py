import os
import platform

def clear_screen():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")



def landscaper_game(days_worked: int, earnings_per_day: int) -> int:
    total_earnings = days_worked * earnings_per_day
    return total_earnings

def main():
    clear_screen()  # Clear the terminal when the game is started
    print("Welcome to the Landscaper game!")
    print("You are starting a landscaping business, but all you have are your teeth.")
    print("Using just your teeth, you can spend the day cutting lawns and make $1. You can do this as much as you want.")
    
    total_earnings = 0
    earnings_per_day = 1
    has_scissors = False
    has_lawnmower = False
    has_battery_lawnmower = False
    has_students = False
    
    
    yourMoney = f"You currently have ${total_earnings}"

    
    while True:
        try:
            days_worked = int(input("Enter the number of days you would like to work (or type 'exit' to quit): "))
            tool_name = "starving students" if has_students else "fancy battery-powered lawnmower" if has_battery_lawnmower else "old-timey push lawnmower" if has_lawnmower else "rusty scissors" if has_scissors else "teeth"
            earned_money = landscaper_game(days_worked, earnings_per_day)
            total_earnings += earned_money
            print(f"Using {tool_name} for {days_worked} days, you made ${earned_money}.")
            print(f"You currently have ${total_earnings}")
        
            if not has_scissors and total_earnings >= 5:
                buy_scissors = input("Do you want to buy rusty scissors for $5? (yes or no): ").lower()
                if buy_scissors in ['yes', 'y']:
                    total_earnings -= 5
                    earnings_per_day = 5
                    has_scissors = True
                    clear_screen()
                    print("You bought rusty scissors. Your earnings per day have increased to $5!")
                    print(f"You currently have ${total_earnings}")
                
            if not has_lawnmower and has_scissors and total_earnings >= 25:
                buy_lawnmower = input("Do you want to buy an old-timey push lawnmower for $25? (yes or no): ").lower()
                if buy_lawnmower in ['yes', 'y']:
                    total_earnings -= 25
                    earnings_per_day = 50
                    has_lawnmower = True
                    clear_screen() 
                    print("You bought an old-timey push lawnmower. Your earnings per day have increased to $50!")
                    print(f"You currently have ${total_earnings}")
        
            if not has_battery_lawnmower and has_lawnmower and total_earnings >= 250:
                buy_battery_lawnmower = input("Do you want to buy a fancy battery-powered lawnmower for $250? (yes or no): ").lower()
                if buy_battery_lawnmower in ['yes', 'y']:
                    total_earnings -= 250
                    earnings_per_day = 100
                    has_battery_lawnmower = True
                    clear_screen() 
                    print("You bought a fancy battery-powered lawnmower. Your earnings per day have increased to $100!")
                    print(f"You currently have ${total_earnings}")
                
            if not has_students and has_battery_lawnmower and total_earnings >= 500:
                hire_students = input("Do you want to hire a team of starving students for $500? (yes or no): ").lower()
                if hire_students in ['yes', 'y']:
                    total_earnings -= 500
                    has_students = True
                    clear_screen() 
                    print("You hired a team of starving students!")
                    print(f"You currently have ${total_earnings}")

            
            continue_working = input("Do you want to continue working? (yes or no): ").lower()
            if continue_working != 'yes':
                print("Goodbye!")
                break
                
        except ValueError:
            print("Invalid input. Please enter a valid number of days or type 'exit' to quit.")
        except KeyboardInterrupt:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
