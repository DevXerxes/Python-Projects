from django.contrib import admin
from .models import djangoClasses


# Here i registered all attributes from the djangoClassses model all in one
admin.site.register(djangoClasses)
