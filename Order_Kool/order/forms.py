from django.forms import ModelForm
from django import forms
from .models import Order, Product

class OrderForm(ModelForm):
    OPTIONS = (
        ('Pa','Postpay'),
        ('Prepay (Full)','Prepay (Full)'),
        ('Prepay (Half)', 'Prepay (Half)')
    )
    OPTIONS2 = (
        ('Confirm', 'Confirm'),
        ('Ready', 'Ready'),
        ('Send', 'Send'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled')
    )
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect)
    payment_option = forms.ChoiceField(choices=OPTIONS)
    product_id = forms.ModelChoiceField(queryset=Product.objects.filter(active='1'), empty_label='')
    delivery_date = forms.DateField(required=True)
    quantity = forms.IntegerField(initial=1)


    class Meta:
        model = Order
        fields = ['name','phone','address','delivery_date','order_date','product_id','payment_option','quantity','order_status','any_other_details','message']


class ProductForm(ModelForm):
    SERVINGS = (
        ('5-10', '5-10'),
        ('10-15', '10-15'),
        ('15-20', '15-20'),
        ('20-30', '20-30'),
        ('30-40', '30-40'),
    )
    SHAPE = (
        ('AS SHOWN', 'AS SHOWN'),
        ('SQUARE', 'SQUARE'),
        ('ROUND', 'ROUND'),

    )
    TYPE = (
        ('ICING', 'ICING'),
        ('FRESH CREAME', 'FRESH CREAME'),
        ('CHOLOCATE FRESH CREAME', 'CHOLOCATE FRESH CREAME'),
        ('BUTTER CREAME', 'BUTTER CREAME'),
        ('CHOLOCATE BUTTER CREAME', 'CHOLOCATE BUTTER CREAME'),

    )

    SPONGE = (
        ('VANILA', 'VANILA'),
        ('CHOLOCATE', 'CHOLOCATE')

    )

    CREAME = (
        ('VANILA CREAME', 'VANILA CREAME'),
        ('CHOLOCATE CREAME', 'CHOLOCATE CREAME')

    )
    FILLING = (
        ('CHOLOCATE BUTTER CREAME', 'CHOLOCATE BUTTER CREAME'),
        ('CHOLOCATE BUTTER CREAME + JAM', 'CHOLOCATE BUTTER CREAME + JAM'),
        ('WHITE BUTTER CREAME', 'WHITE BUTTER CREAME'),
        ('WHITE BUTTER CREAME + JAM', 'WHITE BUTTER CREAME + JAM'),

    )
    DIETARY_REQUIREMENTS= (
        ('NO DIETARY_REQUIREMENTS', 'NO DIETARY_REQUIREMENTS'),
        ('EAGGLESS', 'EAGGLESS'),
        ('GLUTEN FREE \ WHEAT FREE', ' GLUTEN FREE \ WHEAT FREE'),
        ('NUTS', 'NUTS'),

    )
    serving = forms.ChoiceField(choices=SERVINGS)
    shape = forms.ChoiceField(choices=SHAPE)
    cake_type = forms.ChoiceField(choices=TYPE)
    sponge = forms.ChoiceField(choices=SPONGE)
    creame = forms.ChoiceField(choices=CREAME)
    fillings = forms.ChoiceField(choices=FILLING)
    dietary_requirements = forms.ChoiceField(choices=DIETARY_REQUIREMENTS)


    class Meta:
        model = Product
        fields = ['product_name','price','serving','shape','cake_type','sponge','creame','fillings','dietary_requirements']