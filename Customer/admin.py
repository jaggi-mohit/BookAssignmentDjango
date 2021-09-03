from django.contrib import admin
from .models import Customer,BooksPurch,cart

admin.site.register(Customer)
admin.site.register(BooksPurch)
admin.site.register(cart)