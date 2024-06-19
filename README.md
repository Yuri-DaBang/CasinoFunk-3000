# CasinoFunk-3000: Roll the Dice and Pray 🎰🎲

## Welcome to the Shitty Casino Game! 🎉

Experience the thrill of our half-baked casino adventure, where every game is a questionable decision.

## Games That Will Make You Go 🤪

### Dice Delights 🎲💫

Roll the dice and hope for the best! Whether you're a risk-taker or just rolling with it, let's see where luck takes you.

### Wheel of Misfortune 🎡😬

Spin the wheel and hold your breath as it decides your fate. Will you hit the jackpot or end up with a sour spin?

### Card Craziness 🃏🤔

Play your cards right (or wrong) in our chaotic card games. Master the art of deception or play it safe — the choice is yours!

### Slot Machine 🎰

Pull the lever and watch the reels spin! With symbols like Cherry, Bell, and Seven, every pull is a chance to win big or walk away empty-handed.

### Roulette 🎲

Place your bets and watch the wheel spin! Will you choose Red or Black? Test your luck with this classic game of chance.

### Wheel of Fortune 🎡

Take a spin on the Wheel of Fortune! Will you land on a prize or face the dreaded Bankrupt? Spin wisely to win chips and avoid pitfalls.

### Dice Game 🎲

Roll the dice and hope for an even number! It's simple, yet addictive — can you beat the odds and come out a winner?

### Blackjack 🃏

Get as close to 21 as possible without going bust! Play against the dealer in this strategic card game. Hit, stand, or double down — the choice is yours!

## Features

### Play Games 🎮

Step right up and dive into the excitement! Choose from a variety of thrilling casino games and see where luck takes you.

### Buy Chips 💰

Need more chips to keep playing? Purchase additional chips to stay in the game and increase your chances of hitting the jackpot.

### Check Wallet Balance 💼

Want to know how much you've won or lost? Check your wallet balance to track your casino earnings and spending.

### Check Wallet Chips 🎟️

Keep track of your chips at all times! Check your chip count to see how much you have left for playing your favorite games.

### Exit 🚪

Ready to cash out? Choose "Exit" to leave the casino and reflect on your thrilling (and maybe profitable) gaming experience.


## Prizes That Make You Question Reality 🏆

Win big 💰, lose bigger 💸 — it's all part of the thrill (and agony) of our uniquely shitty casino experience.

## Embrace the Chaos 🎯

Bet wisely (or not) and ride the rollercoaster of unpredictability. Ready to test your luck in the craziest casino this side of the internet? Let's play! 🎰💥


### Explanation:

1. **Imports**: 
   - `random`: Used for generating random numbers and choices in the casino games.
   - `locale`: Used to format numbers with commas, making large numbers more readable.

2. **Wallet Class**:
   - Manages the player's balance and chips in the casino.
   - Methods include adding and withdrawing money, adding and removing chips, and checking balances.

3. **CasinoGame Class**:
   - Handles the main casino game logic and user interactions.
   - Includes methods for displaying game options, playing each game (slot machine, roulette, wheel of fortune, dice game, blackjack), buying chips, and checking wallet balances.

4. **Display Options Method**:
   - Prints the main menu of game options when the game starts.

5. **Play Method**:
   - Controls the flow of the game, prompting users for input and calling the corresponding game method based on their choice.

6. **Display Chips Method**:
   - Prints a visual representation of the player's chips and total balance.

7. **Game Methods**:
   - Each game method (`play_slot_machine`, `play_roulette`, `play_wheel_of_fortune`, `play_dice_game`, `play_blackjack`) implements the rules and logic for playing each respective game using random numbers.

8. **Buy Chips Method**:
   - Allows the player to purchase chips with predefined prices. It checks if the player has enough balance and handles errors for invalid chip amounts.

9. **Main Execution**:
   - Creates an instance of `CasinoGame` and starts the game loop with `casino_game.play()`.

This structured Python code simulates a casino environment where players can interact through a command-line interface, play different games, manage their wallet, buy chips, and exit when done. Adjustments and additional game logic can be added as needed within each game method.

