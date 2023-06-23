from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, TrafficJam, RoadAccident, RoadClosure
from django.utils.translation import gettext_lazy as _

# Register your models here.

class CustomSystemAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),  
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff'),
        }),
    )
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('username',)
    search_fields = ('username', 'email')
    ordering = ('username',)

class TrafficJamAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'message', 'location')
    list_filter = ('date', 'time')
    search_fields = ('message', 'date')
    ordering = ('id', 'date')

class RoadAccidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'message', 'location')
    list_filter = ('date', 'time')
    search_fields = ('message', 'date')
    ordering = ('id', 'date')

class RoadClosureAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'message', 'location')
    list_filter = ('date', 'time')
    search_fields = ('message', 'date')
    ordering = ('id', 'date')

admin.site.register(User, CustomSystemAdmin)
admin.site.register(TrafficJam, TrafficJamAdmin)
admin.site.register(RoadAccident, RoadAccidentAdmin)
admin.site.register(RoadClosure, RoadClosureAdmin)