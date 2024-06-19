import random
import locale

# Set locale for formatting numbers with commas
locale.setlocale(locale.LC_ALL, '')

class Wallet:
    def __init__(self, initial_balance=250000):
        self.balance = initial_balance
        self.chips = 0

    def add_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def add_chips(self, amount):
        self.chips += amount

    def remove_chips(self, amount):
        if self.chips >= amount:
            self.chips -= amount
            return True
        else:
            return False

    def check_balance(self):
        return self.balance

    def check_chips(self):
        return self.chips

class CasinoGame:
    def __init__(self):
        self.wallet = Wallet()

    def display_options(self):
        print("\nWelcome to the Casino!")
        print("What would you like to do?")
        print("1. Slot Machine")
        print("2. Roulette")
        print("3. Wheel of Fortune")
        print("4. Dice Game")
        print("5. Blackjack")
        print("6. Buy Chips")
        print("7. Check Wallet Balance")
        print("8. Check Wallet Chips")
        print("9. Exit")

    def play(self):
        self.display_options()
        while True:
            self.display_chips()
            choice = input("\nCasino ==> ")

            if choice == '1':
                self.play_slot_machine()
            elif choice == '2':
                self.play_roulette()
            elif choice == '3':
                self.play_wheel_of_fortune()
            elif choice == '4':
                self.play_dice_game()
            elif choice == '5':
                self.play_blackjack()
            elif choice == '6':
                self.buy_chips()
            elif choice == '7':
                print("Wallet Balance: ${:,}".format(self.wallet.check_balance()))
            elif choice == '8':
                print("Wallet Chips:", self.wallet.check_chips())
            elif choice == '9':
                print("Exiting the Casino. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_chips(self):
        chips_count = self.wallet.check_chips()
        balance_total = self.wallet.check_balance()
        chips_visual = """
  00000  
 0     0 
 0 RED 0 ({:,} Chips) (${:,} Total)
 0     0 
  00000  
""".format(chips_count, balance_total)
        print(chips_visual)

    def play_slot_machine(self):
        print("\nPlaying Slot Machine...")
        bet_amount = int(input("Enter your bet amount in chips: "))
        if self.wallet.remove_chips(bet_amount):
            symbols = ['Cherry', 'Bell', 'Bar', 'Seven', 'Diamond']
            result = [random.choice(symbols) for _ in range(3)]
            print("Slot Machine Result:", result)
            if result.count('Cherry') == 3:
                self.wallet.add_chips(bet_amount * 50)
                print("Congratulations! You won 50 times your bet!")
            elif result.count('Cherry') == 2:
                self.wallet.add_chips(bet_amount * 5)
                print("Congratulations! You won 5 times your bet!")
            elif 'Seven' in result:
                self.wallet.add_chips(bet_amount * 10)
                print("Congratulations! You won 10 times your bet!")
            else:
                print("Sorry, you didn't win this time.")
        else:
            print("Insufficient chips in wallet.")

    def play_roulette(self):
        print("\nPlaying Roulette...")
        bet_amount = int(input("Enter your bet amount in chips: "))
        if self.wallet.remove_chips(bet_amount):
            colors = ['Red', 'Black']
            result_color = random.choice(colors)
            result_number = random.randint(0, 36)
            print("Roulette Result:", result_number, result_color)
            if result_color == 'Red':
                if result_number % 2 == 0:
                    self.wallet.add_chips(bet_amount)
                    print("Congratulations! You won!")
                else:
                    print("Sorry, you lost.")
            elif result_color == 'Black':
                if result_number % 2 != 0:
                    self.wallet.add_chips(bet_amount)
                    print("Congratulations! You won!")
                else:
                    print("Sorry, you lost.")
        else:
            print("Insufficient chips in wallet.")

    def play_wheel_of_fortune(self):
        print("\nPlaying Wheel of Fortune...")
        bet_amount = int(input("Enter your bet amount in chips: "))
        if self.wallet.remove_chips(bet_amount):
            outcomes = ['Bankrupt', 'Lose Turn', '100', '200', '500', '1000']
            result = random.choice(outcomes)
            print("Wheel of Fortune Result:", result)
            if result == 'Bankrupt' or result == 'Lose Turn':
                print("Sorry, you lost.")
            else:
                amount_won = int(result)
                self.wallet.add_chips(amount_won * bet_amount)
                print(f"Congratulations! You won {amount_won} times your bet!")
        else:
            print("Insufficient chips in wallet.")

    def play_dice_game(self):
        print("\nPlaying Dice Game...")
        bet_amount = int(input("Enter your bet amount in chips: "))
        if self.wallet.remove_chips(bet_amount):
            dice_roll = random.randint(1, 6)
            print("Dice Roll Result:", dice_roll)
            if dice_roll % 2 == 0:
                self.wallet.add_chips(bet_amount)
                print("Congratulations! You won!")
            else:
                print("Sorry, you lost.")
        else:
            print("Insufficient chips in wallet.")

    def play_blackjack(self):
        print("\nPlaying Blackjack...")
        bet_amount = int(input("Enter your bet amount in chips: "))
        if self.wallet.remove_chips(bet_amount):
            player_cards = [random.randint(1, 10) for _ in range(2)]
            dealer_cards = [random.randint(1, 10) for _ in range(2)]
            print("Your Cards:", player_cards)
            print("Dealer's Cards:", [dealer_cards[0], '*'])
            player_score = sum(player_cards)
            while player_score < 21:
                action = input("Do you want to hit (h) or stand (s)? ")
                if action == 'h':
                    new_card = random.randint(1, 10)
                    player_cards.append(new_card)
                    player_score += new_card
                    print("Your Cards:", player_cards)
                    if player_score > 21:
                        print("Bust! You lose.")
                        break
                elif action == 's':
                    dealer_score = sum(dealer_cards)
                    print("Dealer's Cards:", dealer_cards)
                    while dealer_score < 17:
                        new_card = random.randint(1, 10)
                        dealer_cards.append(new_card)
                        dealer_score += new_card
                        print("Dealer's Cards:", dealer_cards)
                    if dealer_score > 21 or player_score > dealer_score:
                        self.wallet.add_chips(bet_amount * 2)
                        print("Congratulations! You won!")
                    else:
                        print("Sorry, you lost.")
                    break
                else:
                    print("Invalid action. Please enter 'h' or 's'.")
        else:
            print("Insufficient chips in wallet.")

    def buy_chips(self):
        print("\nBuying Chips...")
        while True:
            try:
                chip_amount = int(input("Enter the number of chips you want to buy: "))
                if chip_amount <= 0:
                    raise ValueError("Invalid chip amount")
                chip_prices = {
                    1: 1,
                    10: 9,
                    100: 80,
                    1000: 700,
                    10000: 6000,
                    100000: 50000,
                    1000000: 400000,
                }
                if chip_amount in chip_prices:
                    cost = chip_prices[chip_amount]
                    if self.wallet.withdraw_money(cost):
                        self.wallet.add_chips(chip_amount)
                        print(f"Bought {chip_amount} chips for ${cost}")
                        break
                    else:
                        print("Insufficient balance to buy chips")
                else:
                    print("Invalid chip amount")
            except ValueError as e:
                print(e)

casino_game = CasinoGame()
casino_game.play()
