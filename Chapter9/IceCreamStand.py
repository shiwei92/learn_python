class IceCreamStand():
	def __init__(self):
		self.flavors=["pepper","apple","banana","peach"]
	def describe_flavor(self):
		print("we supply flavors as it shows blow:")
		for flavor in self.flavors:
			print("--"+flavor)
ice_cream=IceCreamStand()
ice_cream.describe_flavor()
	