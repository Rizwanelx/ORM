from django.db import models
from datetime import datetime    


class Order(models.Model):
    SERVINGS = (
        ('S', '5-10'),
        ('M', '10-15'),
        ('L', '15-20'),
        ('XL', '20-30'),
        ('XXL', '30-40'),

    )
    SHAPE = (
        ('S', 'AS SHOWN'),
        ('M', 'SQUARE'),
        ('L', 'ROUND'),

    )
    TYPE = (
        ('S', 'ICING'),
        ('M', 'FRESH CREAME'),
        ('L', 'CHOLOCATE FRESH CREAME'),
        ('XL', 'BUTTER CREAME'),
        ('XXL', 'CHOLOCATE BUTTER CREAME'),

    )

    SPONGE = (
        ('S', 'VANILA'),
        ('M', 'CHOLOCATE')

    )
    CREAME = (
        ('S', 'VANILA CREAME'),
        ('M', 'CHOLOCATE CREAME')

    )

    FILLING = (
        ('S', 'CHOLOCATE BUTTER CREAME'),
        ('M', 'CHOLOCATE BUTTER CREAME + JAM'),
        ('L', 'WHITE BUTTER CREAME'),
        ('XL', 'WHITE BUTTER CREAME + JAM'),

    )
    DIETARY_REQUIREMENTS= (
        ('S', 'NO DIETARY_REQUIREMENTS'),
        ('M', 'EAGGLESS'),
        ('L', ' GLUTEN FREE \ WHEAT FREE'),
        ('XL', 'NUTS'),

    )
    order_id = models.AutoField(primary_key=True)
    name_of_cake = models.CharField(max_length=60)
    serving = models.CharField(max_length=50, choices=SERVINGS)
    shape = models.CharField(max_length=50, choices=SHAPE)
    cake_type = models.CharField(max_length=50, choices=TYPE)
    sponge = models.CharField(max_length=50, choices=SPONGE)
    fillings = models.CharField(max_length=50, choices=FILLING)
    dietary_requirements = models.CharField(max_length=50, choices=DIETARY_REQUIREMENTS)
    quantity = models.IntegerField()
    collection_time = models.DateTimeField(default=datetime.now, blank=True)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    deposite = models.IntegerField()
    due = models.IntegerField()
    total = models.IntegerField()
    any_other_details = models.CharField(max_length=50)
    message = models.CharField(max_length=50)




    def __str__(self):
        return self.name_of_cake
        
