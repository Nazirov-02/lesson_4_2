from django.contrib import admin

from shop.models import *

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Like)
admin.site.register(Commentary)