from django.db import models
from django.contrib.auth.models import User

# مدل پزشک
class Doctor(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام پزشک")
    specialty = models.CharField(max_length=100, verbose_name="تخصص")
    image = models.ImageField(upload_to='doctors/', null=True, blank=True, verbose_name="عکس")
    address = models.TextField(verbose_name="آدرس مطب")
    phone = models.CharField(max_length=20, verbose_name="شماره تلفن")
    bio = models.TextField(verbose_name="بیوگرافی و توضیحات")
    price = models.IntegerField(verbose_name="هزینه ویزیت (تومان)")

    def __str__(self):
        return self.name

# مدل رزرو نوبت
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار'),
        ('confirmed', 'تایید شده'),
        ('cancelled', 'لغو شده'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) # کاربری که رزرو کرده
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) # دکتری که رزرو شده
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True) # زمان ثبت رزرو

    def __str__(self):
        return f"رزرو {self.doctor.name} توسط {self.user.username}"
