#from cart.cart import Cart

# Create context processor so our cart can work on all pages of the site
def cart(request):
    from cart.cart import Cart
	# Return the default data from our Cart
    return {'cart': Cart(request)}