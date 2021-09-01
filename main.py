from replit import clear
print("Welcome to the blind auction")
should_continue = True
def highest_bidder(bidding_record):
  highest_bid =0
  winner =""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner=bidder
  print(f"The winner is {bidder} with {highest_bid}")
while should_continue:

  key = input("What is your name?")
  value = int(input("How much you want to bid $"))
  dict={}
  dict[key]= value
  
  ask=input("Is there more player? 'YES or 'NO'\n").lower()
  if ask == "no":
    should_continue = False
    highest_bidder(dict)
  elif ask =="yes":
    clear()
    



    

