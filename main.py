from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo+"\n\n")
end_game = False
bid_price = {}

while not end_game:
  name = input("What is your name? : ")
  bid = int(input("What is your bid? : $"))
  bid_price[name] = bid
  continue_bid = input("Is there anyone in the bid? (Type 'yes' or 'no') : ").lower()
  if(continue_bid == 'no'):
    end_game = True

  clear()

max = 0
max_bidder = ""
for key in bid_price:
  if bid_price[key] > max:
    max = bid_price[key]
    max_bidder = key

print(f"The winner is {max_bidder} with a bid of {max}")