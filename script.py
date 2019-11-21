import random
money = 100



## Coin Flip
def coin_flip(guess, bet):
  print("COIN FLIP:")
  print("---------------------")
  print("RULES: Guess 'Heads' or 'Tails'. Flip the coin.")
  print("-----------------------")
  ## Make sure the guess is valid!
  if guess != "Heads" and guess != "Tails":
    print("GAME INVALID. Please double check the spelling of your guess!")
    print("--------------------")
  ## Make sure the bet is valid!
  if bet < 0:
    print("GAME INVALID. You can't bet negative money!")
    print("-----------------------")
  if bet > money:
    print("GAME INVALID. Don't bet more than you have!")
    print("-----------------------")
  print("Your guess is " + guess + ". Your bet is " + str(bet) + " dollars. Now let's flip the coin!")
  print("----------------------")
  ## Flip the coin.
  coin = random.randint(1, 2)
  if coin == 1:
    print("Heads!")
    print("---------------------")
  if coin == 2:
    print("Tails!")
    print("---------------------")
  ## Determine if won or lost.
  if (guess == "Heads" and coin == 1) or (guess == "Tails" and coin == 2):
    print("You win! Collect your bet of " + str(bet) + " dollars.")
    print("------------------")
    return +bet
  if (guess == "Heads" and coin == 2) or (guess == "Tails" and coin == 1):
    print("You lose! Relinquish your bet of " + str(bet) + " dollars.")
    print("------------------")
    return -bet
  
  
  
## Cho-Han
def cho_han(guess, bet):
  print("CHO HAN:")
  print("-------------------")
  print("RULES: Guess if the sum of two dice will be 'Odd' or 'Even'.")
  print("------------------------")
  ## Make sure the guess is valid.
  if guess != "Odd" and guess != "Even":
    print("GAME INVALID! Please check the spelling of your guess!")
    print("-----------------------")
  ## Make sure the bet is valid.
  if bet < 0:
    print("GAME INVALID. You can't bet negative money!")
    print("----------------")
  if bet > money:
    print("GAME INVALID. You can't bet more than you have!")
    print("-------------------")
  print("Your guess is " + guess + ". Your bet is " + str(bet) + " dollars. Now let's roll the dice!")
  print("--------------------------")
  ## Roll dice.
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  sum = die1 + die2
  print("The sum of the dice is " + str(sum) + ".")
  print("-----------------------")
  ## Odd or even?
  if sum % 2 == 0:
    print("Even!")
    print("------------------")
  if sum % 2 == 1:
    print("Odd!")
    print("--------------------")
  ## Won or lost?
  if (guess == "Even" and sum % 2 == 0) or (guess == "Odd" and sum % 2 == 1):
    print("You win! Collect your bet of " + str(bet) + " dollars.")
    print("-------------------")
    return +bet
  if (guess == "Even" and sum % 2 != 0) or (guess == "Odd" and sum % 2 != 1):
    print("You lose! Relinquish your bet of " + str(bet) + " dollars.")
    print("-----------------")
    return -bet
    
    
    
## Pick a Card
def pick_a_card(bet):
  print("PICK A CARD:")
  print("------------------")
  print("RULES: You and your opponent each draw a card. The person with the higher card wins. Note: Ace = 1, Jack = 11, Queen = 12, and King = 13. All other cards reflect their face value.")
  print("----------------")
  ## How much did you bet?
  print("You bet " + str(bet) + " dollars.")
  print("---------------------")
  ## Determine if bet is valid.
  if bet > money:
    print("GAME INVALID. You can't bet more than you have!")
    print("------------")
  if bet < 0:
    print("GAME INVALID. You can't bet negative money!")
    print("------------------")
  ## Pick a card.
  your_card = random.randint(1,13)
  opponent_card = random.randint(1,13)
  print("You picked card " + str(your_card) + ".")
  print("Your opponent picked card " + str(opponent_card) + ".")
  print("------------------")
  ## Determine winner.
  if your_card > opponent_card:
    print("You win! Collect your bet of " + str(bet) + " dollars.")
    print("------------------")
    return +bet
  if opponent_card > your_card:
    print("You lose! Relinquish your bet of " + str(bet) + " dollars.")
    print("----------------")
    return -bet
  else:
    print("Tie! You did not win or lose money.")
    print("---------------")
    return 0

    
    
## Roulette
def roulette(guess, bet):
  print("ROULETTE:")
  print("----------------------")
  print("RULES: Guess if the ball will land on an 'Odd' or 'Even' number (excluding zero) OR place your bets on a specific number OR guess if the number will be high (19-36) or low (1-18). NOTE: if betting on '00', please enter the number in quotation marks.")
  print("-------------------------")
  print("You placed your bet of " + str(bet) + " dollars on " + str(guess) + ".")
  print("----------------")
  ## Determine if guess is valid.
  if (guess != "Odd" and guess != "Even" and guess != "00" and guess != "High" and guess != "Low") and (guess < 0 or guess > 36):
    print("GAME INVALID! Please check your guess!")
    print("--------------")
  ## Determine if bet is valid.
  if bet < 0:
    print("GAME INVALID! You can't bet negative money!")
    print("--------------")
  if bet > money:
    print("GAME INVALID! You can't bet more than you have!")
    print("--------------")
  ## Spin the wheel.
  result = random.randint(0, 37)
  if 0 <= result <= 36:
    print("The ball landed on " + str(result) + ".")
    print("-------------")
  if result == 37:
    print("The ball landed on 00.")
    print("---------------")
  ## Determine if won.
  if (guess == "Even" and result % 2 == 0 and result != 0) or (guess == "Odd" and result % 2 == 1) or (guess == "High" and 19 <= result <= 36) or (guess == "Low" and 1 <= result <=18):
    print("You win! Collect your bet of " + str(bet) + " dollars.")
    print("---------------")
    return +bet
  if (guess == result) or (guess == "00" and result == 37):
    print("You win! Collect THIRTY-FIVE TIMES your bet of " + str(bet) + " dollars, an incredible " + str(bet * 35) + " DOLLARS!!!")
    print("---------------")
    return +bet*35
  else:
    print("You lose. Please relinquish your bet of " + str(bet) + " dollars.")
    print("----------------")
    return -bet

  
  
## Play some games and see how much money you end up with.
money += coin_flip("Heads", 10)
money += coin_flip("Tails", 15)
money += cho_han("Odd", 10)
money += cho_han("Even", 20)
money += pick_a_card(25)
money += roulette("Low", 20)
money += roulette("00", 5)
money += roulette(9, 10)
print("Your money is now " + str(money) + " dollars.")
