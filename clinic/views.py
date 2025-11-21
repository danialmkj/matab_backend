from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny # این اضافه شد
from .models import Doctor
from .serializers import DoctorSerializer

# API لیست دکترها
class DoctorListAPI(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True, context={'request': request})
        return Response(serializer.data)

# API رزرو نوبت
class ReserveAPI(APIView):
    def post(self, request):
        return Response({'message': 'نوبت با موفقیت ثبت شد (شبیه‌سازی)'}, status=status.HTTP_201_CREATED)

# API لیست نوبت‌های من
class MyAppointmentsAPI(APIView):
    def get(self, request):
        return Response([], status=status.HTTP_200_OK)

# API هوش مصنوعی (اصلاح شده برای رفع ارور CSRF)
class AIChatAPI(APIView):
    # --- این دو خط معجزه می‌کنند و ارور ۴۰۳ رو رفع می‌کنند ---
    authentication_classes = [] 
    permission_classes = [AllowAny]
    # -------------------------------------------------------

    def post(self, request):
        # دریافت پیام کاربر
        user_message = request.data.get('message', '')
        
        if not user_message:
            return Response({'response': "لطفاً چیزی بنویسید!"})

        text = user_message.lower()
        ai_response = ""

        # منطق پاسخ‌دهی
        if 'سلام' in text:
            ai_response = "سلام! حالتون چطوره؟ چه کمکی از دستم برمیاد؟"
        
        elif 'سردرد' in text or 'سر درد' in text:
            ai_response = "برای سردرد استراحت کافی و نوشیدن آب پیشنهاد میشه. اگر طولانیه حتما نوبت دکتر بگیرید."
            
        elif 'دل درد' in text or 'شکم درد' in text:
            ai_response = "برای دل‌درد بهتره غذای سبک بخورید. می‌خواید لیست متخصصین داخلی رو ببینید؟"
            
        elif 'خداحافظ' in text:
            ai_response = "خداحافظ! مراقب سلامتی خودتون باشید."
            
        else:
            ai_response = "متوجه نشدم. من فقط درباره 'سردرد'، 'دل درد' یا احوال‌پرسی اطلاعات دارم."

        return Response({'response': ai_response})
