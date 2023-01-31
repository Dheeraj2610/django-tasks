from django.contrib import admin

# Register your models here.
from .models import dummy_model

admin.site.register(dummy_model)
