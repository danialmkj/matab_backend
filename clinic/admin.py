from django.contrib import admin
from .models import Doctor, Appointment

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'price') # ستون‌هایی که در لیست نمایش داده می‌شوند

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'user', 'status', 'created_at')
    list_filter = ('status',) # فیلتر کردن بر اساس وضعیت رزرو
