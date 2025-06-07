from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

#importing modles.py from the file which is just outside of views folder
from ..models import blogs


@login_required
def home(request):
  Blogs=blogs.objects.all()
  return render(request,'main/home.html',{'Blogs':Blogs})

def single_blog(request,blog_id):
  blog= get_object_or_404(blogs,pk=blog_id)
  return render(request,'main/single_blog.html',{"blog":blog})


@login_required
def create_blog(request):
  if request.method == 'POST':
    title = request.POST.get("title")
    subtitle = request.POST.get("subtitle")
    description = request.POST.get("description")
    image  = request.FILES.get("image")
    blog = blogs(title=title, subtitle=subtitle, description=description, image=image,author = request.user)
    blog.save()
    return redirect("home")
  else:
    return render(request,'main/create_blog.html')


@login_required
def edit_blog(request):
  return render(request,'main/edit_blog.html')
  
def delete_blog(request,blog_id):
  blog = get_object_or_404(blogs,pk=blog_id)
  if blog.author == request.user:
    blog.delete()
    return redirect("home")
  else:
    return redirect('blog_detail', blog_id=blog.id)
  
    


