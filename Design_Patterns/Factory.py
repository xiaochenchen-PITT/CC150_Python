'''The essence of Factory Design Pattern is to "Define a factory creation 
method(interface) for creating objects for different classes. 
And the factory instance is to instantiate other class instances.
The Factory method lets a class defer instantiation to subclasses." 

Key point of Factory Design Pattern is--
Only when inheritance is involved is factory method pattern.
'''

class Button(object):
	"""class Button has 3 subclasses Image, Input and Flash."""
	def __init__(self):
		self.string  = ''

	def GetString(self):
		return self.string

class Image(Button):
	"""docstring for Image"""
	def __init__(self):
		self.string = 'string for Image.'

class Input(Button):
	"""docstring for Input"""
	def __init__(self):
		self.string = 'string for Input.'

class Flash(Button):
	"""docstring for Flash"""
	def __init__(self):
		self.string = 'string for Flash.'

class ButtonFactory:
	"""ButtonFactory is the Factory class for Button, its instance is to
	instantiate other button class instances"""
	buttons = {'image': Image, 'input': Input, 'flash': Flash} # value is class
	def create_button(self, typ):
		return self.buttons[typ]() # () is for instantiating class !!!
									# eg. s = Solution()

button_obj = ButtonFactory() # Factory instance is for instantiating other class 
for b in button_obj.buttons:
	print button_obj.create_button(b).GetString()

# print button_obj.buttons['image']
# print Flash

'''Another example/way for Factory design pattern.
Blackjack cards example.
'''
class CardFactory:  # Factory class
	def Newcard(self, rank, suit):
		if rank == 1:
			return ACE(rank, suit)
		elif rank in [11, 12, 13]:
			return FaceCard(rank, suit)
		else:
			return Card(rank, suit)

class Deck:
	def __init__(self, ):
		factory = CardFactory()
		self.cards = [factory.Newcard(rank + 1, suit) for suit in ['Spade', 'Heart', 'Club', 'Diamond'] for rank in range(13)]
		# Above is a huge list comprehesive!!

class Card:
	"""Base class: Normal card"""
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		self.val = rank

	def __str__(self):
		return '{1} {0}'.format(self.rank, self.suit)

	def GetSoftvalue(self):
		return self.val

	def GetHardvalue(self):
		return self.val

class ACE(Card):
	def __init__(self, rank, suit):
		Card.__init__(self, rank, suit)

	def __str__(self):
		return '{1} {0}'.format('A', self.suit)

	def GetSoftvalue(self):
		return 11

	def GetHardvalue(self):
		return 1

class FaceCard(Card):
	"""J, Q, K."""
	def __init__(self, rank, suit):
		Card.__init__(self, rank, suit)
		self.val = 10

	def __str__(self):
		label = ('J', 'Q', 'K')[self.rank - 11]
		return '{1} {0}'.format(label, self.suit)
		
deck = Deck()
for card in deck.cards:
	print card
			
		

		