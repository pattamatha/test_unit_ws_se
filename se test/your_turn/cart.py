from item_db import ItemDatabase

MAX_QUANTITY_PER_PRODUCT = 10
MAX_ITEM = 5

class Cart:
	def __init__(self):
		self.logged_in = False
		self.carts = {}

	def authenticate(self, auth_service, username, password):
		self.logged_in = auth_service.login(username,password)

	def add_to_cart(self, item):
		if self.logged_in:
			if item not in self.carts:
				if len(self.carts) == MAX_ITEM-1:
					raise Exception("You can't add more items.")
				self.carts[item] = 0
			if self.carts[item] <= MAX_QUANTITY_PER_PRODUCT:
				self.carts[item]+=1
			else:
				raise Exception("You can't add more than {} per item".format(MAX_QUANTITY_PER_PRODUCT))
		else:
			print("You need to login first.")

	def total_price(self):
		if self.logged_in:
			if len(self.carts) == 0:
				return 0

			item_db = ItemDatabase()

			total_price = 0
			for item, quantity in self.carts.items():
				total_price += item_db.get_price(item) * quantity
			return total_price
		else:
			print("You need to login first.")
			return None