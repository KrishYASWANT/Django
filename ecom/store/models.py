from django.db import models
import datetime

# Categories of Products
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
        
        
        
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0 ,decimal_places=2, max_digits= 10)
    catagory = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    discription= models.CharField(max_length=255, blank=True, null= True, default= ' ')
    image = models.ImageField(upload_to='uploads/product/')
    
    # Add sale stuff
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0 ,decimal_places=2, max_digits= 10)
    
    def __str__(self):
        return self.name
class Customer(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    phone       = models.CharField(max_length=10)
    email       = models.EmailField(max_length=254)
    password    = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)
    quantity = models.IntegerField(default=1)
    status = models.BooleanField(default=False)
    
    
    
    def __str__(self):
        return self.product