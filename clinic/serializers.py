from rest_framework import serializers
from .models import Doctor, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'image', 'address', 'phone', 'bio', 'price']

    # این تابع باعث می‌شود آدرس عکس کامل (همراه با http) ارسال شود
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

# سریالایزر برای ثبت رزرو (فقط آی‌دی دکتر را می‌گیرد)
class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor']

# سریالایزر برای نمایش لیست رزروها (اطلاعات کامل دکتر را نشان می‌دهد)
class AppointmentListSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer() # نمایش جزئیات دکتر داخل رزرو
    
    class Meta:
        model = Appointment
        fields = ['id', 'doctor', 'status', 'created_at']
