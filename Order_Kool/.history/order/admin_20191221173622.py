from django.contrib import admin

from .models import Order

# admin.site.register(Order)



@admin.register(Order)
class OrderAdmin(admin.ModelOrder):
    fields = ('order_id', 'name_of_cake','shape')






