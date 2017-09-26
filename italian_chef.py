choice = None
while (choice == None):
  choice = input("Would you like pizza or pasta? ")
  if (choice == "pizza"):
    choice = choice + " " + \
    input("Which pizza would you like, hawaiian or pepperoni?")
  elif (choice == "pasta"):
    choice = choice + " " + \
    input("Which pasta would you like, spaghetti or macaroni?")
  else:
    # Choice was invalid, reset to None and retry
    choice = None
    print("Sorry, we don't have it, try again")

print("You have selected " + choice)
