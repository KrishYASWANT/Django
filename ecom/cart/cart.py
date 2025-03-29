""" class Cart(): 
    def __init__(self, request): 
        self.session = request.session 
            # Get the current session key if it exists 
        cart = self.session.get('session_key') 
            # If the user is new, no session key! Create one! 
        if 'session_key' not in request.session: 
            cart = self.session['session_key'] = {} 
            # Make sure cart is available on all pages of site 
        self.cart = cart """
from store.models import Product
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart
        
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'Price': str(product.price)}
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True
        
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # Get IDS from Cart
        product_ids= self.cart.keys()
        # Use IDS to look up products in Database
        products = Product.objects.filter(id__in=product_ids)
        # Return Products
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities