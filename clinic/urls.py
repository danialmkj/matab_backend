from django.urls import path
from .views import DoctorListAPI, ReserveAPI, MyAppointmentsAPI, AIChatAPI

urlpatterns = [
    path('doctors/', DoctorListAPI.as_view()),        # لیست دکترها
    path('reserve/', ReserveAPI.as_view()),           # ثبت رزرو
    path('my-appointments/', MyAppointmentsAPI.as_view()), # رزروهای من
    path('chat/', AIChatAPI.as_view()),               # هوش مصنوعی
]
