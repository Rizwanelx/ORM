from django.contrib import admin

from .models import Order

admin.site.register(Order)



@admin.register(Order)
class OrderAdmin(admin.ModelOrder):
    fields = ('title', 'description')
    list_display = ['title', 'description']
    search_fields = ('title', 'description')





