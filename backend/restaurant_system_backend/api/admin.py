from django.contrib import admin
from .models import Restaurant, Contact

# Register models in the admin site.
admin.site.register(Restaurant)
admin.site.register(Contact)