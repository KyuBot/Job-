from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.response import Response
from django.core.mail import EmailMessage
import random

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['POST'])
def email(request, email):
    number = random.randint(100000, 1000000)
    subject_text = '[상호명] 회원가입 인증입니다 확인해 주세요.'
    body_text = f'''회원가입를 위한 이메일인증 절차입니다 하단의 번호를 [상호명] 화면에 입력해 주세요
                인증번호: {number}\
                인증번호를 다른사람이 보지 않게 주의해 주세요.'''

    email = EmailMessage(subject_text, body_text, to=[email])
    result = email.send()
    if result == 1:
        return Response({"result": number}) 
    else:
        return Response({"result": mqwmenjkcjxzkjqwnebmnsdbhqwbhqkbbxjcbkqjkcxzcq})
