from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

#importing modles.py from the file which is just outside of views folder
from ..models import blogs


@login_required
def home(request):
  return render(request,'main/home.html')

def single_blog(request):
  return render(request,'main/single_blog.html')


@login_required
def create_blog(request):
  if request.method == 'POST':
    title = request.POST.get("title")
    subtitle = request.POST.get("subtitle")
    description = request.POST.get("description")
    image  = request.FILES.get("image")
    blog = blogs(title=title, subtitle=subtitle, description=description, image=image)
    blog.save()
    return redirect("home")
  else:
    return render(request,'main/create_blog.html')


@login_required
def edit_blog(request):
  return render(request,'main/edit_blog.html')
  



