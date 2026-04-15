import cloudinary
from django.http import JsonResponse
from django.shortcuts import render
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import UserModel
import cloudinary
import cloudinary_storage


# Create your views here
@csrf_exempt
def register(req):
    username=req.POST.get('username')
    password=req.POST.get('password')
    image_url = None
    if req.FILES.get('profile_picture'):
        profile_picture=req.FILES.get('profile_picture')
        print("profile picture included")
        image_details=cloudinary.uploader.upload(profile_picture,folders='user_profiles2')
        image_url=image_details.get('secure_url')
        print(image_url)
        
    data={
        'username':username,
        'password':password,
        'profile_picture':image_url
    }
    u1=UserSerializer(data=data)
    if u1.is_valid():
        u1.save()
        return JsonResponse({'status':'user created'})
    return JsonResponse({'status':'something failed'})

    return JsonResponse({'status':"project setup done"})    

  