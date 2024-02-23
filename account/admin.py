from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.forms import EmailAuthenticationForm

class CustomAdminSite(admin.AdminSite):
    login_form = EmailAuthenticationForm

admin_site = CustomAdminSite(name='customadmin')

