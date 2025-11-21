from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Doctor, Appointment
from .serializers import DoctorSerializer, AppointmentCreateSerializer, AppointmentListSerializer

# 1. لیست تمام پزشکان
class DoctorListAPI(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# 2. ثبت رزرو جدید
class ReserveAPI(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializer

    def perform_create(self, serializer):
        # موقتاً اولین کاربر سیستم را به عنوان رزرو کننده در نظر می‌گیریم
        # چون هنوز سیستم لاگین نداریم
        user = User.objects.first()
        serializer.save(user=user)

# 3. نمایش رزروهای من
class MyAppointmentsAPI(ListAPIView):
    serializer_class = AppointmentListSerializer

    def get_queryset(self):
        # رزروهای اولین کاربر را برمی‌گرداند
        user = User.objects.first()
        if user:
            return Appointment.objects.filter(user=user).order_by('-created_at')
        return Appointment.objects.none()

# 4. چت بات هوشمند پزشکی (ساده شده)
class AIChatAPI(APIView):
    def post(self, request):
        user_message = request.data.get('message', '').lower()
        
        # منطق ساده پاسخگویی
        if 'سردرد' in user_message or 'سر درد' in user_message:
            reply = "برای سردرد استراحت در اتاق تاریک و مصرف مایعات توصیه می‌شود. اگر شدید است به پزشک مراجعه کنید."
        elif 'سلام' in user_message:
            reply = "سلام! چطور می‌توانم به شما کمک کنم؟"
        elif 'نوبت' in user_message:
            reply = "برای گرفتن نوبت، لطفاً از لیست پزشکان یک نفر را انتخاب کنید."
        else:
            reply = "متوجه نشدم. لطفاً علائم خود را دقیق‌تر بگویید یا با پشتیبانی تماس بگیرید."

        return Response({'reply': reply}, status=status.HTTP_200_OK)
