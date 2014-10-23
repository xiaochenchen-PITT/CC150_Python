class OnlyOne:
	'''Singleton is a way to provide one and only one object of a class.
	One of them is to nest an inner class into a class and override the attributes.
	'''
	class __OnlyOne:
		'''This inner class is named with a double underscore, 
		it is private so the user cannot directly access it.--Python Grammer

		The inner class contains all the methods that you would normally put in the
		class if it weren't going to be a singleton. And then it is wrapper in the
		outer class which controls creation by using its constructor.
		'''
		def __init__(self, val):
			self.val = val

	instance = None

	def __init__(self, val):
		if not OnlyOne.instance:
			OnlyOne.instance = OnlyOne.__OnlyOne(val)
		else:
			OnlyOne.instance.val = val	# overrides the attr

	def __str__(self):
		return repr(self) + ' ' + self.val
		# repr(obj) : compute the "official" string representation of obj

	def __getattr__(self, name):
		'''getattr(self, name) returns self.name

		Called when an attribute lookup has not found the attribute in the usual places 
		(i.e. it is not an instance attribute nor is it found in the class tree for self)
		'''
		return getattr(self.instance, name)	# no matter how many objects you created
								# for OnlyOne class, it will all redircted to the
								# __OnlyOne class object -- instance


x = OnlyOne('aaa')
print x

y = OnlyOne('bbb')
print y

z = OnlyOne('ccc')
print z

#try print x and y again...
print x
print y