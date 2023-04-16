from django.urls import path
from . import views


urlpatterns = [
path('signup',views.signup, name='signup'),
path('login', views.login_request, name="login"),
path("logout", views.logout_request, name= "logout"),
path('', views.showall, name='showall'),
path('userall', views.userall, name='userall'),
path('save', views.save, name='save'),
path('update/<int:id>', views.update, name='update'),
path('delete/<int:id>', views.delete, name='delete'),

]