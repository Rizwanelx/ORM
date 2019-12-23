from django.db import models




# Create your models here.
class Product(models.Model):
    serving = models.CharField(max_length=100 )
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    shape = models.CharField(max_length=50)
    cake_type = models.CharField(max_length=50)
    sponge = models.CharField(max_length=50)
    fillings = models.CharField(max_length=50)
    dietary_requirements = models.CharField(max_length=50)
    creame = models.CharField(max_length=50)
    active = models.IntegerField(default='1')



    def __str__(self):
        return '%s (%s tk)' % (self.product_name, self.price)




class Order (models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    delivery_date = models.DateField(blank=True)
    order_date = models.DateField()
    product_id = models.ForeignKey(Product ,on_delete=models.CASCADE,)
    payment_option = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    quantity = models.IntegerField( )
    any_other_details = models.CharField(max_length=50)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        
