def outer(number):

	def inner(base):

		return number*base
	return inner

square = outer(2)
