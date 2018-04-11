import random

def create_deck():
  deck = []
  for color in ["red","blue","green","yellow"]: 
    for num in range(10):
      print(color,num)
      deck.append((color,num))
  return deck

def draw_card(deck):
	card = random.choice(deck)
	deck.remove(card)
	return card 

def get_hand(deck):
	hand = []
	for count in range(8):
		hand.append(draw_card(deck))
	return hand

def print_hand(hand):
  for count in range(len(hand)):
    print(str(count) + ": " + str(hand[count]))


# driver code		
deck = create_deck()
hand1 = get_hand(deck)
hand2 = get_hand(deck)
topCard = draw_card(deck)

while True:
	print("This card is on top: " + str(topCard))
	print("Player 1, here is your hand:")
	print_hand(hand1)
	possible = input ("Player 1, is there a card you can play?")
	if possible == "yes":
		num = None
		while num == None or (hand1[num][0] != topCard[0] and hand1[num][1] != topCard[1]):
			num = int(input("Player 1, which card do you want to play?"))
		topCard = hand1[num]
		hand1.remove(topCard)
		if len(hand1) == 0:
			print("Player 1, you won!")
			break
	elif possible == "no":
		draw = draw_card(deck)
		print("Ok, you drew " + str(draw))
		hand1.append(draw)
		
	print("This card is on top: " + str(topCard))
	print("Player 2, here is your hand:")
	print_hand(hand2)
	possible = input ("Player 2, is there a card you can play?")
	if possible == "yes":
		num = None
		while num == None or (hand2[num][0] != topCard[0] and hand2[num][1] != topCard[1]):
			num = int(input("Player 2, which card do you want to play?"))
		topCard = hand2[num]
		hand2.remove(topCard)
		if len(hand2) == 0:
			print("Player 2, you won!")
			break
	elif possible == "no":
		draw = draw_card(deck)
		print("Ok, you drew " + str(draw))
		hand2.append(draw)
	
