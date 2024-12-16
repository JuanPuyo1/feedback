from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ProductForm
from .models import UserProfile

def store_file(file):
    with open("temp/image.png","wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"

# class CreateProfileView(View):
#     def get(self,request):
#         form = ProductForm()
#         return render(request,"profiles/create_profile.html",{
#             "form": form
#         })
    
#     def post(self,request):
#         submited = ProductForm(request.POST, request.FILES)

#         if submited.is_valid():
#             profile = UserProfile(image=request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
        
#         return render(request,"profiles/create_profile.html",{
#             "form": submited
#         })
    