from django.urls import path
from .views.main_view import home, single_blog,edit_blog,create_blog,delete_blog
from .views.auth_view import register,login

urlpatterns = [
  path('', home, name="home"),
  path('<int:blog_id>',single_blog, name="blog_detail"),
  path('edit/',edit_blog),
  path('create/',create_blog),
  path('register/',register, name="register"),
  path('login/',login, name="login"),
  path('blogs/<int:blog_id>/delete/', delete_blog, name='delete_blog')  # correct

]