from django.shortcuts import render
from .models import Profile
from .serializer import ProfileSerializer
from rest_framework import viewsets

# Create your views here.

# def profile_view(request):
#     return render(request, 'index.html')

# def add_profile(data):
#     Profile.create(name=data['name'], age=data['age'], location=data['location'])
#     return render('response.html')

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer