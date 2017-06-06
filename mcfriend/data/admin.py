from django.contrib import admin
from .models import coupon,following

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(coupon)
admin.site.register(following)
