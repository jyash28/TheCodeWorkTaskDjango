from django.contrib import admin

# Register your models here.
from django_otp.admin import OTPAdminSite

admin.site.__class__ = OTPAdminSite